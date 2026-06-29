import streamlit as st

def header_home():
    st.markdown(
        """
        <style>
        .biomark-header {
            background: linear-gradient(135deg, #0F3460 0%, #16213E 50%, #1A1A2E 100%);
            border-radius: 16px;
            padding: 1.25rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 18px;
            margin-bottom: 1.5rem;
            width: 100%;
            box-sizing: border-box;
            box-shadow: 0 8px 24px rgba(0,0,0,0.25);
            border: 1px solid rgba(255,255,255,0.08);
        }
        .biomark-left {
            display: flex;
            align-items: center;
            gap: 18px;
        }
        .biomark-icon {
            min-width: 56px;
            width: 46px;
            height: 46px;
            border-radius: 12px;
            background: linear-gradient(135deg, #4361EE 0%, #00D4FF 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            color: #fff;
            box-shadow: 0 4px 12px rgba(67,97,238,0.4);
        }
        .biomark-title {
            margin: 0;
            font-size: 24px;
            font-weight: 700;
            color: #fff;
            letter-spacing: 0.3px;
        }
        .biomark-actions {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .biomark-login-btn {
            padding: 10px 22px;
            background: #00D4FF;
            color: #042C53;
            border: none;
            font-weight: 700;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            text-decoration: none;
        }
        .biomark-signup-btn {
            padding: 10px 22px;
            background: #00D4FF;
            color: #042C53;
            border: none;
            font-weight: 700;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            text-decoration: none;
        }
        @media (max-width: 768px) {
            .biomark-header { flex-direction: column; align-items: flex-start; gap: 16px; }
        }
        </style>

        <div class="biomark-header">
            <div class="biomark-left">
                <div class="biomark-icon">🧬</div>
                <p class="biomark-title">BioMark</p>
            </div>
            <div class="biomark-actions">
                <p class="biomark-login-btn">Home</p>
                <p class="biomark-signup-btn">Features</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )



def header_dashboard():
    st.markdown(
        """
        <style>
        .biomark-header {
            background: linear-gradient(135deg, #0F3460 0%, #16213E 50%, #1A1A2E 100%);
            border-radius: 16px;
            padding: 1.25rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 18px;
            margin-bottom: 1.5rem;
            width: 100%;
            box-sizing: border-box;
            box-shadow: 0 8px 24px rgba(0,0,0,0.25);
            border: 1px solid rgba(255,255,255,0.08);
        }
        .biomark-left {
            display: flex;
            align-items: center;
            gap: 18px;
        }
        .biomark-icon {
            min-width: 56px;
            width: 46px;
            height: 46px;
            border-radius: 12px;
            background: linear-gradient(135deg, #4361EE 0%, #00D4FF 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            color: #fff;
            box-shadow: 0 4px 12px rgba(67,97,238,0.4);
        }
        .biomark-title {
            margin: 0;
            font-size: 24px;
            font-weight: 700;
            color: #fff;
            letter-spacing: 0.3px;
        }
        <div class="biomark-header">
            <div class="biomark-left">
                <div class="biomark-icon">🧬</div>
                <p class="biomark-title">BioMark</p>
            </div>
            
        </div>
        """,
        unsafe_allow_html=True
    )