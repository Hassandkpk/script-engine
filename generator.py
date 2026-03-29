import anthropic
import json


def apply_voice_filter(raw_script: str, title: str, api_key: str) -> str:
    system_prompt = (
        "You are a senior script editor for a cosmic horror YouTube channel. "
        "Your audience listens — they do not read. Many listen at night, many are trying to sleep. "
        "They are intelligent but not academic. They came to feel something, not to study something.\n\n"
        "You receive a raw script draft and rewrite it according to these non-negotiable principles:\n\n"
        "NARRATOR PRESENCE\n"
        "The script must have a consistent human narrator voice throughout. "
        "Not floating academic prose. A person is speaking. That person has a perspective. "
        "Short declarative statements are the spine. Longer sentences expand them. "
        "The narrator never disappears into the material.\n\n"
        "LISTENER ADDRESS\n"
        "The narrator speaks to the listener directly at least twice — not with rhetorical questions, "
        "not with 'you won't believe this', but with genuine direct address that makes the listener "
        "feel they are being told something specific. "
        "Never opens with a rhetorical question. Never ends with 'what do you think?'\n\n"
        "EARNED COMPLEXITY\n"
        "No concept arrives without context. Every technical term, historical reference, or "
        "philosophical idea is grounded before it goes deep. The listener is smart. "
        "They are not already informed. Build before you go complex.\n\n"
        "EAR RHYTHM\n"
        "Sentences vary in length deliberately. Short sentence. Then one that breathes and expands. "
        "Then short again to land the point. No paragraph reads the same as the one before it.\n\n"
        "STRUCTURAL BANS — banned without exception:\n"
        "- Opening with a rhetorical question of any kind\n"
        "- Three-part documentary structure\n"
        "- Mid-script subscription CTA\n"
        "- Ending with an open question back to the audience\n"
        "- Any sentence beginning with 'What if'\n"
        "- Paragraph-length lists\n"
        "- Academic summary language: 'in conclusion', 'as we have seen', 'this document examines'\n\n"
        "WHAT TO PRESERVE\n"
        "Preserve all real data, all factual content, all structural uniqueness from the original draft. "
        "You are changing the voice and rhythm, not the argument.\n\n"
        "Output only the rewritten script. No preamble, no notes, no commentary."
    )

    user_prompt = (
        f"Video title: {title}\n\n"
        f"Raw script draft to rewrite:\n\n"
        f"{raw_script}\n\n"
        f"Rewrite this script now applying all voice filter principles. "
        f"Output only the finished script."
    )

    client = anthropic.Anthropic(api_key=api_key.strip())
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}]
    )
    return message.content[0].text


def generate_script(protocol: str, word_target: str, tone: str, api_key: str, title: str = "") -> str:
    word_map = {
        "1,700–2,200 words (full script)": "1,700 to 2,200 words",
        "800–1,000 words (short form)": "800 to 1,000 words",
        "200 words (intro only)": "approximately 200 words — intro only",
    }
    tone_map = {
        "Forensic — clinical dread": "forensic and clinical — dread emerges from precision, not description",
        "Existential — scale horror": "existential — the horror comes from scale and the smallness of the human",
        "Intimate — personal wrongness": "intimate — the wrongness is close, specific, personal",
        "Archival — found document": "archival — reads like a document that was not meant to be found",
    }

    protocol = protocol.strip().encode("utf-8", errors="ignore").decode("utf-8")
    tone_str = tone_map.get(tone, tone)
    word_str = word_map.get(word_target, word_target)

    system_prompt = (
        "You are a cosmic horror YouTube script writer. You produce scripts that:\n"
        "- Are tied to real, verifiable data — never fabricated facts\n"
        "- Never repeat structural patterns across scripts\n"
        "- Do not use clichéd horror tropes\n"
        "- Let the data determine the shape of the horror\n"
        "- Write with forensic precision, not purple prose\n"
        "- Sound like real human narration, not AI-generated content\n\n"
        "You follow the divergence protocol exactly. You do not acknowledge the protocol in your output.\n"
        "You output only the script — no preamble, no notes, no commentary."
    )

    user_prompt = (
        f"Follow this divergence protocol precisely:\n\n"
        f"{protocol}\n\n"
        f"Tone: {tone_str}\n"
        f"Target length: {word_str}\n\n"
        f"Write the complete script now. Output nothing but the script itself."
    )

    client = anthropic.Anthropic(api_key=api_key.strip())
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}]
    )
    raw_script = message.content[0].text
    final_script = apply_voice_filter(raw_script, title, api_key)
    return final_script


