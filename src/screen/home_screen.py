import streamlit as st
from src.components.header import header_home 
from src.components.features import feature_highlights
from src.ui.base_layout import style_base_layout, style_background_home
from src.components.How_it_works import how_it_works

from src.components.footer import footer_home
def home_continue_button(label, target_login_type):
    if st.button(label, use_container_width=True):
        st.session_state['login_type'] = target_login_type
        st.rerun()


def home_screen():

    header_home()
    st.markdown('<div style="margin-bottom: 4rem;"></div>', unsafe_allow_html=True)
    style_background_home()
   
    style_base_layout()
    
    
    st.markdown("""
        <style>
        div.stButton > button {
            background: linear-gradient(135deg, #4361EE 0%, #00D4FF 100%);
            color: #fff;
            border: none;
            border-radius: 10px;
            padding: 0.75rem 2.5rem;
            font-size: 16px;
            font-weight: 600;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        div.stButton > button:hover {
            transform: scale(1.03);
            box-shadow: 0 6px 16px rgba(67,97,238,0.4);
        }
                
        .biomark-sub {
            font-size: 15px;
            font-weight: 400;
            margin: 0 4rem 1.5rem;
            line-height: 1.5;
            text-align: center;
            color: #FFFFFF;
            letter-spacing: 0.3px;
        }
        .biomark-tagline {
            font-size: 28px;
            font-weight: 700;
            text-align: center;
            margin: 0 0 1.5rem;
            background: linear-gradient(135deg, #00D4FF 0%, #4361EE 40%, #D4537E 80%, #F0997B 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: 0.3px;
        }
                
        </style>
        <div>
            <h2 class= "biomark-tagline">Mark Attendance with AI Precision</h2>
            <p class="biomark-sub">AI-driven attendance system for tracking using real-time voice and video recognition for seamless classroom management.</p>
                
        </div>
        
         
    """, unsafe_allow_html=True)
    st.markdown('<div style="margin-bottom: 2rem;"></div>', unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)

    with col1:
        home_continue_button("Teacher Portal →", "teacher")

    with col3:
        home_continue_button("Student Portal →", "student")

    
        
    
    feature_highlights()
    how_it_works()
    
    footer_home()
