import streamlit as st

def footer_home():
    st.markdown("""
        <style>
        .biomark-footer {
            background: #16213E;
            border-radius: 16px;
            padding: 2rem 2.5rem;
            display: flex;
            flex-direction: column;
            gap: 24px;
            width: 100%;
            box-sizing: border-box;
            border: 1px solid rgba(255,255,255,0.08);
            margin-top: 2rem;
        }
        .footer-top {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 24px;
        }
        .footer-brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .footer-icon {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            background: linear-gradient(135deg, #4361EE 0%, #00D4FF 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            color: #fff;
        }
        .footer-brand-name {
            margin: 0;
            font-size: 18px;
            font-weight: 700;
            color: #fff;
        }
        .footer-brand-sub {
            margin: 0;
            font-size: 12.5px;
            color: rgba(255,255,255,0.5);
        }
        .footer-links {
            display: flex;
            gap: 40px;
            flex-wrap: wrap;
        }
        .footer-col-title {
            margin: 0 0 10px;
            font-size: 13px;
            font-weight: 600;
            color: #fff;
        }
        .footer-link {
            margin: 0 0 6px;
            font-size: 13px;
            color: rgba(255,255,255,0.6);
        }
        .footer-bottom {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            border-top: 1px solid rgba(255,255,255,0.08);
            padding-top: 16px;
        }
        .footer-copyright {
            margin: 0;
            font-size: 12.5px;
            color: rgba(255,255,255,0.45);
        }
        .footer-socials {
            display: flex;
            gap: 14px;
        }
        .footer-socials i {
            font-size: 18px;
            color: rgba(255,255,255,0.6);
        }
        </style>

        <div class="biomark-footer">
            <div class="footer-top">
                <div class="footer-brand">
                    <div class="footer-icon"><i class="ti ti-dna"></i></div>
                    <div>
                        <p class="footer-brand-name">BioMark</p>
                        <p class="footer-brand-sub">AI attendance, simplified</p>
                    </div>
                </div>
                <div class="footer-links">
                    <div>
                        <p class="footer-col-title">Product</p>
                        <p class="footer-link">Features</p>
                        <p class="footer-link">Pricing</p>
                        <p class="footer-link">Security</p>
                    </div>
                    <div>
                        <p class="footer-col-title">Company</p>
                        <p class="footer-link">About</p>
                        <p class="footer-link">Contact</p>
                        <p class="footer-link">Support</p>
                    </div>
                    <div>
                        <p class="footer-col-title">Legal</p>
                        <p class="footer-link">Privacy policy</p>
                        <p class="footer-link">Terms of service</p>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p class="footer-copyright">© 2026 BioMark. All rights reserved.</p>
                <div class="footer-socials">
                    <i class="ti ti-brand-github"></i>
                    <i class="ti ti-brand-linkedin"></i>
                    <i class="ti ti-brand-twitter"></i>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    


import datetime


def render_footer():
    """
    Renders the shared BioMark footer (CSS + markup in one call).
    Call this as the very last line of every page/screen function
    (student_screen, teacher_screen, student_dashboard, etc.)
    so it's consistent across the whole app.
    """
    year = datetime.datetime.now().year

    st.markdown(f"""
    <style>

    .biomark-footer {{
        margin-top: 48px;
        padding: 20px 0 16px 0;
        border-top: 1px solid rgba(255,255,255,0.06);
        text-align: center;
    }}

    .biomark-footer-brand {{
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 0.3px;
        color: rgba(255,255,255,0.45);
        margin-bottom: 4px;
    }}

    .biomark-footer-brand span {{
        background: linear-gradient(90deg, #4361EE, #00D4FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }}

    .biomark-footer-credit {{
        font-family: 'Inter', sans-serif;
        font-size: 11.5px;
        font-weight: 400;
        letter-spacing: 0.2px;
        color: rgba(255,255,255,0.28);
    }}

    .biomark-footer-credit span {{
        color: rgba(255,255,255,0.5);
        font-weight: 600;
    }}

    </style>

    <div class="biomark-footer">
        <div class="biomark-footer-brand">
            🧬 Bio<span>Mark</span> &nbsp;·&nbsp; Smart Attendance Management
        </div>
        <div class="biomark-footer-credit">
            © {year} BioMark. All rights reserved. &nbsp;·&nbsp; Designed by <span>Sonu Kumar Yadav</span>
        </div>
    </div>
    """, unsafe_allow_html=True)    