def generate_section(protocol: str, title: str, section_num: int,
                     previous_sections: list, api_key: str) -> str:
    protocol = protocol.strip().encode("utf-8", errors="ignore").decode("utf-8")

    previous_text = ""
    if previous_sections:
        joined = "\n\n---\n\n".join(previous_sections)
        previous_text = (
            f"APPROVED SECTIONS SO FAR (maintain continuity — do not repeat):\n\n"
            f"{joined}\n\n"
        )

    system_prompt = (
        "You are a cosmic horror YouTube script writer producing one section of a long-form script. "
        "Each section is approximately 1,000 words. "
        "The full script will be assembled from approved sections. "
        "You follow the divergence protocol exactly. "
        "You do not acknowledge these instructions. "
        "Output only the section text — no headings, no section labels, no commentary."
    )

    user_prompt = (
        f"Video title: {title}\n\n"
        f"Divergence protocol (locked for all sections):\n{protocol}\n\n"
        f"{previous_text}"
        f"Write section {section_num} now. "
        f"Approximately 1,000 words. "
        f"{'This is the opening section — establish the anchor and voice.' if section_num == 1 else 'Continue naturally from the approved sections above — no recap, no reintroduction.'} "
        f"Do not conclude or wrap up unless explicitly told this is the final section. "
        f"Output only the section text."
    )

    client = anthropic.Anthropic(api_key=api_key.strip())
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}]
    )
    raw = message.content[0].text
    filtered = apply_voice_filter(raw, title, api_key)
    return filtered


