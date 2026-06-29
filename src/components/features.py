import streamlit as st

def feature_highlights():
    
    st.markdown(
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/dist/tabler-icons.min.css">',
        unsafe_allow_html=True
    )
    st.markdown('<div style="margin-bottom: 4rem;"></div>', unsafe_allow_html=True)

    st.markdown("""
        <style>
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 16px;
            margin: 0 0 1.5rem;
        }
        .feature-card {
            background: rgba(255,255,255,0.04);
            border-radius: 14px;
            padding: 1.5rem 1.25rem;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.08);
            transition: transform 0.2s ease, background 0.2s ease, border-color 0.2s ease;
        }
        .feature-card:hover {
            transform: translateY(-4px);
            background: rgba(255,255,255,0.07);
            border-color: rgba(0,212,255,0.3);
        }
        .feature-card .icon-wrap {
            width: 48px;
            height: 48px;
            margin: 0 auto 12px;
            border-radius: 12px;
            background: linear-gradient(135deg, #4361EE 0%, #00D4FF 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(67,97,238,0.3);
        }
        .feature-card .icon-wrap i {
            font-size: 22px;
            color: #fff;
        }
        .feature-card p.title {
            margin: 0;
            font-size: 15px;
            font-weight: 600;
            color: #fff;
        }
        .feature-card p.desc {
            margin: 6px 0 0;
            font-size: 12.5px;
            font-weight: 400;
            color: rgba(255,255,255,0.6);
            line-height: 1.4;
        }
        .biomark-section-title {
            font-size: 26px;
            font-weight: 700;
            color: #fff;
            text-align: center;
            margin: 5rem 0 1.5rem;
            letter-spacing: 0.3px;
        }
        .biomark-section-sub {
            font-size: 13.5px;
            color: rgba(255,255,255,0.45);
            text-align: center;
            margin: 0 0 2rem;
        }
        </style>
        
        <h2 class="biomark-section-title">Why choose BioMark</h2>
        <p class="biomark-section-sub">Built for modern classrooms — fast, secure, and effortlessly accurate</p>
        <div class="feature-grid">
            <div class="feature-card">
                <div class="icon-wrap"><i class="ti ti-face-id"></i></div>
                <p class="title">Face recognition</p>
                <p class="desc">Mark attendance instantly with secure facial scans</p>
            </div>
            <div class="feature-card">
                <div class="icon-wrap"><i class="ti ti-microphone"></i></div>
                <p class="title">Voice recognition</p>
                <p class="desc">Verify identity through real-time voice authentication</p>
            </div>
            <div class="feature-card">
                <div class="icon-wrap"><i class="ti ti-chart-bar"></i></div>
                <p class="title">Real-time analytics</p>
                <p class="desc">Track attendance trends with live dashboards</p>
            </div>
            <div class="feature-card">
                <div class="icon-wrap"><i class="ti ti-shield-check"></i></div>
                <p class="title">Secure & accurate</p>
                <p class="desc">AI-driven accuracy with end-to-end data protection</p>
            </div>
        </div>
        
    """, unsafe_allow_html=True)