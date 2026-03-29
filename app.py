import streamlit as st
import json
import os
import random
from datetime import datetime
from pathlib import Path

st.set_page_config(
    page_title="Specter — by Easy Skills",
    page_icon="👻",
    layout="wide",
    initial_sidebar_state="expanded"
)

from data import ANCHORS, ANGLES, POVS, DISTANCES, PARAS, CONSTRAINTS, DEFAULT_BANS
from storage import load_data, save_banned, save_script, load_recent_fingerprints, load_channel, save_channel
from generator import generate_script, generate_titles, generate_protocol_from_title, build_protocol_text, generate_section
from exporter import export_pdf, export_docx
from channel import resolve_channel_id, get_channel_videos, check_concept, get_youtube_api_key

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #f7f7f8 !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stSidebar"] {
    background-color: #ffffff !important;
    border-right: 1px solid #f0f0f0 !important;
}

[data-testid="stSidebar"] * {
    font-family: 'Inter', sans-serif !important;
}

h1, h2, h3 {
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em !important;
    color: #111 !important;
}

.stButton > button {
    background: #111 !important;
    border: none !important;
    color: #fff !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    border-radius: 10px !important;
    padding: 10px 20px !important;
    transition: opacity 0.15s !important;
}

.stButton > button:hover {
    opacity: 0.85 !important;
}

.stButton > button[kind="secondary"] {
    background: #fff !important;
    border: 1.5px solid #e8e8e8 !important;
    color: #555 !important;
}

.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #ffffff !important;
    border: 1.5px solid #e8e8e8 !important;
    color: #111 !important;
    font-family: 'Inter', sans-serif !important;
    border-radius: 12px !important;
    font-size: 14px !important;
    padding: 12px 16px !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.08) !important;
}

.stSelectbox > div > div {
    background: #ffffff !important;
    border: 1.5px solid #e8e8e8 !important;
    border-radius: 12px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
}

[data-testid="stExpander"] {
    background: #ffffff !important;
    border: 1.5px solid #f0f0f0 !important;
    border-radius: 14px !important;
}

[data-testid="stAlert"] {
    background: #faf5ff !important;
    border: 1px solid #e9d5ff !important;
    color: #6d28d9 !important;
    font-family: 'Inter', sans-serif !important;
    border-radius: 12px !important;
}

.stMarkdown p, .stMarkdown li {
    color: #444 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
}

.stRadio > label, .stCheckbox > label {
    color: #444 !important;
    font-family: 'Inter', sans-serif !important;
}

.stSpinner > div {
    border-color: #7c3aed transparent transparent transparent !important;
}

.sp-hero-label {
    font-size: 11px;
    font-weight: 600;
    color: #7c3aed;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 8px;
    text-align: center;
}

.sp-hero-title {
    font-size: 28px;
    font-weight: 700;
    color: #111;
    letter-spacing: -0.025em;
    text-align: center;
    margin-bottom: 6px;
}

.sp-hero-sub {
    font-size: 14px;
    color: #999;
    text-align: center;
    margin-bottom: 28px;
}

.sp-section-label {
    font-size: 10px;
    font-weight: 600;
    color: #bbb;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 10px;
    margin-top: 4px;
}

.sp-reason {
    background: #faf5ff;
    border: 1px solid #e9d5ff;
    border-radius: 12px;
    padding: 12px 16px;
    font-size: 12px;
    color: #6d28d9;
    line-height: 1.6;
    margin-bottom: 20px;
}

.sp-card {
    background: #ffffff;
    border: 1.5px solid #f0f0f0;
    border-radius: 14px;
    padding: 14px 16px 16px;
    height: 100%;
}

.sp-card-top {
    display: flex;
    align-items: center;
    gap: 7px;
    margin-bottom: 8px;
}

.sp-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}

.sp-card-label {
    font-size: 10px;
    font-weight: 600;
    color: #bbb;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.sp-card-val {
    font-size: 12px;
    color: #555;
    line-height: 1.6;
}