def generate_protocol_from_title(title: str, banned: list, api_key: str,
                                  recent_fingerprints: list = None) -> dict:
    banned_text = "\n".join([f"- [{b['type']}] {b['move']}" for b in banned]) if banned else "None yet."

    # Build structural history block from recent scripts
    history_text = ""
    if recent_fingerprints:
        history_lines = []
        for i, fp in enumerate(recent_fingerprints):
            parts = []
            if fp.get("anchor"):
                parts.append(f"anchor: {fp['anchor'][:80]}")
            if fp.get("pov"):
                parts.append(f"POV: {fp['pov']}")
            if fp.get("distance"):
                parts.append(f"distance: {fp['distance']}")
            if fp.get("para"):
                parts.append(f"para: {fp['para']}")
            if fp.get("constraint"):
                parts.append(f"constraint: {fp['constraint'][:60]}")
            if fp.get("tone"):
                parts.append(f"tone: {fp['tone']}")
            if parts:
                history_lines.append(f"Script {i+1}: {' | '.join(parts)}")
        if history_lines:
            history_text = (
                "STRUCTURAL HISTORY — last scripts already produced "
                "(do not repeat any anchor domain, POV, distance, paragraph structure, or constraint from this list):\n"
                + "\n".join(history_lines)
                + "\n\n"
            )

    system = (
        "You are an expert cosmic horror YouTube script architect.\n"
        "Given a video title, you generate a complete divergence protocol — a pre-script brief that ensures\n"
        "the resulting script is structurally unique, grounded in real data, and avoids all AI default patterns.\n"
        "You output only valid JSON. No preamble, no explanation.\n\n"
        "CRITICAL — ANCHOR SELECTION RULE:\n"
        "The audience for this channel listens at night. Many listen to sleep. They are not academics.\n"
        "They are cosmic horror fans who want to FEEL something, not learn something.\n\n"
        "Before choosing any anchor, ask yourself this test:\n"
        "'Can someone who has never studied this topic feel dread from this anchor within the first paragraph\n"
        "— without needing any explanation first?'\n\n"
        "If the answer is NO — REJECT it and find a different anchor.\n\n"
        "GOOD anchors pass the visceral test immediately:\n"
        "- Sleep paralysis research (30% of people have experienced it)\n"
        "- Deep ocean pressure data (steel-crushing depths, things that have never seen light)\n"
        "- Brain's response to incomprehensible stimuli (the prefrontal cortex shuts down)\n"
        "- Infrasound frequencies that trigger dread in mammals (below hearing, felt in the chest)\n"
        "- Historical population disappearances (entire communities, no remains, no explanation)\n"
        "- Documented cases of people who saw something and refused to describe it\n"
        "- Biological anomalies in deep-sea creatures (morphologies that violate evolutionary logic)\n"
        "- Real archaeological finds with no civilization that could have made them\n\n"
        "BAD anchors fail the visceral test:\n"
        "- Organizational theory or management science\n"
        "- Abstract mathematical proofs\n"
        "- Literary theory or philosophical frameworks\n"
        "- Anything requiring technical knowledge before feeling anything\n\n"
        "CRITICAL — STRUCTURAL ROTATION RULE:\n"
        "You will be given a structural history of recent scripts. "
        "You must choose a POV, narrative distance, paragraph structure, and constraint "
        "that have NOT been used in recent scripts. "
        "Rotate deliberately — if the last script used 'forensic distance', pick something else. "
        "If the last script used 'second person', pick a different POV. "
        "The goal is that no two consecutive scripts feel structurally similar."
    )

    user = (
        f'Video title: "{title}"\n\n'
        f"{history_text}"
        f"Banned structural moves (manual log — never repeat these):\n"
        f"{banned_text}\n\n"
        f"Generate a divergence protocol for this title. Return a JSON object with exactly these fields:\n\n"
        f'{{\n'
        f'  "anchor": "A specific real-world data domain that passes the visceral test",\n'
        f'  "angle": "The exact cognitive lens that makes this real data feel cosmically wrong — one sentence a non-expert immediately understands",\n'
        f'  "pov": "One of: second person, first person plural (we), third person omniscient restrained, false documentary (field notes), nested narration, no narrator (pure phenomena), first person singular dissolving into report, second person plural",\n'
        f'  "distance": "One of: maximum intimacy, forensic distance, historical distance, dissolving distance (starts far collapses close), unreliable proximity, absolute removal",\n'
        f'  "para": "One of: paragraphs compress as script progresses, alternating long/short rhythm, single unbroken block, each paragraph shorter than previous, fragments only, normal prose fragmenting in final third, paragraphs expand as script progresses, two sentences per paragraph maximum",\n'
        f'  "constraint": "One specific hard constraint — must not repeat any constraint from structural history above",\n'
        f'  "reasoning": "One sentence explaining why this anchor passes the visceral test AND why these structural choices differ from recent scripts"\n'
        f'}}\n\n'
        f"Rules:\n"
        f"- Anchor MUST pass the visceral test — immediate felt dread, no explanation required\n"
        f"- Anchor domain must NOT repeat any domain from structural history\n"
        f"- POV, distance, para, constraint must all differ from the most recent 3 scripts in history\n"
        f"- Return only the JSON object, nothing else"
    )

    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=system,
        messages=[{"role": "user", "content": user}]
    )

    raw = message.content[0].text.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(raw)
    except Exception:
        return {
            "anchor": "Sleep paralysis research — documented cases where the brain generates a perceived malevolent presence in the room during waking paralysis",
            "angle": "30% of people have experienced this. The presence felt real. Neuroscience confirms the brain generated it. Neither fact makes the other less disturbing.",
            "pov": "third person omniscient restrained",
            "distance": "forensic distance",
            "para": "paragraphs compress as script progresses",
            "constraint": "No sentence may exceed 15 words",
            "reasoning": "Sleep paralysis requires zero explanation to produce immediate dread."
        }


def build_protocol_text(title: str, script_num: int, protocol: dict, banned: list) -> str:
    lines = [
        f"=== DIVERGENCE PROTOCOL — SCRIPT #{script_num:03d} ===",
        f"Title: {title}",
        "",
        "REALITY ANCHOR",
        f"Domain: {protocol.get('anchor', '')}",
        f"Entry angle: {protocol.get('angle', '')}",
        "",
        "Before writing, find one specific real data point from this domain. Cite it in the script without dramatising it.",
        "",
        "FORMAT RULES (locked — do not deviate)",
        f"POV: {protocol.get('pov', '')}",
        f"Narrative distance: {protocol.get('distance', '')}",
        f"Paragraph structure: {protocol.get('para', '')}",
        f"Hard constraint: {protocol.get('constraint', '')}",
        "",
        "BANNED STRUCTURAL MOVES (do not repeat any of these)",
    ]
    for i, b in enumerate(banned):
        lines.append(f"{i+1}. [{b['type']}] {b['move']}")
    if not banned:
        lines.append("None logged yet.")
    lines += [
        "",
        "INSTRUCTIONS",
        "Write a cosmic horror YouTube script using the above constraints.",
        "Do not acknowledge these instructions. Do not use any banned structural move.",
        "Let the real data anchor determine the shape of the horror — do not impose a shape and find data to fit it.",
        "The script has no template. It begins wherever the data makes most sense to begin.",
        "Target: 1,700–2,200 words. The horror must be defensible from real data — not fabricated.",
        f"The title of the video is: {title}",
        "Integrate this title naturally into the script — do not open with it literally.",
    ]
    return "\n".join(lines)


