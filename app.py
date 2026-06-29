import streamlit as st
from src.screen.home_screen import home_screen
from src.screen.student_screen import student_screen
from src.screen.teacher_screen import teacher_screen
from src.components.auto_enroll_dialog import auto_enroll_dialog

st.set_page_config(layout="wide")

def main():
    
    st.set_page_config(
        page_title='Bio_Mark - Making Attendence faster using AI',
        page_icon='🧑‍🎓',
        
    )
    
    
    
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    join_code = st.query_params.get('join-code')

    if join_code:
        if st.session_state.get('login_type') != 'student':
            st.session_state.login_type = 'student'
            st.rerun()

        if (
            st.session_state.get('is_logged_in')
            and st.session_state.get('user_role') == 'student'
        ):
            auto_enroll_dialog(join_code)

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            home_screen()

if __name__ == "__main__":
    main()