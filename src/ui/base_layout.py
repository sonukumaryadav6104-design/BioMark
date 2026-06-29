import streamlit as st

def style_base_layout():
    st.markdown("""
        <style>
                # #MainMenu, footer, header {
                #    visibility: hidden;
                # }
                .block-container {
                    padding-top: 1.5rem !important;
                }

                
        </style>
               """,
            unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
                .stApp{
                   background: linear-gradient(135deg, #10131C 0%, #1B1F33 40%, #1E2A4A 70%, #154360 100%) !important;
                }
        </style>
               """
            ,unsafe_allow_html=True)



def style_background_home():
    st.markdown("""
        <style>
               .stApp{
                   background:linear-gradient(135deg, #0F0F1E 0%, #1A1A2E 40%, #16213E 70%, #0F3460 100%) !important;
                }
        </style>
               """
            ,unsafe_allow_html=True)   