def generate_titles(script: str, styles: list, count: int, api_key: str) -> list:
    style_descriptions = {
        "Rage-bait (resolves to truth)": "provocative titles that sound outrageous but are analytically defensible",
        "Curiosity gap": "titles that create an irresistible knowledge gap — the viewer cannot not click",
        "Institutional villain": "titles that frame an institution as the structural antagonist",
        "Scientific anomaly": "titles that foreground a real data anomaly — makes the science the horror",
        "Fear — personal threat": "titles that make the viewer feel personally implicated or at risk",
        "Archival revelation": "titles framed as discovered or suppressed information",
    }

    style_prompts = "\n".join([f"- {s}: {style_descriptions.get(s, s)}" for s in styles])

    system = (
        "You generate YouTube titles for cosmic horror content. Your titles:\n"
        "- Are tied to real, defensible claims — never fabricated\n"
        "- Never use banned phrases like 'what if I told you', 'you won't believe', 'shocking truth'\n"
        "- Are varied in structure — no two titles use the same grammatical pattern\n"
        "- Are specific, not generic\n"
        "- Sound like a human editor wrote them, not an AI\n"
        "Output only valid JSON."
    )

    user = (
        f"Based on this script content, generate {count} title options for each of these styles:\n\n"
        f"{style_prompts}\n\n"
        f"Script content:\n{script[:3000]}\n\n"
        f"Return a JSON array like this:\n"
        f'[{{"style": "Style name", "titles": ["Title 1", "Title 2"]}}, ...]\n\n'
        f"Return only the JSON array, nothing else."
    )

    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=system,
        messages=[{"role": "user", "content": user}]
    )

    raw = message.content[0].text.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(raw)
    except Exception:
        return [{"style": "Generated", "titles": [raw]}]


def generate_outline(title: str, protocol: dict, tone: str, api_key: str) -> dict:
    """Generate a structured outline: intro summary, main body sections with bullets, conclusion summary."""
    client = anthropic.Anthropic(api_key=api_key.strip())

    system = (
        "You are a cosmic horror YouTube script architect. "
        "You produce outlines for long-form scripts (~12,000 words total). "
        "Structure: 150-word intro, main body (~11,700 words across ~11 sections of ~1,000 words each), 150-word conclusion. "
        "Output only valid JSON."
    )

    user = f"""Title: "{title}"

Protocol:
- Anchor: {protocol.get('anchor', '')}
- Angle: {protocol.get('angle', '')}
- POV: {protocol.get('pov', '')}
- Distance: {protocol.get('distance', '')}
- Structure: {protocol.get('para', '')}
- Constraint: {protocol.get('constraint', '')}
- Tone: {tone}

Generate a detailed outline. Return JSON:
{{
  "intro": "2-3 sentences describing what the intro establishes and how it opens",
  "sections": [
    {{
      "heading": "Section heading",
      "bullets": ["what this section covers", "specific argument or data point", "how it connects to the horror"]
    }}
  ],
  "conclusion": "2-3 sentences describing what the conclusion lands and how it closes",
  "total_sections": 11
}}

Generate exactly 11 main body sections. Each section heading should be specific, not generic.
Return only the JSON object."""

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    raw = msg.content[0].text.strip().replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(raw)
    except Exception:
        return {"intro": "Outline generation failed.", "sections": [], "conclusion": ""}


