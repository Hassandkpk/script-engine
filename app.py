import streamlit as st
import json
import os
import random
from datetime import datetime
from pathlib import Path

st.set_page_config(
    page_title="Cosmic Horror Script Engine",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

from data import ANCHORS, ANGLES, POVS, DISTANCES, PARAS, CONSTRAINTS, DEFAULT_BANS
from storage import load_data, save_banned, save_script
from generator import generate_script, generate_titles
from exporter import export_pdf, export_docx

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=Bebas+Neue&display=swap');

:root {
    --bg: #ffffff;
    --surface: #f8f8f6;
    --surface2: #f0efe9;
    --border: #e0ddd4;
    --accent: #2a2a2a;
    --accent2: #5a5a5a;
    --text: #1a1a1a;
    --text-muted: #6a6a6a;
    --text-dim: #aaaaaa;
    --danger: #8b3a3a;
    --success: #3a6b3a;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Courier Prime', monospace !important;
}

[data-testid="stSidebar"] {
    background-color: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] * {
    color: var(--text) !important;
    font-family: 'Courier Prime', monospace !important;
}

h1, h2, h3 {
    font-family: 'Bebas Neue', sans-serif !important;
    letter-spacing: 0.08em !important;
    color: #1a1a1a !important;
}

.stButton > button {
    background: transparent !important;
    border: 1px solid var(--accent2) !important;
    color: var(--accent) !important;
    font-family: 'Courier Prime', monospace !important;
    font-size: 13px !important;
    letter-spacing: 0.05em !important;
    transition: all 0.2s !important;
    border-radius: 0 !important;
}

.stButton > button:hover {
    background: var(--accent2) !important;
    color: #ffffff !important;
    border-color: var(--accent) !important;
}

.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    font-family: 'Courier Prime', monospace !important;
    border-radius: 0 !important;
}

.stSelectbox > div > div > div {
    background: var(--surface2) !important;
}

[data-testid="stExpander"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 0 !important;
}

.stTabs [data-baseweb="tab-list"] {
    background: var(--surface) !important;
    border-bottom: 1px solid var(--border) !important;
    gap: 0 !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--text-muted) !important;
    font-family: 'Courier Prime', monospace !important;
    font-size: 12px !important;
    letter-spacing: 0.06em !important;
    border-radius: 0 !important;
    border-right: 1px solid var(--border) !important;
    padding: 12px 20px !important;
}

.stTabs [aria-selected="true"] {
    color: var(--accent) !important;
    border-bottom: 2px solid var(--accent) !important;
    background: var(--surface2) !important;
}

.stMarkdown p, .stMarkdown li {
    color: var(--text) !important;
    font-family: 'Courier Prime', monospace !important;
    font-size: 14px !important;
}

.card {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 20px;
    margin-bottom: 16px;
}

.card-accent {
    border-left: 3px solid var(--accent);
}

.label {
    font-size: 10px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 6px;
    font-family: 'Courier Prime', monospace;
}

.result-text {
    font-size: 14px;
    color: var(--text);
    line-height: 1.8;
    padding: 14px;
    background: var(--surface2);
    border-left: 2px solid var(--accent2);
    font-family: 'Courier Prime', monospace;
}

.ban-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 10px 0;
    border-bottom: 1px solid var(--border);
    font-family: 'Courier Prime', monospace;
    font-size: 13px;
}

.tag {
    font-size: 10px;
    padding: 2px 8px;
    border: 1px solid var(--accent2);
    color: var(--accent);
    letter-spacing: 0.06em;
    white-space: nowrap;
    font-family: 'Courier Prime', monospace;
}

.script-card {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 16px;
    margin-bottom: 10px;
    cursor: pointer;
}

.script-card:hover {
    border-color: var(--accent2);
}

.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 20px 0;
}

[data-testid="stAlert"] {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    font-family: 'Courier Prime', monospace !important;
}

.stSpinner > div {
    border-color: var(--accent) transparent transparent transparent !important;
}