.sp-gen-btn {
    width: 100%;
    background: linear-gradient(135deg, #7c3aed, #2563eb);
    color: #fff;
    border: none;
    border-radius: 14px;
    padding: 15px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    font-family: 'Inter', sans-serif;
    letter-spacing: -0.01em;
    margin-top: 4px;
}

.sp-locked-badge {
    background: #f0fdf4;
    color: #16a34a;
    font-size: 12px;
    padding: 6px 14px;
    border-radius: 20px;
    font-weight: 500;
    display: inline-block;
    margin-bottom: 16px;
}

.sp-divider {
    border: none;
    border-top: 1px solid #f0f0f0;
    margin: 20px 0;
}

.sp-script-output {
    background: #ffffff;
    border: 1.5px solid #f0f0f0;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 16px;
}

.sp-approved-badge {
    background: #f0fdf4;
    color: #16a34a;
    font-size: 10px;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 20px;
    letter-spacing: 0.05em;
}

.sp-pending-label {
    font-size: 13px;
    font-weight: 600;
    color: #111;
    margin-bottom: 12px;
}

.sp-sidebar-brand {
    font-size: 18px;
    font-weight: 700;
    color: #111;
    letter-spacing: -0.02em;
}

.sp-sidebar-sub {
    font-size: 11px;
    color: #bbb;
    margin-top: 2px;
}

.sp-sidebar-icon {
    width: 32px;
    height: 32px;
    border-radius: 9px;
    background: linear-gradient(135deg, #7c3aed, #2563eb);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 8px;
}

.sp-stat {
    background: #f7f7f8;
    border-radius: 10px;
    padding: 12px 14px;
    margin-bottom: 8px;
}

.sp-stat-label {
    font-size: 10px;
    font-weight: 600;
    color: #bbb;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.sp-stat-num {
    font-size: 24px;
    font-weight: 700;
    color: #111;
    letter-spacing: -0.02em;
}

.sp-nav-item {
    padding: 8px 12px;
    border-radius: 9px;
    font-size: 13px;
    font-weight: 500;
    color: #888;
    cursor: pointer;
    margin-bottom: 2px;
}

.sp-nav-active {
    background: #f7f7f8;
    color: #111;
}

.sp-mode-toggle {
    display: flex;
    background: #f5f5f5;
    border-radius: 10px;
    padding: 3px;
    margin-bottom: 20px;
}

.sp-tag {
    font-size: 10px;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 20px;
    letter-spacing: 0.05em;
    display: inline-block;
}

.sp-tag-purple { background: #f5f3ff; color: #6d28d9; }
.sp-tag-blue   { background: #eff6ff; color: #1d4ed8; }
.sp-tag-teal   { background: #f0fdfa; color: #0f766e; }
.sp-tag-amber  { background: #fffbeb; color: #b45309; }
.sp-tag-green  { background: #f0fdf4; color: #16a34a; }
.sp-tag-red    { background: #fef2f2; color: #b91c1c; }
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
if 'channel' not in st.session_state:
    st.session_state.channel = load_channel()
if 'concept_result' not in st.session_state:
    st.session_state.concept_result = None
if 'api_key' not in st.session_state:
    # Try to load from Streamlit secrets (works on Streamlit Cloud and locally via .streamlit/secrets.toml)
    try:
        st.session_state.api_key = st.secrets["ANTHROPIC_API_KEY"]
    except Exception:
        st.session_state.api_key = ""

with st.sidebar:
    st.markdown("""
    <div class='sp-sidebar-icon'>S</div>
    <div class='sp-sidebar-brand'>Specter</div>
    <div class='sp-sidebar-sub'>by Easy Skills · Hassan Ali</div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    try:
        _from_secrets = bool(st.secrets.get("ANTHROPIC_API_KEY"))
    except Exception:
        _from_secrets = False

    if _from_secrets:
        st.markdown("<div style='font-size:12px;color:#16a34a;font-weight:500;margin-bottom:4px;'>✓ API connected</div>", unsafe_allow_html=True)
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
    st.markdown(f"""
    <div class='sp-stat'>
        <div class='sp-stat-label'>Next script</div>
        <div class='sp-stat-num'>#{script_num:03d}</div>
    </div>
    <div class='sp-stat'>
        <div class='sp-stat-label'>Banned moves</div>
        <div class='sp-stat-num'>{len(data.get("banned", []))}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.channel.get("channel_name"):
        ch = st.session_state.channel
        st.markdown(f"<div style='font-size:11px;font-weight:600;color:#7c3aed;background:#f5f3ff;border:1px solid #e9d5ff;border-radius:20px;padding:5px 12px;margin-top:8px;text-align:center;'>📺 {ch['channel_name']}</div>", unsafe_allow_html=True)

    st.markdown("---")

    if st.session_state.mode == "Simple":
        page = st.radio("", ["Quick Generate", "Script History"], label_visibility="collapsed")
    else:
        page = st.radio("", ["Divergence Protocol", "Script Generator", "Title Machine", "Script History", "Anti-Pattern Log", "Channel Settings"], label_visibility="collapsed")


if page == "Quick Generate":
    st.markdown("<div class='sp-hero-label'>Simple mode — team view</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-hero-title'>What's the next script?</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-hero-sub'>Paste a title. Specter builds the protocol and writes the script automatically.</div>", unsafe_allow_html=True)
    st.markdown("")

    if not st.session_state.api_key:
        st.warning("Add your Anthropic API key in the sidebar to generate scripts.")

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

    if st.button("Generate Script", key="simple_gen"):
        if not st.session_state.api_key:
            st.error("API key required.")
        elif not title_input.strip():
            st.error("Paste a video title first.")
        else:
            # Concept check
            proceed = True
            if st.session_state.channel.get("channel_id") and get_youtube_api_key():
                with st.spinner(f"Checking concept against {st.session_state.channel.get('channel_name','your channel')}..."):
                    try:
                        videos = get_channel_videos(st.session_state.channel["channel_id"], get_youtube_api_key())
                        result = check_concept(title_input.strip(), videos, st.session_state.api_key)
                        st.session_state.concept_result = result
                        if result["status"] == "red":
                            proceed = False
                    except Exception as e:
                        st.warning(f"Concept check skipped: {e}")

            if st.session_state.concept_result and not proceed:
                r = st.session_state.concept_result
                st.error(f"**Concept already covered** — {r['reason']}")
                if r.get("matches"):
                    st.markdown("Overlapping videos: " + " · ".join([f"`{m}`" for m in r["matches"][:3]]))
                st.info("Change your title angle and try again.")
            else:
                if st.session_state.concept_result and st.session_state.concept_result["status"] == "yellow":
                    r = st.session_state.concept_result
                    st.warning(f"⚠ Adjacent concept — {r['reason']} Proceeding anyway.")

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
            with st.expander("View auto-generated protocol — what ran behind the scenes"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"<div class='sp-section-label'>Reality anchor</div><div style='font-size:13px;line-height:1.7;margin-bottom:16px;color:#444;'>{p.get('anchor','')}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='sp-section-label'>Entry angle</div><div style='font-size:13px;line-height:1.7;margin-bottom:16px;color:#444;'>{p.get('angle','')}</div>", unsafe_allow_html=True)
                    if p.get('reasoning'):
                        st.markdown(f"<div class='sp-reason'>{p.get('reasoning','')}</div>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<div class='sp-section-label'>POV</div><div style='font-size:13px;margin-bottom:12px;color:#444;'>{p.get('pov','')}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='sp-section-label'>Distance</div><div style='font-size:13px;margin-bottom:12px;color:#444;'>{p.get('distance','')}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='sp-section-label'>Structure</div><div style='font-size:13px;margin-bottom:12px;color:#444;'>{p.get('para','')}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='sp-section-label'>Hard constraint</div><div style='font-size:13px;color:#444;'>{p.get('constraint','')}</div>", unsafe_allow_html=True)

        st.markdown(f"<div class='sp-section-label'>Generated script — auto-saved as #{script_num-1:03d}</div>", unsafe_allow_html=True)
        st.text_area("", value=st.session_state.simple_script, height=500, label_visibility="collapsed", key="simple_script_area")

        st.markdown("")
        col1, col2, col3 = st.columns(3)
        with col1:
            pdf_bytes = export_pdf(st.session_state.simple_script, script_num - 1)
            st.download_button("Download PDF", pdf_bytes, file_name=f"script_{script_num-1:03d}.pdf", mime="application/pdf")
        with col2:
            docx_bytes = export_docx(st.session_state.simple_script, script_num - 1)
            st.download_button("Download Word", docx_bytes, file_name=f"script_{script_num-1:03d}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        with col3:
            if st.button("Generate Titles"):
                st.session_state.go_to_titles = True
                st.session_state.title_script = st.session_state.simple_script
                st.session_state.mode = "Full"
                st.rerun()


elif page == "Divergence Protocol":
    st.markdown("<div class='sp-hero-label'>Full mode — Hassan Ali</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-hero-title'>What's your next script?</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-hero-sub'>Enter a title. Specter suggests the protocol. You review, override, then generate.</div>", unsafe_allow_html=True)
    st.markdown("")

    if not st.session_state.api_key:
        st.warning("Add your Anthropic API key in the sidebar.")

    # Step 1 — Title
    st.markdown("<div class='sp-section-label'>Step 1 — Video title</div>", unsafe_allow_html=True)
    full_title = st.text_input(
        "Title",
        value=st.session_state.get("full_title", ""),
        placeholder="e.g. The Hidden HIERARCHY of Lovecraft's Gods (Who Really Controls Everything)",
        label_visibility="collapsed"
    )
    if full_title:
        st.session_state.full_title = full_title

    st.markdown("")

    if st.button("Analyse title and suggest protocol", key="analyse_title"):
        if not st.session_state.api_key:
            st.error("API key required.")
        elif not full_title.strip():
            st.error("Enter a title first.")
        else:
            # Concept check first
            proceed = True
            if st.session_state.channel.get("channel_id") and get_youtube_api_key():
                with st.spinner(f"Checking concept against {st.session_state.channel.get('channel_name','your channel')}..."):
                    try:
                        videos = get_channel_videos(st.session_state.channel["channel_id"], get_youtube_api_key())
                        result = check_concept(full_title.strip(), videos, st.session_state.api_key)
                        st.session_state.concept_result = result
                        if result["status"] == "red":
                            proceed = False
                    except Exception as e:
                        st.warning(f"Concept check skipped: {e}")

            if not proceed:
                r = st.session_state.concept_result
                st.error(f"**Concept already covered** — {r['reason']}")
                if r.get("matches"):
                    st.markdown("Overlapping videos: " + " · ".join([f"`{m}`" for m in r["matches"][:3]]))
                st.info("Change your title angle and try again.")
            else:
                if st.session_state.concept_result and st.session_state.concept_result.get("status") == "yellow":
                    r = st.session_state.concept_result
                    st.warning(f"⚠ Adjacent concept — {r['reason']} Review the suggested protocol carefully.")

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
                st.rerun()

    # Show suggestions if available
    if st.session_state.get("full_anchor"):
        st.markdown("<hr class='sp-divider'>", unsafe_allow_html=True)
        st.markdown("<div class='sp-section-label'>Step 2 — Review and override suggestions</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:13px;color:#6a6a6a;margin-bottom:20px;'>The tool analysed your title and pre-filled everything below. Change anything before generating — or accept as is.</div>", unsafe_allow_html=True)

        # Reasoning
        if st.session_state.get("full_reasoning"):
            st.markdown(f"<div style='font-size:12px;color:#6a6a6a;font-style:italic;margin-bottom:20px;padding:10px;background:#f8f8f6;border-left:2px solid #e0ddd4;'>◈ Why this anchor was chosen: {st.session_state.full_reasoning}</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='sp-card-top'><div class='sp-dot' style='background:#7c3aed'></div><div class='sp-card-label'>Reality anchor</div></div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#aaa;margin-bottom:8px;'>Must produce immediate dread — no explanation needed.</div>", unsafe_allow_html=True)
            full_anchor = st.text_area("Anchor", value=st.session_state.full_anchor, height=100, label_visibility="collapsed", key="ta_anchor")
            st.session_state.full_anchor = full_anchor

            st.markdown("")
            st.markdown("<div class='sp-card-top'><div class='sp-dot' style='background:#2563eb'></div><div class='sp-card-label'>Entry angle</div></div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#aaa;margin-bottom:8px;'>The lens that makes this data feel cosmically wrong.</div>", unsafe_allow_html=True)
            full_angle = st.text_area("Angle", value=st.session_state.full_angle, height=100, label_visibility="collapsed", key="ta_angle")
            st.session_state.full_angle = full_angle

            st.markdown("")
            st.markdown("<div class='sp-card-top'><div class='sp-dot' style='background:#d97706'></div><div class='sp-card-label'>Hard constraint</div></div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#aaa;margin-bottom:8px;'>One banned device or forced structural rule.</div>", unsafe_allow_html=True)
            full_constraint = st.text_area("Constraint", value=st.session_state.full_constraint, height=80, label_visibility="collapsed", key="ta_constraint")
            st.session_state.full_constraint = full_constraint

        with col2:
            st.markdown("<div class='sp-card-top'><div class='sp-dot' style='background:#0891b2'></div><div class='sp-card-label'>Point of view</div></div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#aaa;margin-bottom:8px;'>Who is narrating and how.</div>", unsafe_allow_html=True)
            full_pov = st.text_area("POV", value=st.session_state.full_pov, height=80, label_visibility="collapsed", key="ta_pov")
            st.session_state.full_pov = full_pov

            st.markdown("")
            st.markdown("<div class='sp-card-top'><div class='sp-dot' style='background:#059669'></div><div class='sp-card-label'>Narrative distance</div></div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#aaa;margin-bottom:8px;'>How close the narrator is to the subject.</div>", unsafe_allow_html=True)
            full_distance = st.text_area("Distance", value=st.session_state.full_distance, height=80, label_visibility="collapsed", key="ta_distance")
            st.session_state.full_distance = full_distance

            st.markdown("")
            st.markdown("<div class='sp-card-top'><div class='sp-dot' style='background:#db2777'></div><div class='sp-card-label'>Paragraph structure</div></div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size:12px;color:#aaa;margin-bottom:8px;'>How paragraphs are shaped across the script.</div>", unsafe_allow_html=True)
            full_para = st.text_area("Para", value=st.session_state.full_para, height=80, label_visibility="collapsed", key="ta_para")
            st.session_state.full_para = full_para

            st.markdown("")

        # Output mode selector
        st.markdown("<hr class='sp-divider'>", unsafe_allow_html=True)
        st.markdown("<div class='sp-section-label'>Step 3 — Output mode & tone</div>", unsafe_allow_html=True)
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
        st.markdown("<hr class='sp-divider'>", unsafe_allow_html=True)
        banned = data.get("banned", [])
        st.markdown(f"<div class='sp-section-label'>Active ban list — {len(banned)} moves</div>", unsafe_allow_html=True)
        if banned:
            ban_pills = " ".join([f"<span class='sp-tag sp-tag-purple'>{b['type']}</span>" for b in banned[:6]])
            if len(banned) > 6:
                ban_pills += f" <span style='color:#bbb;font-size:12px;'>+{len(banned)-6} more</span>"
            st.markdown(f"<div style='margin-bottom:4px;line-height:2;'>{ban_pills}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='font-size:12px;color:#bbb;'>No bans yet — go to Anti-Pattern Log to add them.</div>", unsafe_allow_html=True)

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
            st.markdown("<hr class='sp-divider'>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:12px;color:#3a6b3a;margin-bottom:16px;'>✓ Protocol locked — all sections use the same brief</div>", unsafe_allow_html=True)

            mode_sel = st.session_state.full_output_mode

            # NON-SECTIONED OUTPUT
            if "sections" not in mode_sel and st.session_state.full_generated_script:
                st.markdown("<div class='sp-section-label'>Generated script</div>", unsafe_allow_html=True)
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
                    st.markdown(f"<div class='sp-section-label'>Approved sections — {len(approved)} sections · ~{total_words:,} words total</div>", unsafe_allow_html=True)
                    for i, sec in enumerate(approved):
                        with st.expander(f"Section {i+1} — approved ✓"):
                            st.text_area("", value=sec, height=200,
                                         label_visibility="collapsed", key=f"sec_view_{i}")

                # Show pending section for approval
                if pending:
                    st.markdown(f"<div class='sp-section-label'>Section {sec_num} — review before approving</div>", unsafe_allow_html=True)
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
                    st.markdown("<hr class='sp-divider'>", unsafe_allow_html=True)
                    st.markdown(f"<div class='sp-section-label'>Full assembled script — ~{total_words:,} words</div>", unsafe_allow_html=True)
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
    st.markdown("<div class='sp-hero-label'>Full mode redirect</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:13px;color:#6a6a6a;'>The Script Generator is now part of the Divergence Protocol page. Go to <b>Divergence Protocol</b> in the sidebar to build and generate your script from a title.</div>", unsafe_allow_html=True)




elif page == "Title Machine":
    st.markdown("<div class='sp-hero-label'>Full mode</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-hero-title'>Title machine</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-section-label'>Generate rage-bait titles that resolve into defensible arguments</div>", unsafe_allow_html=True)
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
        st.markdown("<hr class='sp-divider'>", unsafe_allow_html=True)
        for group in st.session_state.generated_titles:
            st.markdown(f"<div class='sp-section-label'>{group['style']}</div>", unsafe_allow_html=True)
            for title in group['titles']:
                col1, col2 = st.columns([6, 1])
                with col1:
                    st.markdown(f"<div class='sp-card-val' style='margin-bottom:6px;'>{title}</div>", unsafe_allow_html=True)
                with col2:
                    st.button("Copy", key=f"copy_{title[:20]}")
            st.markdown("")

        all_titles = "\n".join([t for g in st.session_state.generated_titles for t in g['titles']])
        st.download_button("↓ Download all titles", all_titles, file_name=f"titles_script_{script_num:03d}.txt")


elif page == "Script History":
    st.markdown("<div class='sp-hero-label'>All scripts</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-hero-title'>Script history</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-section-label'>All saved scripts — sorted newest first</div>", unsafe_allow_html=True)
    st.markdown("")

    scripts = data.get("scripts", [])
    if not scripts:
        st.markdown("<div style='color:#aaaaaa;font-size:13px;padding:40px 0;'>No scripts saved yet. Generate and save your first one.</div>", unsafe_allow_html=True)
    else:
        for script in reversed(scripts):
            with st.expander(f"Script #{script['id']:03d}  —  {script['date'][:10]}  —  {(script.get('anchor','') or '')[:60]}..."):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"<div class='sp-section-label'>POV</div><div style='font-size:13px;'>{script.get('pov','—')}</div>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<div class='sp-section-label'>Constraint</div><div style='font-size:13px;'>{script.get('constraint','—')}</div>", unsafe_allow_html=True)
                with col3:
                    st.markdown(f"<div class='sp-section-label'>Tone</div><div style='font-size:13px;'>{script.get('tone','—')}</div>", unsafe_allow_html=True)

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
    st.markdown("<div class='sp-hero-label'>Structural memory</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-hero-title'>Anti-pattern log</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-section-label'>The living memory of structural moves already used — grows every script</div>", unsafe_allow_html=True)
    st.markdown("")

    banned = data.get("banned", [])

    types = ["all"] + list(set(b["type"] for b in banned))
    filter_type = st.selectbox("Filter by type", types, label_visibility="collapsed")

    filtered = banned if filter_type == "all" else [b for b in banned if b["type"] == filter_type]

    st.markdown(f"<div class='sp-section-label'>{len(filtered)} moves logged</div>", unsafe_allow_html=True)
    st.markdown("")

    for i, b in enumerate(filtered):
        col1, col2, col3 = st.columns([1, 5, 1])
        with col1:
            st.markdown(f"<span class='sp-tag sp-tag-purple'>{b['type'].upper()}</span>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<span style='font-size:13px;line-height:1.8;'>{b['move']}</span>", unsafe_allow_html=True)
        with col3:
            real_i = banned.index(b)
            if st.button("✕", key=f"apl_del_{real_i}"):
                banned.pop(real_i)
                data["banned"] = banned
                save_banned(banned)
                st.rerun()

    st.markdown("<hr class='sp-divider'>", unsafe_allow_html=True)
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

elif page == "Channel Settings":
    st.markdown("<div class='sp-hero-label'>Concept protection</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-hero-title'>Channel settings</div>", unsafe_allow_html=True)
    st.markdown("<div class='sp-hero-sub'>Link your YouTube channel so Specter checks new titles against your existing videos before generating.</div>", unsafe_allow_html=True)
    st.markdown("")

    yt_key = get_youtube_api_key()
    if not yt_key:
        st.warning("⚠ Add your YOUTUBE_API_KEY to Streamlit secrets to enable concept checking. See the README for instructions.")

    # Show saved channel
    ch = st.session_state.channel
    if ch.get("channel_name"):
        st.markdown(f"<div class='sp-locked-badge'>✓ Linked: {ch['channel_name']} ({ch.get('channel_url','')})</div>", unsafe_allow_html=True)
        st.markdown("")

    st.markdown("<div class='sp-section-label'>YouTube channel URL or ID</div>", unsafe_allow_html=True)
    channel_input = st.text_input(
        "Channel",
        value=ch.get("channel_url", ""),
        placeholder="e.g. https://youtube.com/@YourChannel or UCxxxxxxxx",
        label_visibility="collapsed"
    )
    st.markdown("<div style='font-size:12px;color:#aaa;margin-top:4px;margin-bottom:16px;'>Accepts full YouTube URL, @handle URL, or raw channel ID (starts with UC).</div>", unsafe_allow_html=True)

    if st.button("Save channel", key="save_ch"):
        if not yt_key:
            st.error("YOUTUBE_API_KEY not found in secrets.")
        elif not channel_input.strip():
            st.error("Enter a channel URL or ID first.")
        else:
            with st.spinner("Verifying channel..."):
                try:
                    channel_id, channel_name = resolve_channel_id(channel_input.strip(), yt_key)
                    if not channel_id:
                        st.error("Could not find channel. Try the full YouTube URL e.g. https://youtube.com/@YourChannel")
                    else:
                        save_channel(channel_id, channel_input.strip(), channel_name)
                        st.session_state.channel = {"channel_id": channel_id, "channel_url": channel_input.strip(), "channel_name": channel_name}
                        st.success(f"✓ Channel saved: {channel_name}")
                        st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")

    st.markdown("<hr class='sp-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='sp-section-label'>How concept checking works</div>", unsafe_allow_html=True)
    st.markdown("")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style='background:#f0fdf4;border:1.5px solid #bbf7d0;border-radius:14px;padding:14px'>
            <div style='font-size:10px;font-weight:600;color:#16a34a;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px'>Green</div>
            <div style='font-size:13px;color:#444;line-height:1.6'>Genuinely new concept. Safe to generate.</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style='background:#fffbeb;border:1.5px solid #fde68a;border-radius:14px;padding:14px'>
            <div style='font-size:10px;font-weight:600;color:#b45309;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px'>Yellow</div>
            <div style='font-size:13px;color:#444;line-height:1.6'>Adjacent to existing content. Proceed with a different angle.</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style='background:#fef2f2;border:1.5px solid #fecaca;border-radius:14px;padding:14px'>
            <div style='font-size:10px;font-weight:600;color:#b91c1c;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px'>Red</div>
            <div style='font-size:13px;color:#444;line-height:1.6'>This concept is already published. YouTube will flag it as repetitive.</div>
        </div>""", unsafe_allow_html=True)
