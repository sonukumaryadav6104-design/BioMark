import streamlit.components.v1 as components


def subject_card(name, code, section, stats=None):

    stats_html = ""

    if stats:
        stats_html += """
        <div style="display:flex;gap:12px;margin-top:8px;">
        """
        for icon, label, value in stats:
            stats_html += f"""
            <div style="
                flex:1;
                background:white;
                border-radius:16px;
                padding:18px 10px;
                text-align:center;
                border:1px solid #eef2ff;
                box-shadow:0 4px 12px rgba(0,0,0,.04);
            ">
                <div style="font-size:1.5rem;margin-bottom:8px;">{icon}</div>
                <div style="font-size:1.4rem;font-weight:800;color:#0f172a;">{value}</div>
                <div style="font-size:0.78rem;color:#64748b;margin-top:4px;">{label}</div>
            </div>
            """
        stats_html += "</div>"

    html = f"""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <style>
    body {{ margin:0; padding:0; }}
    .subject-card {{ transition:all .3s ease; }}
    .subject-card:hover {{
        transform:translateY(-5px);
        box-shadow:0 20px 40px rgba(0,0,0,.12), 0 10px 20px rgba(37,99,235,.08);
    }}
    </style>

    <div style="padding:4px;font-family:'Inter',sans-serif;">
        <div class="subject-card" style="
            background:rgba(255,255,255,0.95);
            backdrop-filter:blur(14px);
            border-radius:22px;
            border:1px solid rgba(255,255,255,0.4);
            box-shadow:0 15px 35px rgba(0,0,0,.08), 0 4px 12px rgba(0,0,0,.05);
            padding:24px;
            position:relative;
            overflow:hidden;
        ">
            <!-- Blue Glow -->
            <div style="
                position:absolute;top:-60px;right:-60px;
                width:220px;height:220px;
                background:radial-gradient(circle, rgba(37,99,235,.18), transparent 70%);
                border-radius:50%;pointer-events:none;
            "></div>

            <!-- Pink Glow -->
            <div style="
                position:absolute;bottom:-60px;left:-60px;
                width:220px;height:220px;
                background:radial-gradient(circle, rgba(235,69,158,.12), transparent 70%);
                border-radius:50%;pointer-events:none;
            "></div>

            <div style="
                display:flex;justify-content:space-between;
                align-items:flex-start;position:relative;z-index:2;
            ">
                <div>
                    <div style="
                        font-size:1.35rem;font-weight:800;
                        background:linear-gradient(135deg,#0ea5e9,#2563eb,#EB459E);
                        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                        margin-bottom:8px;
                    ">{name}</div>
                    <div style="display:flex;gap:16px;align-items:center;color:#64748b;font-size:0.85rem;">
                        <span>🔖 {code}</span>
                        <span>📚 Section {section}</span>
                    </div>
                </div>
                <span style="
                    font-size:0.72rem;font-weight:700;color:#10b981;
                    background:rgba(16,185,129,.12);border:1px solid rgba(16,185,129,.25);
                    padding:6px 12px;border-radius:999px;white-space:nowrap;
                ">● Active</span>
            </div>

            <div style="border-top:1px solid #e5e7eb;margin:18px 0;"></div>

            {stats_html}

            <div style="display:flex;justify-content:space-between;align-items:center;margin-top:18px;">
                <span style="font-size:0.78rem;color:#64748b;">Last updated · Today</span>
                <button
                    onclick="window.parent.postMessage('{code}__share', '*')"
                    style="
                        background:linear-gradient(135deg,#FFB347,#FF7A18);
                        color:white;border:none;border-radius:12px;
                        padding:10px 20px;font-size:0.85rem;font-weight:700;
                        cursor:pointer;
                        box-shadow:0 8px 20px rgba(255,122,24,.35), 0 0 20px rgba(255,122,24,.15);
                    "
                >🔗 Share</button>
            </div>
        </div>
    </div>
    """

    # ✅ Fix: accurate height based on stat count
    height = 220 + (len(stats) * 50 if stats else 0)

    components.html(html, height=height, scrolling=False)