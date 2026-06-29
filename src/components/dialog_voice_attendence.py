import streamlit as st
from src.database.db import create_subject
from src.pipelines.voice_pipelines import process_bulk_audio
import pandas as pd
from src.database.config import supabase
from datetime import datetime
from src.components.attendence_result_dialogue import show_attendance_result


@st.dialog("Voice Attendance")
def voice_attendence_dialog(selected_subject_id):
    st.write('Record audio of students saying I am present. Then AI will recognize the students.')

    audio_data = st.audio_input("Record classroom audio")

    if st.button('Analyze Audio', width='stretch', type='primary'):
        if not audio_data:
            st.warning("Please record audio first.")
            return

        with st.spinner('Processing Audio data'):
            enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id', selected_subject_id).execute()
            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning('No students enrolled on this course.')
                return

            candidates_dict = {
                s['students']['student_id']: s['students']['voice_embedding']
                for s in enrolled_students if s['students'].get('voice_embedding')
            }

            if not candidates_dict:
                st.error('No enrolled students have a voice profile registered.')
                return

            audio_bytes = audio_data.read()
            detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

            results, attendance_to_logs = [], []
            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student = node['students']                          
                score = detected_scores.get(student['student_id'], 0.0) 
                is_present = bool(score > 0)

                results.append({
                    "Name": student['name'],
                    "ID": student['student_id'],
                    "Source": round(score, 3) if is_present else "_",
                    "Status": "✅ Present" if is_present else "❌ Absent"
                })

                attendance_to_logs.append({
                    'student_id': student['student_id'],
                    'subject_id': selected_subject_id,
                    'timestamp': current_timestamp,
                    'is_present': is_present
                })

            
            st.session_state['voice_attendance_results'] = (pd.DataFrame(results), attendance_to_logs)

    if st.session_state.get('voice_attendance_results'):
        st.divider()
        df_results, logs = st.session_state['voice_attendance_results']
        show_attendance_result(df_results, logs)