def check_outline_uniqueness(title: str, outline: dict, past_scripts: list, api_key: str) -> dict:
    """Check if the outline structure and approach is unique vs past saved scripts."""
    client = anthropic.Anthropic(api_key=api_key.strip())

    if not past_scripts:
        return {"status": "unique", "reason": "No past scripts to compare against.", "conflicts": []}

    past_summary = "\n".join([
        f"- Script #{s.get('id','?')}: anchor={s.get('anchor','')[:60]} | pov={s.get('pov','')[:40]}"
        for s in past_scripts[-20:]
    ])

    section_headings = "\n".join([f"- {s['heading']}" for s in outline.get("sections", [])])

    system = "You are a content uniqueness analyst for a YouTube channel. Output only valid JSON."

    user = f"""New script outline:
Title: "{title}"
Intro approach: {outline.get('intro', '')}
Section headings:
{section_headings}
Conclusion: {outline.get('conclusion', '')}

Past scripts (last 20):
{past_summary}

Check if this outline's structure, approach, and argument flow is genuinely different from past scripts.
Focus on: same opening approach, same argumentative arc, same section structure, same conclusion framing.

Return JSON:
{{
  "status": "unique" | "similar" | "duplicate",
  "reason": "one sentence verdict",
  "conflicts": ["description of any specific similarity found"]
}}"""

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=400,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    raw = msg.content[0].text.strip().replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(raw)
    except Exception:
        return {"status": "unique", "reason": "Check inconclusive.", "conflicts": []}


def generate_intro(title: str, protocol_text: str, outline: dict, tone: str, api_key: str) -> str:
    raw = _generate_part(
        title, protocol_text, tone, api_key,
        instruction=f"Write ONLY the intro (exactly 150 words). Intro outline: {outline.get('intro', '')}. "
                    "No section headings. Just the opening 150 words of the script.",
        max_tokens=600
    )
    return apply_voice_filter(raw, title, api_key)


def generate_body_section(title: str, protocol_text: str, outline: dict, section_num: int,
                           approved_parts: list, tone: str, api_key: str) -> str:
    sections = outline.get("sections", [])
    if section_num <= len(sections):
        sec = sections[section_num - 1]
        section_brief = f"Heading: {sec['heading']}\nCover: {', '.join(sec.get('bullets', []))}"
    else:
        section_brief = f"Section {section_num} — continue the narrative arc toward the conclusion"

    prior = "\n\n---\n\n".join(approved_parts[-2:]) if approved_parts else ""
    prior_text = f"APPROVED CONTENT SO FAR (last 2 parts — maintain continuity, do not repeat):\n{prior}\n\n" if prior else ""

    raw = _generate_part(
        title, protocol_text, tone, api_key,
        instruction=f"{prior_text}Write ONLY section {section_num} of the main body (~1,000 words).\n{section_brief}\n"
                    "No intro recap. No conclusion. Continue naturally. Output only this section.",
        max_tokens=2000
    )
    return apply_voice_filter(raw, title, api_key)


def generate_conclusion(title: str, protocol_text: str, outline: dict,
                         approved_parts: list, tone: str, api_key: str) -> str:
    prior = "\n\n---\n\n".join(approved_parts[-2:]) if approved_parts else ""
    prior_text = f"APPROVED FINAL BODY SECTIONS (for continuity):\n{prior}\n\n" if prior else ""
    raw = _generate_part(
        title, protocol_text, tone, api_key,
        instruction=f"{prior_text}Write ONLY the conclusion (exactly 150 words). "
                    f"Conclusion outline: {outline.get('conclusion', '')}. "
                    "Land the horror. No new information. Close the script. Output only the conclusion.",
        max_tokens=600
    )
    return apply_voice_filter(raw, title, api_key)


def _generate_part(title: str, protocol_text: str, tone: str, api_key: str,
                   instruction: str, max_tokens: int = 2000) -> str:
    tone_map = {
        "Existential — scale horror": "existential — the horror comes from scale and the smallness of the human",
        "Forensic — clinical dread": "forensic and clinical — dread emerges from precision, not description",
        "Intimate — personal wrongness": "intimate — the wrongness is close, specific, personal",
        "Archival — found document": "archival — reads like a document that was not meant to be found",
    }
    client = anthropic.Anthropic(api_key=api_key.strip())
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=max_tokens,
        system=(
            "You are a cosmic horror YouTube script writer. Follow the divergence protocol exactly. "
            "Write for listeners, not readers. Output only the requested content — no labels, no preamble."
        ),
        messages=[{"role": "user", "content":
            f"Title: {title}\nTone: {tone_map.get(tone, tone)}\n\nProtocol:\n{protocol_text}\n\n{instruction}"
        }]
    )
    return msg.content[0].text
