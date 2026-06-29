import streamlit as st
import time
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.database.db import get_all_students, create_student ,get_student_subjects ,get_student_attendence,unenroll_student_to_subject
import numpy as np
from PIL import Image
from src.pipelines.face_pipelines import predict_attendence, get_face_embedding, train_classifier
from src.pipelines.voice_pipelines import get_voice_embedding
from src.components.header import header_dashboard
from src.components.footer import render_footer
from src.components.enroll_dialog import enroll_dialog
from src.components.subject_card import subject_card

def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        st.subheader(f"Welcome, {student_data['name']}")
    with c2:
        if st.button("Logout", type='secondary', key='logoutbtn'):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    st.write("")

    c1, c2, c3 = st.columns([2, 1, 1], vertical_alignment='center', gap='xlarge')
    with c1:
        st.header('Your Enrolled Subjects')
    with c2:
        if st.button('Enroll in Subjects', type='primary', use_container_width=True):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading your enrolled subjects...'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendence(student_id)

    stats_map = {}
    for log in logs:
        sid = log['subject_id']
        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}
        stats_map[sid]['total'] += 1
        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']
        stats = stats_map.get(sid, {"total": 0, "attended": 0})

        with cols[i % 2]:
            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=[
                    ("📅", "Total",    stats['total']),
                    ("✅", "Attended", stats['attended']),
                ],
            )
            if st.button(
                "Unenroll from the course",
                type='tertiary',
                use_container_width=True,
                key=f"unenroll_{sid}"
            ):
                unenroll_student_to_subject(student_id, sid)
                st.toast(f'Unenrolled from {sub["name"]} successfully')
                st.rerun()

    render_footer()
