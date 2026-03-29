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
from storage import load_data, save_banned, save_script, load_recent_fingerprints
from generator import generate_script, generate_titles, generate_protocol_from_title, build_protocol_text, generate_section
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
if 'simple_protocol' not in st.session_state:
    st.session_state.simple_protocol = None
if 'simple_script' not in st.session_state:
    st.session_state.simple_script = ""
if 'simple_title' not in st.session_state:
    st.session_state.simple_title = ""
if 'mode' not in st.session_state:
    st.session_state.mode = "Simple"
if 'full_title' not in st.session_state:
    st.session_state.full_title = ""
if 'full_anchor' not in st.session_state:
    st.session_state.full_anchor = ""
if 'full_angle' not in st.session_state:
    st.session_state.full_angle = ""
if 'full_pov' not in st.session_state:
    st.session_state.full_pov = ""
if 'full_distance' not in st.session_state:
    st.session_state.full_distance = ""
if 'full_para' not in st.session_state:
    st.session_state.full_para = ""
if 'full_constraint' not in st.session_state:
    st.session_state.full_constraint = ""
if 'full_reasoning' not in st.session_state:
    st.session_state.full_reasoning = ""
if 'full_generated_script' not in st.session_state:
    st.session_state.full_generated_script = ""
if 'full_suggested' not in st.session_state:
    st.session_state.full_suggested = None
if 'full_output_mode' not in st.session_state:
    st.session_state.full_output_mode = "Full script by sections"
if 'full_sections' not in st.session_state:
    st.session_state.full_sections = []        # list of approved section texts
if 'full_section_pending' not in st.session_state:
    st.session_state.full_section_pending = "" # current unapproved section
if 'full_protocol_locked' not in st.session_state:
    st.session_state.full_protocol_locked = False
if 'full_protocol_text' not in st.session_state:
    st.session_state.full_protocol_text = ""
if 'full_section_num' not in st.session_state:
    st.session_state.full_section_num = 1
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

    mode = st.radio("Mode", ["Simple", "Full"], index=0 if st.session_state.mode == "Simple" else 1, horizontal=True)
    st.session_state.mode = mode

    st.markdown("---")

    script_num = len(data.get("scripts", [])) + 1
    st.markdown(f"<div class='label'>Next script</div><div style='font-size:28px;font-family:Bebas Neue,sans-serif;color:#1a1a1a;letter-spacing:0.1em;'>#{script_num:03d}</div>", unsafe_allow_html=True)

    bans_count = len(data.get("banned", []))
    st.markdown(f"<div class='label' style='margin-top:16px;'>Banned moves</div><div style='font-size:28px;font-family:Bebas Neue,sans-serif;color:#1a1a1a;letter-spacing:0.1em;'>{bans_count}</div>", unsafe_allow_html=True)

    st.markdown("---")

    if st.session_state.mode == "Simple":
        page = st.radio("", ["Quick Generate", "Script History"], label_visibility="collapsed")
    else:
        page = st.radio("", ["Divergence Protocol", "Script Generator", "Title Machine", "Script History", "Anti-Pattern Log"], label_visibility="collapsed")


