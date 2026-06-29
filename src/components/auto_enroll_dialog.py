import streamlit as st
import time
from src.database.db import enroll_student_to_subject
from src.database.config import supabase


@st.dialog("Quick Enrollment")
def auto_enroll_dialog(subject_code: str):
    student_id = st.session_state.student_data["student_id"]

  
    try:
        res = (
            supabase.table("subjects")
            .select("subject_id, name")
            .eq("subject_code", subject_code)
            .execute()
        )
    except Exception as e:
        st.error(f"Could not reach the database. Please try again. ({e})")
        return

    if not res.data:
        st.error(f"No subject found with code **{subject_code}**.")
        if st.button("Close", key="close_not_found"):
            st.query_params.clear()
            st.rerun()
        return

    subject = res.data[0]


    try:
        check = (
            supabase.table("subject_students")
            .select("*")
            .eq("subject_id", subject["subject_id"])
            .eq("student_id", student_id)
            .execute()
        )
    except Exception as e:
        st.error(f"Could not verify enrolment status. Please try again. ({e})")
        return

    if check.data:
        st.info(f"You're already enrolled in **{subject['name']}**!")
        if st.button("Got it!", key="close_already_enrolled"):
            st.query_params.clear()
            st.rerun()
        return

    
    st.markdown(f"Would you like to enroll in **{subject['name']}**?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("No thanks", use_container_width=True, key="decline_enroll"):
            st.query_params.clear()
            st.rerun()

    with col2:
        if st.button("Yes, Enroll Now!", type="primary",
                     use_container_width=True, key="confirm_enroll"):
            try:
                enroll_student_to_subject(student_id, subject["subject_id"])
            except Exception as e:
                st.error(f"Enrolment failed. Please try again. ({e})")
                return

            st.success(f"Successfully joined **{subject['name']}**!")
            time.sleep(2)
            st.query_params.clear()
            st.rerun()