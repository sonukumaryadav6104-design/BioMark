import time
import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.database.db import check_teacher_exists, create_teacher, teacher_login2 , get_teacher_subjects
from src.components.footer import render_footer
from src.components.create_subject_dialog import create_subject_dialog
from src.components.share_subject_dialog import share_subject_dialog
from src.components.subject_card import subject_card
from src.components.add_photos_dialog import add_photos_dialog
from src.components.attendence_result_dialogue import attendance_result_dialog
from src.components.dialog_voice_attendence import voice_attendence_dialog

from src.pipelines.face_pipelines import predict_attendence
import  numpy as np
import pandas as pd
from src.database.config import supabase
from src.database.db import get_attendence_for_teacher
from datetime import datetime


def teacher_login():
    with st.container(border=True):
        st.markdown("""
            <div style="
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 20px;
            ">
                <div style="
                    width: 4px;
                    height: 28px;
                    background: #4361EE;
                    border-radius: 4px;
                "></div>
                <span style="
                    color: white;
                    font-size: 20px;
                    font-weight: 600;
                    letter-spacing: 0.3px;
                ">Teacher Login</span>
            </div>
        """, unsafe_allow_html=True)

        teacher_username = st.text_input(
            "Username",
            placeholder="Enter your username",
            key="login_username"
        )

        teacher_password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        if st.button(
            "Login →",
            key="teacher_login_btn",
            use_container_width=True
        ):
            if not teacher_username or not teacher_password:
                st.error("Please fill in all fields")
            else:
                result = teacher_login2(teacher_username, teacher_password)
                if result:
                    st.session_state['teacher'] = result
                    st.session_state['teacher_logged_in'] = True
                    st.toast("Welcome back!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Invalid username or password")

        st.markdown("""
            <div style="
                text-align: center;
                margin-top: 14px;
                color: rgba(255,255,255,0.4);
                font-size: 13px;
            ">Forgot password? <span style="color:#4361EE; cursor:pointer;">Reset here</span></div>
        """, unsafe_allow_html=True)


def register_teacher(teacher_name, teacher_username, teacher_email, teacher_password, teacher_confirm_password):
    if not teacher_name or not teacher_username or not teacher_email or not teacher_password or not teacher_confirm_password:
        return False, "All fields are required!"

    if check_teacher_exists(teacher_username):
        return False, "Username already taken"

    if teacher_password != teacher_confirm_password:
        return False, "Passwords do not match"

    try:
        create_teacher(teacher_name, teacher_username, teacher_email, teacher_password)
        return True, "Account created! Please login now."
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"


def teacher_register():
    with st.container(border=True):
        st.markdown("""
            <div style="
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 20px;
            ">
                <div style="
                    width: 4px;
                    height: 28px;
                    background: #00D4FF;
                    border-radius: 4px;
                "></div>
                <span style="
                    color: white;
                    font-size: 20px;
                    font-weight: 600;
                    letter-spacing: 0.3px;
                ">Create Account</span>
            </div>
        """, unsafe_allow_html=True)

        col_a, col_b = st.columns(2)
        with col_a:
            teacher_name = st.text_input(
                "Full Name",
                placeholder="John Doe",
                key="register_name"
            )
        with col_b:
            teacher_username = st.text_input(
                "Username",
                placeholder="johndoe123",
                key="register_username"
            )

        teacher_email = st.text_input(
            "Official Email",
            placeholder="teacher@school.edu",
            key="register_email"
        )

        col_c, col_d = st.columns(2)
        with col_c:
            teacher_password = st.text_input(
                "Password",
                type="password",
                key="register_password"
            )
        with col_d:
            teacher_confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                key="confirm_password"
            )

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        if st.button(
            "Create Account →",
            key="teacher_register_btn",
            use_container_width=True
        ):
            success, message = register_teacher(
                teacher_name,
                teacher_username,
                teacher_email,
                teacher_password,
                teacher_confirm_password
            )
            if success:
                st.success(message)
                time.sleep(2)
                st.rerun()
            else:
                st.error(message)

        st.markdown("""
            <div style="
                text-align: center;
                margin-top: 14px;
                color: rgba(255,255,255,0.4);
                font-size: 13px;
            "> Already have an account? <span style="color:#4361EE; cursor:pointer;">Sign in to continue.</span></div>
        """, unsafe_allow_html=True)


