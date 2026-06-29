import streamlit as st
def how_it_works():
    st.markdown(
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/dist/tabler-icons.min.css">',
        unsafe_allow_html=True
    )

    st.markdown("""
    <style>
    .hiw-title {
        font-size: 26px;
        font-weight: 700;
        color: #fff;
        text-align: center;
        margin: 4rem 0 0.4rem;
        letter-spacing: 0.3px;
    }
    .hiw-sub {
        font-size: 13.5px;
        color: rgba(255,255,255,0.45);
        text-align: center;
        margin: 0 0 2.5rem;
    }
    .steps-wrapper {
        position: relative;
        max-width: 680px;
        margin: 0 auto;
    }
    .steps-connector {
        position: absolute;
        top: 22px;
        left: calc(12.5% + 22px);
        right: calc(12.5% + 22px);
        height: 2px;
        background: linear-gradient(90deg, #4361EE, #00D4FF);
        opacity: 0.25;
        border-radius: 2px;
    }
    .steps-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0;
    }
    .step-item {
        text-align: center;
        padding: 0 0.75rem 1rem;
    }
    .step-num {
        width: 44px; height: 44px;
        margin: 0 auto 12px;
        border-radius: 50%;
        background: linear-gradient(135deg, #4361EE 0%, #00D4FF 100%);
        display: flex; align-items: center; justify-content: center;
        font-size: 16px; font-weight: 700; color: #fff;
        position: relative; z-index: 1;
    }
    .step-title {
        font-size: 14px; font-weight: 600;
        color: #fff; margin: 0 0 5px;
    }
    .step-desc {
        font-size: 12px;
        color: rgba(255,255,255,0.5);
        line-height: 1.45;
    }
    </style>

    <h2 class="hiw-title">How it works</h2>
    <p class="hiw-sub">Four steps from classroom to confirmed attendance</p>

    <div class="steps-wrapper">
        <div class="steps-connector"></div>
        <div class="steps-grid">
            <div class="step-item">
                <div class="step-num">1</div>
                <div class="step-title">Login</div>
                <div class="step-desc">Authenticate via student or teacher portal</div>
            </div>
            <div class="step-item">
                <div class="step-num">2</div>
                <div class="step-title">Scan face</div>
                <div class="step-desc">Camera captures and verifies facial identity</div>
            </div>
            <div class="step-item">
                <div class="step-num">3</div>
                <div class="step-title">Voice check</div>
                <div class="step-desc">Voice pattern adds a second factor</div>
            </div>
            <div class="step-item">
                <div class="step-num">4</div>
                <div class="step-title">Confirmed</div>
                <div class="step-desc">Attendance logged instantly to Supabase</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)