if page == "Quick Generate":
    st.markdown("# QUICK GENERATE")
    st.markdown("<div class='label'>Paste a title — the system does the rest</div>", unsafe_allow_html=True)
    st.markdown("")

    if not st.session_state.api_key:
        st.warning("⚠ Add your Anthropic API key in the sidebar.")

    title_input = st.text_input(
        "Video title",
        placeholder="e.g. The Hidden HIERARCHY of Lovecraft's Gods (Who Really Controls Everything)",
        label_visibility="collapsed"
    )

    col1, col2 = st.columns(2)
    with col1:
        word_target = st.selectbox("Length", [
            "1,700–2,200 words (full script)",
            "800–1,000 words (short form)",
            "200 words (intro only)"
        ])
    with col2:
        tone = st.selectbox("Tone", [
            "Existential — scale horror",
            "Forensic — clinical dread",
            "Intimate — personal wrongness",
            "Archival — found document"
        ])

    st.markdown("")

    if st.button("◈  Generate Script", key="simple_gen"):
        if not st.session_state.api_key:
            st.error("API key required.")
        elif not title_input.strip():
            st.error("Paste a video title first.")
        else:
            banned = data.get("banned", [])

            with st.spinner("Building protocol from title..."):
                fingerprints = load_recent_fingerprints(15)
                protocol = generate_protocol_from_title(
                    title_input.strip(), banned, st.session_state.api_key,
                    recent_fingerprints=fingerprints
                )
                st.session_state.simple_protocol = protocol
                st.session_state.simple_title = title_input.strip()

            protocol_text = build_protocol_text(
                title_input.strip(), script_num, protocol, banned
            )

            with st.spinner("Writing script — pass 1 of 2..."):
                script = generate_script(
                    protocol_text, word_target, tone, st.session_state.api_key,
                    title=title_input.strip()
                )
                st.session_state.simple_script = script

            # Auto-save to history
            new_record = {
                "id": script_num,
                "date": datetime.now().isoformat(),
                "protocol": protocol_text,
                "script": script,
                "anchor": protocol.get("anchor", ""),
                "pov": protocol.get("pov", ""),
                "constraint": protocol.get("constraint", ""),
                "word_target": word_target,
                "tone": tone,
            }
            save_script(new_record)
            st.rerun()

    if st.session_state.simple_script:
        st.markdown("<hr style='border:none;border-top:1px solid #e0ddd4;margin:24px 0;'>", unsafe_allow_html=True)

        # Show what the system auto-selected
        if st.session_state.simple_protocol:
            p = st.session_state.simple_protocol
            with st.expander("◈ View auto-generated protocol (what ran behind the scenes)"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"<div class='label'>Reality anchor</div><div style='font-size:13px;line-height:1.7;margin-bottom:16px;'>{p.get('anchor','')}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='label'>Entry angle</div><div style='font-size:13px;line-height:1.7;margin-bottom:16px;'>{p.get('angle','')}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='label'>Why this anchor</div><div style='font-size:13px;line-height:1.7;color:#6a6a6a;'>{p.get('reasoning','')}</div>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<div class='label'>POV</div><div style='font-size:13px;margin-bottom:12px;'>{p.get('pov','')}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='label'>Distance</div><div style='font-size:13px;margin-bottom:12px;'>{p.get('distance','')}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='label'>Structure</div><div style='font-size:13px;margin-bottom:12px;'>{p.get('para','')}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='label'>Hard constraint</div><div style='font-size:13px;'>{p.get('constraint','')}</div>", unsafe_allow_html=True)

        st.markdown(f"<div class='label'>Generated script — auto-saved as #{script_num-1:03d}</div>", unsafe_allow_html=True)
        st.text_area("", value=st.session_state.simple_script, height=500, label_visibility="collapsed", key="simple_script_area")

        st.markdown("")
        col1, col2, col3 = st.columns(3)
        with col1:
            pdf_bytes = export_pdf(st.session_state.simple_script, script_num - 1)
            st.download_button("↓ Export PDF", pdf_bytes, file_name=f"script_{script_num-1:03d}.pdf", mime="application/pdf")
        with col2:
            docx_bytes = export_docx(st.session_state.simple_script, script_num - 1)
            st.download_button("↓ Export Word", docx_bytes, file_name=f"script_{script_num-1:03d}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        with col3:
            if st.button("→ Generate Titles"):
                st.session_state.go_to_titles = True
                st.session_state.title_script = st.session_state.simple_script
                st.session_state.mode = "Full"
                st.rerun()


elif page == "Divergence Protocol":
    st.markdown("# SCRIPT BUILDER")
    st.markdown("<div class='label'>Title-first guided flow — review and override before generating</div>", unsafe_allow_html=True)
    st.markdown("")

    if not st.session_state.api_key:
        st.warning("⚠ Add your Anthropic API key in the sidebar.")

    # Step 1 — Title
    st.markdown("<div class='label'>Step 1 — Video title</div>", unsafe_allow_html=True)
    full_title = st.text_input(
        "Title",
        value=st.session_state.get("full_title", ""),
        placeholder="e.g. The Hidden HIERARCHY of Lovecraft's Gods (Who Really Controls Everything)",
        label_visibility="collapsed"
    )
    if full_title:
        st.session_state.full_title = full_title

    st.markdown("")

    if st.button("◈  Analyse title and suggest protocol", key="analyse_title"):
        if not st.session_state.api_key:
            st.error("API key required.")
        elif not full_title.strip():
            st.error("Enter a title first.")
        else:
            banned = data.get("banned", [])
            with st.spinner("Analysing title and building suggestions..."):
                fingerprints = load_recent_fingerprints(15)
                suggested = generate_protocol_from_title(
                    full_title.strip(), banned, st.session_state.api_key,
                    recent_fingerprints=fingerprints
                )
                st.session_state.full_suggested = suggested
                st.session_state.full_anchor = suggested.get("anchor", "")
                st.session_state.full_angle = suggested.get("angle", "")
                st.session_state.full_pov = suggested.get("pov", "")
                st.session_state.full_distance = suggested.get("distance", "")
                st.session_state.full_para = suggested.get("para", "")
                st.session_state.full_constraint = suggested.get("constraint", "")
                st.session_state.full_reasoning = suggested.get("reasoning", "")

    # Show suggestions if available
    if st.session_state.get("full_anchor"):
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("<div class='label'>Step 2 — Review and override suggestions</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:13px;color:#6a6a6a;margin-bottom:20px;'>The tool analysed your title and pre-filled everything below. Change anything before generating — or accept as is.</div>", unsafe_allow_html=True)

        # Reasoning
        if st.session_state.get("full_reasoning"):
            st.markdown(f"<div style='font-size:12px;color:#6a6a6a;font-style:italic;margin-bottom:20px;padding:10px;background:#f8f8f6;border-left:2px solid #e0ddd4;'>◈ Why this anchor was chosen: {st.session_state.full_reasoning}</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='label'>Reality anchor</div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#6a6a6a;margin-bottom:8px;'>The real-world data this script is grounded in. Must produce immediate dread — no explanation needed.</div>", unsafe_allow_html=True)
            full_anchor = st.text_area("Anchor", value=st.session_state.full_anchor, height=100, label_visibility="collapsed", key="ta_anchor")
            st.session_state.full_anchor = full_anchor

            st.markdown("")
            st.markdown("<div class='label'>Entry angle</div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#6a6a6a;margin-bottom:8px;'>The specific lens that makes this data feel cosmically wrong.</div>", unsafe_allow_html=True)
            full_angle = st.text_area("Angle", value=st.session_state.full_angle, height=100, label_visibility="collapsed", key="ta_angle")
            st.session_state.full_angle = full_angle

            st.markdown("")
            st.markdown("<div class='label'>Hard constraint</div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#6a6a6a;margin-bottom:8px;'>One banned device or forced structural rule for this script only.</div>", unsafe_allow_html=True)
            full_constraint = st.text_area("Constraint", value=st.session_state.full_constraint, height=80, label_visibility="collapsed", key="ta_constraint")
            st.session_state.full_constraint = full_constraint

        with col2:
            st.markdown("<div class='label'>Point of view</div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#6a6a6a;margin-bottom:8px;'>Who is narrating and how.</div>", unsafe_allow_html=True)
            full_pov = st.text_area("POV", value=st.session_state.full_pov, height=80, label_visibility="collapsed", key="ta_pov")
            st.session_state.full_pov = full_pov

            st.markdown("")
            st.markdown("<div class='label'>Narrative distance</div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#6a6a6a;margin-bottom:8px;'>How close the narrator is to the subject.</div>", unsafe_allow_html=True)
            full_distance = st.text_area("Distance", value=st.session_state.full_distance, height=80, label_visibility="collapsed", key="ta_distance")
            st.session_state.full_distance = full_distance

            st.markdown("")
            st.markdown("<div class='label'>Paragraph structure</div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#6a6a6a;margin-bottom:8px;'>How paragraphs are shaped across the script.</div>", unsafe_allow_html=True)
            full_para = st.text_area("Para", value=st.session_state.full_para, height=80, label_visibility="collapsed", key="ta_para")
            st.session_state.full_para = full_para

            st.markdown("")

        # Output mode selector
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("<div class='label'>Step 3 — Output mode & tone</div>", unsafe_allow_html=True)
        output_mode = st.selectbox("Output mode", [
            "Intro only (200 words) — approve then stop or continue",
            "Short script (1,000 words) — single pass",
            "Full script at once (1,700–2,200 words)",
            "Full script by sections (1,000 words each, approve before next)",
        ], label_visibility="collapsed", key="output_mode_select")
        st.session_state.full_output_mode = output_mode

        full_tone = st.selectbox("Horror tone", [
            "Existential — scale horror",
            "Forensic — clinical dread",
            "Intimate — personal wrongness",
            "Archival — found document"
        ], label_visibility="collapsed", key="full_tone")

        # Ban list preview
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        banned = data.get("banned", [])
        st.markdown(f"<div class='label'>Active ban list — {len(banned)} moves</div>", unsafe_allow_html=True)
        if banned:
            ban_preview = " · ".join([f"<span class='tag'>{b['type'].upper()}</span> {b['move']}" for b in banned[:5]])
            if len(banned) > 5:
                ban_preview += f" <span style='color:#aaaaaa;font-size:12px;'>+{len(banned)-5} more (see Anti-Pattern Log)</span>"
            st.markdown(f"<div style='font-size:12px;color:#6a6a6a;line-height:2;'>{ban_preview}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='font-size:12px;color:#aaaaaa;'>No bans yet. Go to Anti-Pattern Log to add them.</div>", unsafe_allow_html=True)

        st.markdown("")

        # --- GENERATE BUTTON ---
        if not st.session_state.full_protocol_locked:
            if st.button("◈  Lock protocol and start generating", key="full_gen"):
                if not st.session_state.api_key:
                    st.error("API key required.")
                elif not st.session_state.full_anchor.strip():
                    st.error("Anchor is required — analyse a title first.")
                else:
                    protocol = {
                        "anchor": st.session_state.full_anchor,
                        "angle": st.session_state.full_angle,
                        "pov": st.session_state.full_pov,
                        "distance": st.session_state.full_distance,
                        "para": st.session_state.full_para,
                        "constraint": st.session_state.full_constraint,
                    }
                    protocol_text = build_protocol_text(
                        full_title.strip(), script_num, protocol, banned
                    )
                    st.session_state.full_protocol_text = protocol_text
                    st.session_state.full_protocol_locked = True
                    st.session_state.full_sections = []
                    st.session_state.full_section_pending = ""
                    st.session_state.full_section_num = 1
                    st.session_state.full_generated_script = ""

                    # For non-sectioned modes generate immediately
                    mode_sel = st.session_state.full_output_mode
                    if "sections" not in mode_sel:
                        word_map = {
                            "Intro only (200 words) — approve then stop or continue": "200 words (intro only)",
                            "Short script (1,000 words) — single pass": "800–1,000 words (short form)",
                            "Full script at once (1,700–2,200 words)": "1,700–2,200 words (full script)",
                        }
                        wt = word_map.get(mode_sel, "1,700–2,200 words (full script)")
                        with st.spinner("Writing script — pass 1 of 2..."):
                            try:
                                script = generate_script(
                                    protocol_text, wt, full_tone,
                                    st.session_state.api_key, title=full_title.strip()
                                )
                                st.session_state.full_generated_script = script
                            except Exception as e:
                                st.error(f"Generation failed: {str(e)}")
                                st.session_state.full_protocol_locked = False
                    else:
                        # Section mode — generate section 1 immediately
                        with st.spinner("Writing section 1 of ~14 — pass 1 of 2..."):
                            try:
                                section = generate_section(
                                    protocol_text, full_title.strip(), 1, [],
                                    st.session_state.api_key
                                )
                                st.session_state.full_section_pending = section
                            except Exception as e:
                                st.error(f"Generation failed: {str(e)}")
                                st.session_state.full_protocol_locked = False
                    st.rerun()

        # --- PROTOCOL LOCKED STATE ---
        if st.session_state.full_protocol_locked:
            st.markdown("<hr class='divider'>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:12px;color:#3a6b3a;margin-bottom:16px;'>✓ Protocol locked — all sections use the same brief</div>", unsafe_allow_html=True)

            mode_sel = st.session_state.full_output_mode

            # NON-SECTIONED OUTPUT
            if "sections" not in mode_sel and st.session_state.full_generated_script:
                st.markdown("<div class='label'>Generated script</div>", unsafe_allow_html=True)
                st.text_area("", value=st.session_state.full_generated_script, height=500,
                             label_visibility="collapsed", key="full_script_display")
                st.markdown("")
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    pdf_bytes = export_pdf(st.session_state.full_generated_script, script_num)
                    st.download_button("↓ PDF", pdf_bytes, file_name=f"script_{script_num:03d}.pdf",
                                       mime="application/pdf", key="full_pdf")
                with col2:
                    docx_bytes = export_docx(st.session_state.full_generated_script, script_num)
                    st.download_button("↓ Word", docx_bytes, file_name=f"script_{script_num:03d}.docx",
                                       mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                                       key="full_docx")
                with col3:
                    if st.button("→ Titles", key="full_to_titles"):
                        st.session_state.title_script = st.session_state.full_generated_script
                        st.rerun()
                with col4:
                    if st.button("✕ Reset", key="full_reset"):
                        st.session_state.full_protocol_locked = False
                        st.session_state.full_generated_script = ""
                        st.rerun()

            # SECTION MODE OUTPUT
            elif "sections" in mode_sel:
                approved = st.session_state.full_sections
                pending = st.session_state.full_section_pending
                sec_num = st.session_state.full_section_num

                # Show approved sections
                if approved:
                    total_words = sum(len(s.split()) for s in approved)
                    st.markdown(f"<div class='label'>Approved sections — {len(approved)} sections · ~{total_words:,} words total</div>", unsafe_allow_html=True)
                    for i, sec in enumerate(approved):
                        with st.expander(f"Section {i+1} — approved ✓"):
                            st.text_area("", value=sec, height=200,
                                         label_visibility="collapsed", key=f"sec_view_{i}")

                # Show pending section for approval
                if pending:
                    st.markdown(f"<div class='label'>Section {sec_num} — review before approving</div>", unsafe_allow_html=True)
                    edited = st.text_area("", value=pending, height=350,
                                          label_visibility="collapsed", key="sec_pending")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        if st.button("✓ Approve — generate next section", key="sec_approve"):
                            # Auto-save this section
                            st.session_state.full_sections.append(edited)
                            new_record = {
                                "id": script_num,
                                "date": datetime.now().isoformat(),
                                "protocol": st.session_state.full_protocol_text,
                                "script": f"[SECTION {sec_num}]\n\n{edited}",
                                "anchor": st.session_state.full_anchor,
                                "pov": st.session_state.full_pov,
                                "constraint": st.session_state.full_constraint,
                                "word_target": f"Section {sec_num}",
                                "tone": full_tone,
                            }
                            save_script(new_record)
                            next_num = sec_num + 1
                            st.session_state.full_section_num = next_num
                            st.session_state.full_section_pending = ""
                            with st.spinner(f"Writing section {next_num} — pass 1 of 2..."):
                                try:
                                    section = generate_section(
                                        st.session_state.full_protocol_text,
                                        full_title.strip(), next_num,
                                        st.session_state.full_sections,
                                        st.session_state.api_key
                                    )
                                    st.session_state.full_section_pending = section
                                except Exception as e:
                                    st.error(f"Section generation failed: {str(e)}")
                            st.rerun()

                    with col2:
                        if st.button("↻ Regenerate this section", key="sec_regen"):
                            with st.spinner(f"Regenerating section {sec_num}..."):
                                try:
                                    section = generate_section(
                                        st.session_state.full_protocol_text,
                                        full_title.strip(), sec_num,
                                        st.session_state.full_sections,
                                        st.session_state.api_key
                                    )
                                    st.session_state.full_section_pending = section
                                except Exception as e:
                                    st.error(f"Regeneration failed: {str(e)}")
                            st.rerun()

                    with col3:
                        if st.button("⏹ Stop — assemble what I have", key="sec_stop"):
                            st.session_state.full_sections.append(edited)
                            st.session_state.full_section_pending = ""
                            full_assembled = "\n\n".join(st.session_state.full_sections)
                            st.session_state.full_generated_script = full_assembled
                            st.rerun()

                # Assembled full script download when done
                if approved and not pending:
                    assembled = "\n\n".join(approved)
                    total_words = len(assembled.split())
                    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
                    st.markdown(f"<div class='label'>Full assembled script — ~{total_words:,} words</div>", unsafe_allow_html=True)
                    st.text_area("", value=assembled, height=300,
                                 label_visibility="collapsed", key="full_assembled_view")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        pdf_bytes = export_pdf(assembled, script_num)
                        st.download_button("↓ PDF", pdf_bytes, file_name=f"script_{script_num:03d}_full.pdf",
                                           mime="application/pdf", key="full_assembled_pdf")
                    with col2:
                        docx_bytes = export_docx(assembled, script_num)
                        st.download_button("↓ Word", docx_bytes, file_name=f"script_{script_num:03d}_full.docx",
                                           mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                                           key="full_assembled_docx")
                    with col3:
                        if st.button("✕ Start new script", key="full_new"):
                            st.session_state.full_protocol_locked = False
                            st.session_state.full_sections = []
                            st.session_state.full_section_pending = ""
                            st.session_state.full_section_num = 1
                            st.session_state.full_generated_script = ""
                            st.rerun()




elif page == "Script Generator":
    # Redirect to Divergence Protocol in full mode — they are now the same page
    st.markdown("# SCRIPT BUILDER")
    st.markdown("<div style='font-size:13px;color:#6a6a6a;'>The Script Generator is now part of the Divergence Protocol page. Go to <b>Divergence Protocol</b> in the sidebar to build and generate your script from a title.</div>", unsafe_allow_html=True)




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