def teacher_screen():

    style_background_dashboard()
    style_base_layout()

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

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

    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');

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

    /* Input labels */
    div[data-testid="stVerticalBlockBorderWrapper"] label {
        color: rgba(255,255,255,0.55) !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.8px !important;
    }

    /* Input fields */
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

    /* Selectbox */
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

    /* Logout button (overrides the transparent Home style above when logged in) */
    div[data-testid="stColumns"] > div:last-child button[kind="secondary"] {
        background: rgba(239, 68, 68, 0.1) !important;
        color: #ef4444 !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
    }

    div[data-testid="stColumns"] > div:last-child button[kind="secondary"]:hover {
        background: rgba(239, 68, 68, 0.18) !important;
        border-color: rgba(239, 68, 68, 0.5) !important;
        color: #ff6b6b !important;
    }

    /* Divider */
    hr {
        border-color: rgba(255,255,255,0.06) !important;
        margin: 16px 0 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # Header
    c1, c2 = st.columns([5, 1], vertical_alignment="center", gap="xxlarge")

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
        if st.session_state.get("teacher_logged_in"):
            if st.button("Logout", key="teacher_logout_btn", type="secondary"):
                del st.session_state['teacher']
                st.session_state['teacher_logged_in'] = False
                st.rerun()
        else:
            if st.button("← Home", key="loginbackbtn"):
                st.session_state['login_type'] = None
                st.rerun()

    st.divider()

    # st.markdown(
    #     "<div class='portal-heading'>Teacher Portal</div>",
    #     unsafe_allow_html=True
    # )

    if st.session_state.get("teacher_logged_in"):
        teacher_dashboard()

    else:
        col1, col2 = st.columns(2, gap="large")

        with col1:
            teacher_login()

        with col2:
            teacher_register()


def teacher_dashboard():
    teacher_data = st.session_state.teacher

    st.subheader(f"Welcome, {teacher_data['name']}")

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendence'

    st.space()

    st.space()
    tab1, tab2, tab3 = st.columns(3)

    with tab1:
        type1="primary" if st.session_state.current_teacher_tab == 'take_attendence' else "tertiary"
        if st.button('Take Attendence',type=type1, width='stretch',use_container_width=True, icon='📸'):
            st.session_state.current_teacher_tab = 'take_attendence'
            st.rerun()

    with tab2:
        type2 ="primary" if st.session_state.current_teacher_tab =='manage_subjects' else "tertiary"
        if st.button('Manage Subjects', type=type2,use_container_width=True,width='stretch', icon='📚'):
            st.session_state.current_teacher_tab = 'manage_subject'
            st.rerun()
            

    with tab3:
        type3 ="primary" if st.session_state.current_teacher_tab =='attendence_records' else "tertiary"
        
        if st.button('Attendence Records', type=type3,use_container_width=True, width='stretch',icon='🗂️'):
            st.session_state.current_teacher_tab = 'attendence_records'
        
            st.rerun()
           
    if st.session_state.current_teacher_tab == "take_attendence":
            teacher_tab_take_attendence()
        
    if st.session_state.current_teacher_tab == "manage_subject":
            
                teacher_tab_manage_subjects()
            
    if st.session_state.current_teacher_tab == "attendence_records":
            teacher_tab_attendence_records()        
        
        
    st.space()
    st.space()
    render_footer()
    
st.space()
st.space()

def teacher_tab_take_attendence():
    teacher_id = st.session_state.teacher['teacher_id']
    st.header("Take AI Attendance")

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning('You haven\'t created any subjects yet! Please create one to begin!')
        return

    subject_options = {f"{s['name']} - {s['subject_code']}": s['subject_id'] for s in subjects}

    col1, col2 = st.columns([3, 1], vertical_alignment="bottom")

    with col1:
        selected_subject_label = st.selectbox('Select Subject', options=list(subject_options.keys()))

    with col2:
        if st.button('📸 Add Photos', type='primary', width='stretch'):
            add_photos_dialog()

    selected_subject_id = subject_options[selected_subject_label]

    st.divider()

    if st.session_state.attendance_images:
        st.header('Added Photos')
        gallery_cols = st.columns(4)

        for idx, img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4]:
                st.image(img, width='stretch', caption=f'Photo {idx + 1}')

    has_photos = bool(st.session_state.attendance_images)
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button('Clear all photos', width='stretch', type='tertiary', disabled=not has_photos):
            st.session_state.attendance_images = []
            st.rerun()

    with c2:
        if st.button('Run Face Analysis', width='stretch', disabled=not has_photos):
            all_detected_id = {}

            for idx, img in enumerate(st.session_state.attendance_images):
                img_np = np.array(img.convert('RGB'))

                detected, _, _ = predict_attendence(img_np)

                if detected:
                    for sid in detected.keys():
                        # FIX 1: use str keys consistently to avoid int/str mismatch
                        all_detected_id.setdefault(str(sid), []).append(f"Photo {idx + 1}")
                        # FIX 2: was missing f-prefix → was always "Photo { idx + 1}" literally

            enrolled_res = (
                supabase.table('subject_students')
                .select("*, students(*)")
                .eq('subject_id', selected_subject_id)
                .execute()
            )
            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning('No students enrolled in this subject.')

            else:
                results, attendance_to_logs = [], []
                current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                for node in enrolled_students:
                    student = node['students']
                    # FIX 3: match str keys used during detection above
                    sources = all_detected_id.get(str(student['student_id']), [])

                    is_present = len(sources) > 0

                    results.append({
                        "Name":   student['name'],
                        "ID":     student['student_id'],
                        "Source": ", ".join(sources) if is_present else "—",
                        "Status": "✅ Present" if is_present else "❌ Absent"
                    })

                    attendance_to_logs.append({
                        'student_id': student['student_id'],
                        'subject_id': selected_subject_id,
                        'timestamp':  current_timestamp,
                        'is_present': bool(is_present)
                    })

                # FIX 4: was outside the else block → crashed with NameError when no students
                attendance_result_dialog(pd.DataFrame(results), attendance_to_logs)

    with c3:
        # FIX 5: dialog was called unconditionally on every rerun — caused phantom dialog pops
        if st.button('Use voice Attendance', type='primary', width='stretch'):
            voice_attendence_dialog(selected_subject_id)
            
                       
    
    