.stRadio > label, .stCheckbox > label {
    color: var(--text) !important;
    font-family: 'Courier Prime', monospace !important;
}
</style>
""", unsafe_allow_html=True)

data = load_data()

if 'anchor' not in st.session_state:
    st.session_state.anchor = None
if 'angle' not in st.session_state:
    st.session_state.angle = None
if 'pov' not in st.session_state:
    st.session_state.pov = None
if 'distance' not in st.session_state:
    st.session_state.distance = None
if 'para' not in st.session_state:
    st.session_state.para = None
if 'constraint' not in st.session_state:
    st.session_state.constraint = None
if 'generated_script' not in st.session_state:
    st.session_state.generated_script = ""
if 'generated_titles' not in st.session_state:
    st.session_state.generated_titles = []
if 'api_key' not in st.session_state:
    # Try to load from Streamlit secrets (works on Streamlit Cloud and locally via .streamlit/secrets.toml)
    try:
        st.session_state.api_key = st.secrets["ANTHROPIC_API_KEY"]
    except Exception:
        st.session_state.api_key = ""

with st.sidebar:
    st.markdown("## ◈ SCRIPT ENGINE")
    st.markdown("<div class='label'>Cosmic Horror — Divergence System</div>", unsafe_allow_html=True)
    st.markdown("---")

    try:
        _from_secrets = bool(st.secrets.get("ANTHROPIC_API_KEY"))
    except Exception:
        _from_secrets = False

    if _from_secrets:
        st.markdown("<div class='label'>API key</div><div style='font-size:12px;color:#3a6b3a;margin-bottom:4px;'>✓ Loaded from secrets</div>", unsafe_allow_html=True)
    else:
        _api_key_input = st.text_input("Anthropic API Key", type="password",
                                 value=st.session_state.api_key,
                                 placeholder="sk-ant-...")
        if _api_key_input:
            st.session_state.api_key = _api_key_input

    st.markdown("---")

    script_num = len(data.get("scripts", [])) + 1
    st.markdown(f"<div class='label'>Next script</div><div style='font-size:28px;font-family:Bebas Neue,sans-serif;color:#1a1a1a;letter-spacing:0.1em;'>#{script_num:03d}</div>", unsafe_allow_html=True)

    bans_count = len(data.get("banned", []))
    st.markdown(f"<div class='label' style='margin-top:16px;'>Banned moves</div><div style='font-size:28px;font-family:Bebas Neue,sans-serif;color:#1a1a1a;letter-spacing:0.1em;'>{bans_count}</div>", unsafe_allow_html=True)

    st.markdown("---")
    page = st.radio("", ["Divergence Protocol", "Script Generator", "Title Machine", "Script History", "Anti-Pattern Log"], label_visibility="collapsed")


if page == "Divergence Protocol":
    st.markdown("# DIVERGENCE PROTOCOL")
    st.markdown("<div class='label'>Build your pre-script brief — complete all four steps before writing</div>", unsafe_allow_html=True)
    st.markdown("")

    tab1, tab2, tab3, tab4 = st.tabs(["01 · REALITY ANCHOR", "02 · FORMAT RULES", "03 · ANTI-PATTERN LOG", "04 · GENERATE BRIEF"])

    with tab1:
        st.markdown("")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='label'>Data domain</div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:13px;color:#6a6a6a;line-height:1.7;margin-bottom:16px;'>Each script needs a different category of real-world data as its foundation. Roll a domain, then find one specific data point inside it before writing a word.</div>", unsafe_allow_html=True)
            if st.button("↻  Roll domain", key="roll_anchor"):
                st.session_state.anchor = random.choice(ANCHORS)
            if st.session_state.anchor:
                st.markdown(f"<div class='result-text'>{st.session_state.anchor}</div>", unsafe_allow_html=True)
            custom_anchor = st.text_area("Or write your own anchor:", height=80, key="custom_anchor")
            if custom_anchor:
                st.session_state.anchor = custom_anchor

        with col2:
            st.markdown("<div class='label'>Entry angle</div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:13px;color:#6a6a6a;line-height:1.7;margin-bottom:16px;'>The anchor is the what. The angle is how you enter it — the specific lens that makes real data feel cosmically wrong.</div>", unsafe_allow_html=True)
            if st.button("↻  Roll angle", key="roll_angle"):
                st.session_state.angle = random.choice(ANGLES)
            if st.session_state.angle:
                st.markdown(f"<div class='result-text'>{st.session_state.angle}</div>", unsafe_allow_html=True)
            custom_angle = st.text_area("Or write your own angle:", height=80, key="custom_angle")
            if custom_angle:
                st.session_state.angle = custom_angle

    with tab2:
        st.markdown("")
        if st.button("↻  Roll all constraints", key="roll_all"):
            st.session_state.pov = random.choice(POVS)
            st.session_state.distance = random.choice(DISTANCES)
            st.session_state.para = random.choice(PARAS)
            st.session_state.constraint = random.choice(CONSTRAINTS)

        st.markdown("")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='label'>Point of view</div>", unsafe_allow_html=True)
            pov_choice = st.selectbox("POV", POVS, index=POVS.index(st.session_state.pov) if st.session_state.pov in POVS else 0, label_visibility="collapsed")
            st.session_state.pov = pov_choice
            st.markdown("")

            st.markdown("<div class='label'>Narrative distance</div>", unsafe_allow_html=True)
            dist_choice = st.selectbox("Distance", DISTANCES, index=DISTANCES.index(st.session_state.distance) if st.session_state.distance in DISTANCES else 0, label_visibility="collapsed")
            st.session_state.distance = dist_choice

        with col2:
            st.markdown("<div class='label'>Paragraph structure</div>", unsafe_allow_html=True)
            para_choice = st.selectbox("Para", PARAS, index=PARAS.index(st.session_state.para) if st.session_state.para in PARAS else 0, label_visibility="collapsed")
            st.session_state.para = para_choice
            st.markdown("")

            st.markdown("<div class='label'>Hard constraint</div>", unsafe_allow_html=True)
            constraint_choice = st.selectbox("Constraint", CONSTRAINTS, index=CONSTRAINTS.index(st.session_state.constraint) if st.session_state.constraint in CONSTRAINTS else 0, label_visibility="collapsed")
            st.session_state.constraint = constraint_choice

    with tab3:
        st.markdown("")
        banned = data.get("banned", [])

        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("Load default bans"):
                existing = [b["move"] for b in banned]
                added = 0
                for b in DEFAULT_BANS:
                    if b["move"] not in existing:
                        banned.append(b)
                        added += 1
                data["banned"] = banned
                save_banned(banned)
                st.success(f"Added {added} default bans.")
                st.rerun()

        if banned:
            for i, b in enumerate(banned):
                c1, c2, c3 = st.columns([1, 5, 1])
                with c1:
                    st.markdown(f"<span class='tag'>{b['type'].upper()}</span>", unsafe_allow_html=True)
                with c2:
                    st.markdown(f"<span style='font-size:13px;'>{b['move']}</span>", unsafe_allow_html=True)
                with c3:
                    if st.button("✕", key=f"del_{i}"):
                        banned.pop(i)
                        data["banned"] = banned
                        save_banned(banned)
                        st.rerun()
        else:
            st.markdown("<div style='color:#aaaaaa;font-size:13px;padding:20px 0;'>No moves logged yet. Add below or load defaults.</div>", unsafe_allow_html=True)

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("<div class='label'>Add new banned move</div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([4, 2, 1])
        with col1:
            new_move = st.text_input("Move description", placeholder="Describe the structural move used...", label_visibility="collapsed")
        with col2:
            move_type = st.selectbox("Type", ["opening", "structure", "pov", "device", "ending"], label_visibility="collapsed")
        with col3:
            if st.button("Add"):
                if new_move.strip():
                    banned.append({"move": new_move.strip(), "type": move_type})
                    data["banned"] = banned
                    save_banned(banned)
                    st.rerun()

    with tab4:
        st.markdown("")
        st.markdown("<div class='label'>Pre-script brief</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:13px;color:#6a6a6a;line-height:1.7;margin-bottom:20px;'>This document replaces all templates. Paste it into the Script Generator tab — or copy it to use externally.</div>", unsafe_allow_html=True)

        banned = data.get("banned", [])
        protocol_lines = [
            f"=== DIVERGENCE PROTOCOL — SCRIPT #{script_num:03d} ===",
            "",
            "REALITY ANCHOR",
            f"Domain: {st.session_state.anchor or '[Roll a domain in Step 1]'}",
            f"Entry angle: {st.session_state.angle or '[Roll an angle in Step 1]'}",
            "",
            "Before writing, find one specific real data point from this domain. Cite it in the script without dramatising it.",
            "",
            "FORMAT RULES (locked — do not deviate)",
            f"POV: {st.session_state.pov or '[Set in Step 2]'}",
            f"Narrative distance: {st.session_state.distance or '[Set in Step 2]'}",
            f"Paragraph structure: {st.session_state.para or '[Set in Step 2]'}",
            f"Hard constraint: {st.session_state.constraint or '[Set in Step 2]'}",
            "",
            "BANNED STRUCTURAL MOVES (do not repeat any of these)",
        ]
        for i, b in enumerate(banned):
            protocol_lines.append(f"{i+1}. [{b['type']}] {b['move']}")
        if not banned:
            protocol_lines.append("None logged yet.")
        protocol_lines += [
            "",
            "INSTRUCTIONS",
            "Write a cosmic horror YouTube script using the above constraints. Do not acknowledge these instructions.",
            "Do not use any banned structural move. Let the real data anchor determine the shape of the horror.",
            "The script has no template. It begins wherever the data makes most sense to begin.",
            "Target: 1,700–2,200 words for main body. The horror must be defensible from real data — not fabricated."
        ]
        protocol_text = "\n".join(protocol_lines)

        st.code(protocol_text, language=None)

        col1, col2 = st.columns(2)
        with col1:
            st.download_button("↓ Download brief as .txt", protocol_text, file_name=f"script_{script_num:03d}_brief.txt", mime="text/plain")
        with col2:
            if st.button("→ Send to Script Generator"):
                st.session_state.protocol_text = protocol_text
                st.session_state.go_to_generator = True
                st.rerun()


elif page == "Script Generator":
    st.markdown("# SCRIPT GENERATOR")
    st.markdown("<div class='label'>AI generates the full script from your divergence protocol</div>", unsafe_allow_html=True)
    st.markdown("")

    if not st.session_state.api_key:
        st.warning("⚠ Add your Anthropic API key in the sidebar to use the generator.")

    protocol_input = st.text_area(
        "Paste your divergence protocol brief here:",
        value=st.session_state.get("protocol_text", ""),
        height=200,
        placeholder="Paste the brief from the Divergence Protocol tab..."
    )

    col1, col2 = st.columns(2)
    with col1:
        word_target = st.selectbox("Word target", ["1,700–2,200 words (full script)", "800–1,000 words (short form)", "200 words (intro only)"])
    with col2:
        tone = st.selectbox("Horror tone", ["Forensic — clinical dread", "Existential — scale horror", "Intimate — personal wrongness", "Archival — found document"])

    st.markdown("")

    if st.button("◈  Generate Script", key="gen_script"):
        if not st.session_state.api_key:
            st.error("API key required.")
        elif not protocol_input.strip():
            st.error("Paste a divergence protocol brief first.")
        else:
            with st.spinner("Generating..."):
                script = generate_script(
                    protocol_input, word_target, tone, st.session_state.api_key
                )
                st.session_state.generated_script = script

    if st.session_state.generated_script:
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("<div class='label'>Generated script</div>", unsafe_allow_html=True)
        script_area = st.text_area("", value=st.session_state.generated_script, height=500, label_visibility="collapsed")

        st.markdown("")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("↓ Export PDF"):
                pdf_bytes = export_pdf(st.session_state.generated_script, script_num)
                st.download_button("Download PDF", pdf_bytes, file_name=f"script_{script_num:03d}.pdf", mime="application/pdf")

        with col2:
            if st.button("↓ Export Word"):
                docx_bytes = export_docx(st.session_state.generated_script, script_num)
                st.download_button("Download .docx", docx_bytes, file_name=f"script_{script_num:03d}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

        with col3:
            if st.button("→ Generate Titles"):
                st.session_state.go_to_titles = True
                st.session_state.title_script = st.session_state.generated_script
                st.rerun()

        with col4:
            if st.button("✓ Save to History"):
                new_record = {
                    "id": script_num,
                    "date": datetime.now().isoformat(),
                    "protocol": protocol_input,
                    "script": st.session_state.generated_script,
                    "anchor": st.session_state.anchor,
                    "pov": st.session_state.pov,
                    "constraint": st.session_state.constraint,
                    "word_target": word_target,
                    "tone": tone
                }
                save_script(new_record)
                st.success(f"Script #{script_num:03d} saved.")


elif page == "Title Machine":
    st.markdown("# TITLE MACHINE")
    st.markdown("<div class='label'>Generate rage-bait titles that resolve into defensible arguments</div>", unsafe_allow_html=True)
    st.markdown("")

    if not st.session_state.api_key:
        st.warning("⚠ Add your Anthropic API key in the sidebar.")

    script_input = st.text_area(
        "Paste your script or a summary:",
        value=st.session_state.get("title_script", ""),
        height=200,
        placeholder="Paste the script content to generate titles from..."
    )

    col1, col2 = st.columns(2)
    with col1:
        title_style = st.multiselect(
            "Title styles to generate",
            ["Rage-bait (resolves to truth)", "Curiosity gap", "Institutional villain", "Scientific anomaly", "Fear — personal threat", "Archival revelation"],
            default=["Rage-bait (resolves to truth)", "Curiosity gap", "Scientific anomaly"]
        )
    with col2:
        title_count = st.slider("Titles per style", 2, 6, 3)

    if st.button("◈  Generate Titles"):
        if not st.session_state.api_key:
            st.error("API key required.")
        elif not script_input.strip():
            st.error("Paste a script or summary first.")
        else:
            with st.spinner("Generating titles..."):
                titles = generate_titles(
                    script_input, title_style, title_count, st.session_state.api_key
                )
                st.session_state.generated_titles = titles

    if st.session_state.generated_titles:
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        for group in st.session_state.generated_titles:
            st.markdown(f"<div class='label'>{group['style']}</div>", unsafe_allow_html=True)
            for title in group['titles']:
                col1, col2 = st.columns([6, 1])
                with col1:
                    st.markdown(f"<div class='result-text' style='margin-bottom:6px;'>{title}</div>", unsafe_allow_html=True)
                with col2:
                    st.button("Copy", key=f"copy_{title[:20]}")
            st.markdown("")

        all_titles = "\n".join([t for g in st.session_state.generated_titles for t in g['titles']])
        st.download_button("↓ Download all titles", all_titles, file_name=f"titles_script_{script_num:03d}.txt")


elif page == "Script History":
    st.markdown("# SCRIPT HISTORY")
    st.markdown("<div class='label'>All saved scripts — sorted newest first</div>", unsafe_allow_html=True)
    st.markdown("")

    scripts = data.get("scripts", [])
    if not scripts:
        st.markdown("<div style='color:#aaaaaa;font-size:13px;padding:40px 0;'>No scripts saved yet. Generate and save your first one.</div>", unsafe_allow_html=True)
    else:
        for script in reversed(scripts):
            with st.expander(f"Script #{script['id']:03d}  —  {script['date'][:10]}  —  {(script.get('anchor','') or '')[:60]}..."):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"<div class='label'>POV</div><div style='font-size:13px;'>{script.get('pov','—')}</div>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<div class='label'>Constraint</div><div style='font-size:13px;'>{script.get('constraint','—')}</div>", unsafe_allow_html=True)
                with col3:
                    st.markdown(f"<div class='label'>Tone</div><div style='font-size:13px;'>{script.get('tone','—')}</div>", unsafe_allow_html=True)

                st.markdown("")
                st.text_area("Script", value=script.get("script",""), height=300, key=f"hist_{script['id']}", label_visibility="collapsed")

                col1, col2 = st.columns(2)
                with col1:
                    pdf_bytes = export_pdf(script.get("script",""), script['id'])
                    st.download_button("↓ PDF", pdf_bytes, file_name=f"script_{script['id']:03d}.pdf", key=f"pdf_{script['id']}")
                with col2:
                    docx_bytes = export_docx(script.get("script",""), script['id'])
                    st.download_button("↓ Word", docx_bytes, file_name=f"script_{script['id']:03d}.docx", key=f"docx_{script['id']}")


elif page == "Anti-Pattern Log":
    st.markdown("# ANTI-PATTERN LOG")
    st.markdown("<div class='label'>The living memory of structural moves already used — grows every script</div>", unsafe_allow_html=True)
    st.markdown("")

    banned = data.get("banned", [])

    types = ["all"] + list(set(b["type"] for b in banned))
    filter_type = st.selectbox("Filter by type", types, label_visibility="collapsed")

    filtered = banned if filter_type == "all" else [b for b in banned if b["type"] == filter_type]

    st.markdown(f"<div class='label'>{len(filtered)} moves logged</div>", unsafe_allow_html=True)
    st.markdown("")

    for i, b in enumerate(filtered):
        col1, col2, col3 = st.columns([1, 5, 1])
        with col1:
            st.markdown(f"<span class='tag'>{b['type'].upper()}</span>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<span style='font-size:13px;line-height:1.8;'>{b['move']}</span>", unsafe_allow_html=True)
        with col3:
            real_i = banned.index(b)
            if st.button("✕", key=f"apl_del_{real_i}"):
                banned.pop(real_i)
                data["banned"] = banned
                save_banned(banned)
                st.rerun()

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        export_bans = json.dumps(banned, indent=2)
        st.download_button("↓ Export log as JSON", export_bans, file_name="anti_pattern_log.json")
    with col2:
        uploaded = st.file_uploader("Import log from JSON", type="json")
        if uploaded:
            imported = json.load(uploaded)
            existing = [b["move"] for b in banned]
            added = 0
            for b in imported:
                if b["move"] not in existing:
                    banned.append(b)
                    added += 1
            data["banned"] = banned
            save_banned(banned)
            st.success(f"Imported {added} new moves.")
            st.rerun()