def student_screen():

    style_background_dashboard()
    style_base_layout()

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');

    * {
        font-family: 'Inter', sans-serif !important;
    }

    .biomark-title {
        color: white;
        font-size: 46px;
        font-weight: 700;
        margin-bottom: 0;
        line-height: 1.1;
        letter-spacing: -1px;
    }

    .biomark-title span {
        background: linear-gradient(90deg, #4361EE, #00D4FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .biomark-subtitle {
        color: rgba(255,255,255,0.5);
        font-size: 15px;
        margin-top: 6px;
        font-weight: 400;
        letter-spacing: 0.2px;
    }

    .portal-heading {
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: white;
        font-family: 'Orbitron', sans-serif;
    }

    /* Cards */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #0d0d0d !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 14px !important;
        padding: 10px !important;
        box-shadow: 0 2px 40px rgba(0,0,0,0.4) !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] label {
        color: rgba(255,255,255,0.55) !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.8px !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] input {
        background-color: #1a1a1a !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 8px !important;
        color: white !important;
        font-size: 14px !important;
        padding: 10px 14px !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] input:focus {
        border: 1px solid #4361EE !important;
        box-shadow: 0 0 0 3px rgba(67,97,238,0.15) !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] input::placeholder {
        color: rgba(255,255,255,0.2) !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] div[data-baseweb="select"] > div {
        background-color: #1a1a1a !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 8px !important;
        color: white !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] div[data-baseweb="select"] span {
        color: white !important;
        font-size: 14px !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] div[data-baseweb="select"] svg {
        fill: rgba(255,255,255,0.4) !important;
    }

    /* Login button */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) div[data-testid="stButton"] button {
        background: #4361EE !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        letter-spacing: 0.3px !important;
        padding: 12px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 16px rgba(67,97,238,0.35) !important;
    }

    div[data-testid="stHorizontalBlock"] > div:nth-child(1) div[data-testid="stButton"] button:hover {
        background: #3451d1 !important;
        box-shadow: 0 6px 20px rgba(67,97,238,0.5) !important;
        transform: translateY(-1px) !important;
    }

    /* Register button */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #00D4FF, #0099cc) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        letter-spacing: 0.3px !important;
        padding: 12px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 16px rgba(0,212,255,0.3) !important;
    }

    div[data-testid="stHorizontalBlock"] > div:nth-child(2) div[data-testid="stButton"] button:hover {
        box-shadow: 0 6px 20px rgba(0,212,255,0.45) !important;
        transform: translateY(-1px) !important;
    }

    /* Home button */
    div[data-testid="stColumns"] > div:last-child div[data-testid="stButton"] button {
        background: transparent !important;
        color: rgba(255,255,255,0.6) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 8px !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
    }

    div[data-testid="stColumns"] > div:last-child div[data-testid="stButton"] button:hover {
        border-color: rgba(255,255,255,0.35) !important;
        color: white !important;
        transform: none !important;
    }

    hr {
        border-color: rgba(255,255,255,0.06) !important;
        margin: 16px 0 !important;
    }

    /* ─── Upload Zone Styling ─── */
    [data-testid="stFileUploader"] {
        background: linear-gradient(145deg, rgba(67,97,238,0.06), rgba(0,212,255,0.04)) !important;
        border: 2px dashed rgba(67,97,238,0.45) !important;
        border-radius: 16px !important;
        padding: 12px !important;
        transition: border-color 0.25s ease, background 0.25s ease !important;
        position: relative !important;
        z-index: 1 !important;
    }

    [data-testid="stFileUploader"]:hover {
        border-color: rgba(0,212,255,0.7) !important;
        background: linear-gradient(145deg, rgba(67,97,238,0.1), rgba(0,212,255,0.07)) !important;
    }

    [data-testid="stFileUploader"] section {
        background: transparent !important;
        border: none !important;
        padding: 24px 16px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 8px !important;
    }

    [data-testid="stFileUploader"] section > div {
        color: rgba(255,255,255,0.75) !important;
        font-size: 14px !important;
        text-align: center !important;
    }

   [data-testid="stFileUploader"] button[kind="secondary"] {
    background: linear-gradient(135deg, #4361EE, #00D4FF) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 8px 20px !important;
}

    [data-testid="stFileUploader"] button:hover {
        box-shadow: 0 6px 20px rgba(0,212,255,0.45) !important;
        transform: translateY(-1px) !important;
    }

    [data-testid="stFileUploader"] [data-testid="stMarkdownContainer"] p {
        color: rgba(255,255,255,0.5) !important;
        font-size: 12px !important;
    }

    /* ─── Camera Input Styling ─── */
    [data-testid="stCameraInput"] {
        border: 2px solid rgba(67,97,238,0.3) !important;
        border-radius: 16px !important;
        overflow: hidden !important;
        position: relative !important;
        z-index: 1 !important;
    }

    [data-testid="stCameraInput"] button {
        background: linear-gradient(135deg, #4361EE, #00D4FF) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 14px rgba(67,97,238,0.4) !important;
    }

    /* Caption */
    [data-testid="stCaptionContainer"] p {
        color: rgba(255,255,255,0.35) !important;
        font-size: 12px !important;
        text-align: center !important;
        letter-spacing: 0.3px !important;
        margin-top: 8px !important;
    }

    </style>
    """, unsafe_allow_html=True)

    if "student_data" in st.session_state:
        student_dashboard()
        return

    # ── Header ──────────────────────────────────────────────
    c1, c2 = st.columns([5, 1], vertical_alignment="center")

    with c1:
        st.markdown("""
        <div class="biomark-title">
            🧬 Bio<span>Mark</span>
        </div>
        <div class="biomark-subtitle">
            Smart Attendance Management for Educators
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Home", key="loginbackbtn", use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    st.divider()

    st.markdown(
        "<div class='portal-heading'>Student Portal</div>",
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<h3 style='text-align:center;'>Login using Face Scan</h3>",
        unsafe_allow_html=True
    )

    show_registration = False

    # ── Capture mode init ────────────────────────────────────
    if "capture_mode" not in st.session_state:
        st.session_state.capture_mode = "camera"

    # ── Mode toggle buttons ──────────────────────────────────
    st.markdown('<div class="capture-toggle-row">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4, vertical_alignment="center")

    with col1:
        if st.button("📷  Camera", use_container_width=True,
                     type="primary" if st.session_state.capture_mode == "camera" else "secondary",
                     key="mode_camera_btn"):
            st.session_state.capture_mode = "camera"
            # ✅ Wipe every ghost widget key with either prefix
            for k in [k for k in st.session_state
                      if k.startswith("file_uploader") or k.startswith("camera_input")]:
                del st.session_state[k]
            st.rerun()

    with col2:
        if st.button("🖼️  Upload Photo", use_container_width=True,
                     type="primary" if st.session_state.capture_mode == "upload" else "secondary",
                     key="mode_upload_btn"):
            st.session_state.capture_mode = "upload"
            # ✅ Wipe every ghost widget key with either prefix
            for k in [k for k in st.session_state
                      if k.startswith("file_uploader") or k.startswith("camera_input")]:
                del st.session_state[k]
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # ── ✅ Dynamic key = brand-new widget on every mode switch ──
    photo_source = None

    if st.session_state.capture_mode == "camera":
        photo_source = st.camera_input(
            "Position your face in the center",
            label_visibility="collapsed",
            key=f"camera_input_{st.session_state.capture_mode}"
        )
    else:
        st.markdown("""
            <div style="
                text-align: center;
                margin-bottom: 8px;
                color: rgba(255,255,255,0.45);
                font-size: 13px;
                letter-spacing: 0.3px;
            ">
                📂 &nbsp; Drag & drop or click to browse
            </div>
        """, unsafe_allow_html=True)

        photo_source = st.file_uploader(
            "Upload a clear, front-facing photo",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed",
            key=f"file_uploader_{st.session_state.capture_mode}"
        )

    st.caption("Use a well-lit, front-facing photo for best recognition accuracy.")

    # ── Face recognition ─────────────────────────────────────
    if photo_source:
        img = np.array(Image.open(photo_source).convert("RGB"))
        with st.spinner('AI is scanning..'):
            detected, all_ids, num_faces = predict_attendence(img)

            if num_faces == 0:
                st.warning('Face not found')
            elif num_faces > 1:
                st.warning('Multiple faces found')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next(
                        (s for s in all_students if s['student_id'] == student_id), None
                    )
                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f"Welcome Back {student['name']}")
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('Face not recognized! You might be a new student!')
                    show_registration = True

    # ── Registration form ────────────────────────────────────
    if show_registration:
        with st.container(border=True):
            st.header('Register your Profile')
            new_name = st.text_input("Enter your name", placeholder='Eg. Sonu Kumar')

            st.subheader('Optional: Voice Enrollment')
            st.info("Enroll your voice for attendance verification")

            audio_data = None

            try:
                audio_data = st.audio_input(
                    'Record a short phrase like "I am present, My name is Akash."'
                )
            except Exception as e:
                st.error(f'Audio capture failed: {e}')

            if st.button('Create Account', type='primary'):
                if new_name:
                    with st.spinner('Creating Profile..'):
                        encodings = get_face_embedding(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(
                                new_name,
                                face_embedding=face_emb,
                                voice_embedding=voice_emb
                            )

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Hi {new_name}!')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error('Could not capture facial features for registration')
                else:
                    st.warning('Please enter your name!')