def teacher_tab_manage_subjects():
    teacher_id = st.session_state.teacher['teacher_id']
    st.space()
    st.space()

    c1, c2 = st.columns([1, 1], vertical_alignment="bottom")

    with c1:
        st.subheader("Manage Subjects")

    with c2:
        if st.button("Create New Subject"):
            create_subject_dialog(teacher_id)

    subjects = get_teacher_subjects(teacher_id)

    st.markdown("""
    <style>
    div[data-testid="stButton"] button[kind="secondary"]{
        background: linear-gradient(135deg, #38BDF8, #2563EB, #EC4899) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        box-shadow: 0 8px 20px rgba(59,130,246,0.30);
        transition: all 0.3s ease;
    }
    div[data-testid="stButton"] button[kind="secondary"]:hover{
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(236,72,153,0.35);
    }
    </style>
    """, unsafe_allow_html=True)

    if subjects:
        # Iterate subjects in pairs
        for i in range(0, len(subjects), 2):
            col1, col2 = st.columns(2)

            for col, idx in zip([col1, col2], [i, i + 1]):
                if idx >= len(subjects):
                    break  # No second subject in this row
                sub = subjects[idx]

                with col:
                    stats = [
                        ("👥", "Students", sub['total_students']),
                        ("⌚", "Classes", sub['total_classes']),
                    ]
                    subject_card(
                        name=sub['name'],
                        code=sub['subject_code'],
                        section=sub['section'],
                        stats=stats,
                    )
                    if st.button(
                        f"🔗 Share Code: {sub['subject_code']}",
                        key=f"share_{sub['subject_code']}"
                    ):
                        share_subject_dialog(sub['name'], sub['subject_code'])
    else:
        st.info("No subjects found. Create one above.")   
          
def teacher_tab_attendence_records():
    st.header("Check Attendance Records")

    teacher_id = st.session_state.teacher['teacher_id']
    records = get_attendence_for_teacher(teacher_id)

    if not records:
        st.info("No attendance records found.")
        return

    data = []

    for r in records:
        ts = r.get('timestamp')
        data.append({
            "ts_group": ts.split(".")[0] if ts else None,
            "Time": datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "N/A",
            "Subject": r['subjects']['name'],
            "Subject Code": r['subjects']['subject_code'],
            "is_present": bool(r.get('is_present', False))
        })

    df = pd.DataFrame(data)

    summary = (
        df.groupby(['ts_group', 'Time', 'Subject', 'Subject Code'])
        .agg(
            Present_Count=('is_present', 'sum'),
            Total_Count=('is_present', 'count')
        ).reset_index()
    )

    summary['Attendance Stats'] = (
        "✅ " + summary['Present_Count'].astype(str) + " / "
        + summary['Total_Count'].astype(str) + " Students"
    )

    display_df = (
        summary.sort_values(by='ts_group', ascending=False)
        [['Time', 'Subject', 'Subject Code', 'Attendance Stats']]
    )

    st.dataframe(display_df, use_container_width=True, hide_index=True)
