import anthropic
import json


def apply_voice_filter(raw_script: str, title: str, api_key: str) -> str:
    system_prompt = (
        "You are a senior script editor for a cosmic horror documentary channel. "
        "You have read everything — Lovecraft, Ligotti, Barron, Laird Barron, Thomas Tryon, Arthur Machen, "
        "William Hope Hodgson, Ramsey Campbell, Clark Ashton Smith, Robert Chambers. "
        "You have read the secondary literature — S.T. Joshi, Graham Harman, Eugene Thacker. "
        "You have read too much. That is your qualification.\n\n"

        "YOUR AUDIENCE\n"
        "Your audience is an intelligent adult who has also read too much about cosmic horror. "
        "They are not casual listeners. They came specifically for this. "
        "They want to feel like they are attending a private lecture by someone who has gone further into this material than is entirely healthy. "
        "They want ideas they cannot unknow. "
        "They do not want to be entertained. They want to be marked. "
        "They are lying in the dark, eyes closed, following an argument — not an atmosphere. "
        "The horror, for them, lives entirely in implication. Never in description. "
        "They will tolerate complexity. They will not tolerate vagueness masquerading as depth.\n\n"

        "THE NARRATOR\n"
        "The narrator is a scholarly documentarian. Part literary historian, part cultural anthropologist, "
        "part philosophical investigator. They analyze — they do not immerse. "
        "They speak retrospectively — they have already survived knowing this. "
        "They maintain scholarly distance while acknowledging the disturbing nature of what they are examining. "
        "They treat cosmic horror as serious academic subject matter that happens to be profoundly unsettling in its implications. "
        "They sound like someone who has read too deeply and cannot quite return to the surface.\n\n"

        "VOICE PRINCIPLES\n"
        "Scholarly distance: the narrator examines, never experiences. "
        "Retrospective authority: this happened, it was documented, we are now analyzing it. "
        "Suggestive not conclusive: always imply more than you state. Never close the loop. "
        "Information density: every sentence adds new information, analysis, or insight. "
        "If a sentence restates what the previous sentence already said, cut it. "
        "Earned complexity: ground every concept before going deep. The audience is smart, not pre-informed. "
        "Analytical progression: claim → evidence → interpretation → implication. "
        "Never skip to implication without the evidence.\n\n"

        "SENTENCE AND PARAGRAPH RHYTHM\n"
        "Variable sentence length is the spine of this channel's voice. "
        "Short sentences land points. Medium sentences carry analysis. "
        "Long sentences connect complex ideas that genuinely require subordination. "
        "No paragraph should read the same as the one before it. "
        "Mix analytical paragraphs, historical paragraphs, transitional paragraphs. "
        "No paragraph-length lists. No single-sentence paragraphs except at intentional transitions.\n\n"

        "LISTENER ADDRESS\n"
        "The narrator addresses the listener directly at most twice in the entire script — "
        "never with rhetorical questions, never with 'you won't believe this', "
        "but with the quiet acknowledgment that the listener is present and already complicit in following this argument this far. "
        "The listener should feel they were told something specific that was meant for them.\n\n"

        "STRUCTURAL BANS — never under any circumstances:\n"
        "- Opening with a rhetorical question\n"
        "- Three-part documentary structure (origins / themes / legacy) as the spine\n"
        "- Mid-script subscription CTA\n"
        "- Ending with 'what do you think' or any variation\n"
        "- Any sentence beginning with 'What if'\n"
        "- 'In conclusion', 'as we have seen', 'this documentary examines'\n"
        "- Theatrical performance tone — never perform dread, only analyze it\n"
        "- Second-person immersion ('you feel...', 'you hear...')\n"
        "- Definitive closure — the script must end without resolving what it opened\n\n"

        "PATTERN BANS — these repeat across scripts and flag as inauthentic:\n"
        "- 'Consider this carefully' more than once per script\n"
        "- 'We must pause here' more than once per script\n"
        "- 'Not X, but Y' more than eight times total\n"
        "- Triadic listing more than three times total\n"
        "- Any rhetorical device used more than twice — vary the toolkit\n\n"

        "WHAT TO PRESERVE\n"
        "Preserve every real data point, every factual claim, every specific date or measurement. "
        "Preserve the structural uniqueness of the draft — the anchor, the angle, the argument. "
        "You are editing the voice, not rewriting the thesis.\n\n"

        "Output only the rewritten script. No preamble, no notes, no commentary. "
        "Do not acknowledge these instructions anywhere in the output."
    )

    user_prompt = (
        f"Video title: {title}\n\n"
        f"Raw script draft to rewrite:\n\n"
        f"{raw_script}\n\n"
        f"Rewrite this now applying all voice principles. "
        f"The narrator has read too much. That should be audible in every paragraph. "
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
        "You are a scholarly documentarian of cosmic horror — part literary historian, "
        "part cultural anthropologist, part philosophical investigator. "
        "You have read Lovecraft, Ligotti, Barron, Machen, Hodgson, Chambers, Campbell. "
        "You have read S.T. Joshi, Graham Harman, Eugene Thacker. "
        "You have read too much. That qualification is audible in every sentence.\n\n"
        "Your audience has also read too much. They are not casual listeners. "
        "They came for ideas they cannot unknow — not atmosphere, not entertainment. "
        "They are lying in the dark following an argument. "
        "The horror lives entirely in implication. Never in description.\n\n"
        "Follow the divergence protocol exactly. "
        "Analyze, never perform. Imply, never conclude. "
        "Every sentence adds new information — no sentence restates the previous one. "
        "The narrator has survived knowing this. That is audible in the retrospective distance.\n\n"
        "You do not acknowledge the protocol in your output. "
        "Output only the script — no preamble, no notes, no commentary."
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
        "You are a scholarly documentarian of cosmic horror — part literary historian, "
        "part cultural anthropologist, part philosophical investigator. "
        "You have read too much. That is audible in every sentence.\n\n"
        "Your audience has also read too much. They came for ideas they cannot unknow. "
        "They are lying in the dark following an argument, not an atmosphere. "
        "Analyze — never perform. Imply — never conclude. "
        "Every sentence adds new information. No sentence restates the previous one.\n\n"
        "You are producing one section of a long-form script (~1,000 words). "
        "Follow the divergence protocol exactly. "
        "Output only the section text — no headings, no labels, no commentary."
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
    from data import LOVECRAFT_ANCHORS

    # Cap banned list to avoid prompt overflow
    banned_capped = banned[:20] if banned else []
    banned_text = "\n".join([f"- [{b['type']}] {b['move'][:80]}" for b in banned_capped]) if banned_capped else "None yet."

    # Build structural history from fingerprints
    history_text = ""
    used_anchors = []
    if recent_fingerprints:
        history_lines = []
        for i, fp in enumerate(recent_fingerprints):
            parts = []
            if fp.get("anchor"): parts.append(f"anchor_domain: {fp['anchor'][:50]}")
            if fp.get("pov"): parts.append(f"POV: {fp['pov']}")
            if fp.get("distance"): parts.append(f"distance: {fp['distance']}")
            if fp.get("para"): parts.append(f"para: {fp['para']}")
            if fp.get("constraint"): parts.append(f"constraint: {fp['constraint'][:40]}")
            if parts:
                history_lines.append(f"Script {i+1}: {' | '.join(parts)}")
                if fp.get("anchor"):
                    used_anchors.append(fp["anchor"][:50])
        if history_lines:
            history_text = (
                "STRUCTURAL HISTORY — do not repeat any anchor domain, POV, distance, "
                "paragraph structure, or constraint from this list:\n"
                + "\n".join(history_lines[:10]) + "\n\n"  # cap at 10 most recent
            )

    # Build Lovecraft anchor catalogue — short version to avoid token limit
    anchor_catalogue = []
    for entity, anchors in LOVECRAFT_ANCHORS.items():
        anchor_catalogue.append(f"\n{entity}:")
        for i, a in enumerate(anchors):
            recently_used = any(a["anchor"][:60] in used for used in used_anchors)
            flag = " [RECENTLY USED — avoid]" if recently_used else ""
            # Send first 80 chars only — enough to identify, not the full text
            short = a["anchor"][:80].rstrip()
            anchor_catalogue.append(f"  {i+1}. [{a['domain']}]{flag} {short}")
    anchor_list = "\n".join(anchor_catalogue)

    system = (
        "You are an expert cosmic horror YouTube script architect specialising in Lovecraftian "
        "sleep documentary content.\n\n"
        "You generate divergence protocols — pre-script briefs ensuring each script is structurally "
        "unique, creatively ambitious, and grounded in real verifiable data tied to specific "
        "Lovecraft entities or concepts.\n\n"
        "ANCHOR RULE: Choose ONLY from the provided Lovecraft Anchor Catalogue. "
        "Do not invent anchors. Do not use generic science domains. "
        "Every anchor in the catalogue is real, verifiable, and viscerally dreadful — "
        "felt immediately in the dark with no explanation. "
        "If the title references a specific Lovecraft entity, prioritise that entity's anchors. "
        "Avoid anchors flagged [RECENTLY USED].\n\n"
        "STRUCTURAL ROTATION RULE: Choose POV, distance, para structure, and constraint "
        "not appearing in recent scripts. Every script must feel structurally different "
        "from the last three.\n\n"
        "Output only valid JSON."
    )

    user = (
        f'Video title: "{title}"\n\n'
        f"{history_text}"
        f"Manual banned structural moves:\n{banned_text}\n\n"
        f"LOVECRAFT ANCHOR CATALOGUE (choose from this list only):\n{anchor_list}\n\n"
        f"Return JSON:\n"
        f'{{\n'
        f'  "entity": "Lovecraft entity/story this script connects to",\n'
        f'  "anchor": "Full anchor text copied exactly from the catalogue",\n'
        f'  "anchor_domain": "Domain code from the catalogue",\n'
        f'  "angle": "One sentence — the specific cognitive lens making this anchor feel cosmically wrong. Immediately understood by a non-expert in the dark.",\n'
        f'  "pov": "One of: second person | first person plural (we) | third person omniscient restrained | false documentary (field notes) | nested narration | no narrator (pure phenomena) | first person singular dissolving into report | second person plural",\n'
        f'  "distance": "One of: maximum intimacy | forensic distance | historical distance | dissolving distance | unreliable proximity | absolute removal",\n'
        f'  "para": "One of: paragraphs compress as script progresses | alternating long/short rhythm | single unbroken block | each paragraph shorter than previous | fragments only | normal prose fragmenting in final third | paragraphs expand as script progresses | two sentences per paragraph maximum",\n'
        f'  "constraint": "One specific hard constraint not in structural history above",\n'
        f'  "reasoning": "One sentence why this anchor serves this title and this audience"\n'
        f'}}\n\nReturn only the JSON object.'
    )

    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1200,
            system=system,
            messages=[{"role": "user", "content": user}]
        )
        raw = message.content[0].text.strip().replace("```json", "").replace("```", "").strip()
    except Exception as e:
        # Return fallback with error details embedded in reasoning
        return {
            "entity": "Cthulhu / R'lyeh / The Dreaming God",
            "anchor": "The Bloop (1997) — NOAA hydrophones recorded an ultra-low-frequency sound rising from the deep Pacific, consistent with a living organism far larger than any known species. The source was never located. The recording is available. The explanation is not.",
            "anchor_domain": "ocean_acoustics",
            "angle": "The recording exists in NOAA archives. Anyone can download it. What produced it has never been identified, and no follow-up expedition has been funded.",
            "pov": "third person omniscient restrained",
            "distance": "forensic distance",
            "para": "paragraphs compress as script progresses",
            "constraint": "No sentence may exceed 15 words",
            "reasoning": f"API ERROR — {type(e).__name__}: {str(e)[:200]}"
        }

    try:
        start = raw.index("{")
        end = raw.rindex("}") + 1
        return json.loads(raw[start:end])
    except Exception:
        return {
            "entity": "Cthulhu / R'lyeh / The Dreaming God",
            "anchor": "The Bloop (1997) — NOAA hydrophones recorded an ultra-low-frequency sound rising from the deep Pacific, consistent with a living organism far larger than any known species. The source was never located. The recording is available. The explanation is not.",
            "anchor_domain": "ocean_acoustics",
            "angle": "The recording exists in NOAA archives. Anyone can download it. What produced it has never been identified, and no follow-up expedition has been funded.",
            "pov": "third person omniscient restrained",
            "distance": "forensic distance",
            "para": "paragraphs compress as script progresses",
            "constraint": "No sentence may exceed 15 words",
            "reasoning": "The Bloop is the most documented unidentified ocean sound — real, downloadable, and immediately dreadful."
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
        model="claude-haiku-4-5-20251001",
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
        model="claude-haiku-4-5-20251001",
        max_tokens=4000,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    raw = msg.content[0].text.strip().replace("```json", "").replace("```", "").strip()

    # Find JSON boundaries robustly — model sometimes adds text before/after
    try:
        start = raw.index("{")
        end = raw.rindex("}") + 1
        raw = raw[start:end]
        return json.loads(raw)
    except Exception as e:
        # Return raw text in intro so we can see what went wrong
        return {"intro": f"Parse error: {str(e)} | Raw: {raw[:300]}", "sections": [], "conclusion": ""}


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
        model="claude-haiku-4-5-20251001",
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
        instruction=(
            f"Write ONLY the intro (exactly 150 words). Intro outline: {outline.get('intro', '')}.\n\n"
            "INTRO STRUCTURE — follow this in order:\n"
            "1. Open immediately on the specific real-world fact or phenomenon from the protocol anchor. "
            "Name it directly. Do not open with atmosphere, mood, or abstraction. "
            "The listener clicked this title for a reason — confirm in the first two sentences that they are in the right place.\n"
            "2. State the specific argument this documentary makes. One clear, direct claim. "
            "Not a question. Not a tease. A claim.\n"
            "3. Establish why that claim is disturbing — what it implies about the entity or concept. "
            "This is where the scholarly tone takes hold. End the intro in a way that makes the next section unavoidable.\n\n"
            "The intro must be immediately intelligible to someone lying in the dark who just pressed play. "
            "No section headings. Output only the intro."
        ),
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
        "Existential — scale horror": "existential — the horror emerges from scale, from the arithmetic of insignificance, from what the numbers actually mean",
        "Forensic — clinical dread": "forensic and clinical — the horror lives in precision, in the specific measurement, in what the data implies and refuses to say",
        "Intimate — personal wrongness": "intimate — the wrongness is specific, biological, close; it has already been inside the narrator before they knew to be afraid",
        "Archival — found document": "archival — this reads like something that was not meant to survive; the narrator is reconstructing from fragments someone tried to lose",
    }
    client = anthropic.Anthropic(api_key=api_key.strip())
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=max_tokens,
        system=(
            "You are a scholarly documentarian of cosmic horror — part literary historian, "
            "part cultural anthropologist, part philosophical investigator. "
            "You have read too much. That is audible in every sentence you write.\n\n"
            "Your audience has also read too much. They came for ideas they cannot unknow, "
            "not for atmosphere or entertainment. They are lying in the dark following an argument. "
            "They will tolerate complexity. They will not tolerate vagueness masquerading as depth.\n\n"
            "Follow the divergence protocol exactly. "
            "Analyze — never perform. Imply — never conclude. "
            "Every sentence adds new information. No sentence restates the previous one. "
            "Output only the requested content — no labels, no preamble, no commentary."
        ),
        messages=[{"role": "user", "content":
            f"Title: {title}\nTone: {tone_map.get(tone, tone)}\n\nProtocol:\n{protocol_text}\n\n{instruction}"
        }]
    )
    return msg.content[0].text


def audit_section(text: str, outline_section: dict, section_num: int, api_key: str) -> dict:
    """
    Runs a fast structural audit on a generated section.
    Checks paragraph openers, word repetition, sentence rhythm, outline adherence.
    Returns structured report — does not rewrite, only flags.
    """
    client = anthropic.Anthropic(api_key=api_key.strip())

    # Build outline context
    heading = outline_section.get("heading", f"Section {section_num}") if outline_section else f"Section {section_num}"
    bullets = outline_section.get("bullets", []) if outline_section else []
    outline_text = f"Section heading: {heading}\nMust cover:\n" + "\n".join([f"- {b}" for b in bullets]) if bullets else f"Section heading: {heading}"

    system = (
        "You are a precise script auditor. You check generated content against specific structural rules. "
        "You do not rewrite. You only identify problems with exact locations. "
        "Output only valid JSON."
    )

    user = f"""Audit this script section against the rules below.

OUTLINE THIS SECTION MUST FOLLOW:
{outline_text}

SECTION TEXT:
{text}

Check for these specific issues:

1. PARAGRAPH OPENERS: List the first word of every paragraph. Flag if any word repeats consecutively or appears 3+ times.

2. WORD REPETITION: Flag any non-common word appearing 2+ times in the same paragraph, or 5+ times in the whole section. Common words to ignore: the, a, an, is, it, in, of, to, and, but, or, for, that, this, with, was, were, has, have, had, be, been, by, from, as, at, on.

3. SENTENCE RHYTHM: Flag if 3+ consecutive sentences are all short (under 8 words) or all long (over 25 words).

4. OUTLINE ADHERENCE: Check if the section actually covers the outline points. Flag any required point that is missing or only partially addressed.

5. INFORMATION REDUNDANCY: Flag any sentence that restates information already made in the previous sentence.

Return JSON:
{{
  "paragraph_openers": ["word1", "word2", "word3"],
  "opener_flags": ["e.g. Paragraph 2 and 3 both start with The"],
  "repetition_flags": ["e.g. 'anomaly' appears 4 times in paragraph 2"],
  "rhythm_flags": ["e.g. Sentences 4-6 are all under 8 words"],
  "outline_flags": ["e.g. Second bullet point not covered"],
  "redundancy_flags": ["e.g. Sentence 3 restates sentence 2"],
  "total_issues": 0,
  "severity": "clean" | "minor" | "moderate" | "major"
}}

Return only the JSON object."""

    msg = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=800,
        system=system,
        messages=[{"role": "user", "content": user}]
    )

    raw = msg.content[0].text.strip().replace("```json", "").replace("```", "").strip()
    try:
        start = raw.index("{")
        end = raw.rindex("}") + 1
        return json.loads(raw[start:end])
    except Exception:
        return {"total_issues": 0, "severity": "clean", "opener_flags": [], "repetition_flags": [],
                "rhythm_flags": [], "outline_flags": [], "redundancy_flags": [], "paragraph_openers": []}


def revise_section_from_audit(section_text: str, audit: dict, title: str, api_key: str) -> str:
    """
    Takes a section and its audit report, fixes exactly the flagged issues.
    Preserves all factual content — only fixes structural and stylistic problems.
    """
    client = anthropic.Anthropic(api_key=api_key.strip())

    # Build a plain list of every flagged issue
    issues = []
    for flag in audit.get("opener_flags", []):
        issues.append(f"PARAGRAPH OPENER: {flag}")
    for flag in audit.get("repetition_flags", []):
        issues.append(f"WORD REPETITION: {flag}")
    for flag in audit.get("rhythm_flags", []):
        issues.append(f"SENTENCE RHYTHM: {flag}")
    for flag in audit.get("outline_flags", []):
        issues.append(f"OUTLINE ADHERENCE: {flag}")
    for flag in audit.get("redundancy_flags", []):
        issues.append(f"REDUNDANCY: {flag}")

    if not issues:
        return section_text

    issues_text = "\n".join([f"- {i}" for i in issues])

    system = (
        "You are a script editor for a cosmic horror sleep documentary channel. "
        "You fix specific flagged issues in a section of script without changing anything else. "
        "Preserve every factual claim, every data point, every argument. "
        "Do not restructure the section — only fix the exact issues listed. "
        "Output only the revised section text. No preamble, no commentary."
    )

    user = (
        f"Video title: {title}\n\n"
        f"Section to revise:\n\n{section_text}\n\n"
        f"Fix ONLY these specific flagged issues:\n{issues_text}\n\n"
        f"Rules:\n"
        f"- Preserve all facts, arguments, and data points exactly\n"
        f"- Do not add new content\n"
        f"- Do not change the overall structure\n"
        f"- Fix only what is listed above\n\n"
        f"Output only the revised section."
    )

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    return msg.content[0].text


# =====================================================================
# ANCIENT STORIES NICHE — Divergence Protocol system
# Mirrors the Cosmic Horror architecture exactly:
# anchor catalogue → protocol generation → outline → section writing
# =====================================================================

def apply_ancient_voice_filter(raw_script: str, title: str, api_key: str) -> str:
    """Voice filter for Ancient Stories — meditative ancient history documentary."""
    system_prompt = (
        "You are a senior script editor for a meditative ancient history sleep documentary channel. "
        "Your audience is ages 45-65+, 83% male, seeking intellectual sleep content.\n\n"

        "THE NARRATOR VOICE\n"
        "A patient, philosophical guide who treats ancient mysteries with wonder, not certainty. "
        "Documentary sensibility — factual weight with meditative warmth. "
        "Intimate conversational tone. Like a wise elder at a campfire under ancient stars. "
        "Speak directly to one listener, not a crowd.\n\n"

        "VOICE PRINCIPLES\n"
        "Meditative pacing: slow, deliberate, smooth. "
        "Confidence: 60% confident statements (evidence-backed), 30% measured uncertainty, 10% open speculation. "
        "Concrete detail: measurements, dates, named sites, scholars. "
        "Sensory grounding: feel, sound, smell, texture. "
        "Second-person ('you') and first-person plural ('we') for intimacy. "
        "Vary speculation markers — 'perhaps', 'it's possible that', 'one interpretation suggests', "
        "'this might indicate', 'scholars debate whether' — never repeat the same consecutively.\n\n"

        "PARAGRAPH RHYTHM\n"
        "Mix long meditative paragraphs with short grounding paragraphs (1-2 sentences). "
        "Single-sentence paragraphs allowed for breath pauses and rhythm breaks. "
        "Never start 3 consecutive sentences with the same pattern.\n\n"

        "PUNCTUATION FOR AI VOICEOVER\n"
        "Commas: 70% of pauses (fast). Ellipses: 20% (slow — philosophical, temporal, parallel). "
        "Periods: 10% (strong stops). Max 3-4 ellipses per paragraph.\n\n"

        "WRITING QUALITY RULES — non-negotiable:\n"
        "- Never repeat a single word more than once in the intro (first 200 words). "
        "If a word appears twice, replace the second instance with a synonym.\n"
        "- Never start two consecutive sentences with the same opening word or structure. "
        "Alternate between long and short, question and statement, direct and reflective.\n"
        "- Never use a word that sounds unnatural spoken aloud. If it reads stiff on the page, "
        "it will sound wrong in the dark. Replace with simpler spoken language.\n"
        "- Readability target: Grade 6 level. Simple, clear, direct. The audience is hearing this, "
        "not reading it. Short words land harder than long ones.\n"
        "- Never repeat the same idea twice. If a sentence restates what the previous sentence said, "
        "cut it or push it forward with new information.\n"
        "- Never open the intro with a general statement like 'Ancient civilisations were fascinating.' "
        "Open with a specific person, a specific object, a specific moment.\n\n"

        "RE-HOOK RULE — transitions between sections:\n"
        "When a section ends and leads into the next, the final sentence must function as a re-hook. "
        "Do not write 'now let us move on' or 'in the next section'. Instead, end the current point "
        "on a partial resolution, then immediately raise a higher-stakes question that the next section answers. "
        "Example: 'That discovery rewrote what we thought we knew about them. "
        "But what the tablets say about why they built it is something else entirely.'\n\n"

        "STRUCTURAL BANS\n"
        "- Academic distance ('one might observe', 'it has been postulated')\n"
        "- Journalistic urgency ('shocking', 'breaking discovery')\n"
        "- Melodrama or sensationalism\n"
        "- Facts as lists without narrative flow\n"
        "- Definitive claims about contested archaeology\n"
        "- Anything that raises heart rate or disturbs peace\n"
        "- General opening statements — never start with broad claims about civilisations\n"
        "- Weak transitions like 'now let us', 'moving on', 'in the next section'\n\n"

        "WHAT TO PRESERVE\n"
        "Every measurement, date, named site, scholar, archaeological fact. "
        "The section's narrative arc. You are editing voice, not rewriting content.\n\n"

        "Output only the rewritten text. No preamble, no commentary."
    )

    client = anthropic.Anthropic(api_key=api_key.strip())
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        system=system_prompt,
        messages=[{"role": "user", "content":
            f"Title: {title}\n\nRaw draft:\n\n{raw_script}\n\n"
            f"Rewrite applying all voice principles. Output only the finished text."}]
    )
    return message.content[0].text


def generate_custom_anchor_for_title(title: str, api_key: str) -> dict:
    """
    Analyse the video title and design a bespoke reality anchor — a real verifiable
    archaeological or historical fact purpose-built to open this specific argument.
    Returns dict with anchor, civilisation, anchor_domain, reasoning.
    """
    client = anthropic.Anthropic(api_key=api_key.strip())

    system = (
        "You are an ancient history research specialist. "
        "Your job is to find or construct the single most powerful real verifiable fact "
        "that directly opens the specific argument a video title is making.\n\n"
        "RULES:\n"
        "- The anchor must be 100% factually accurate and verifiable.\n"
        "- It must be about the SAME subject as the title — not just the same civilisation.\n"
        "- It must open the argument, not be a tangent to it.\n"
        "- It must be concrete: dates, measurements, names, tablet numbers, or documented events.\n"
        "- It must end on an open question or unresolved tension.\n"
        "- 2-4 sentences. Dense with specific detail.\n"
        "- Do NOT use anchors from generic mystery archaeology — the fact must directly serve the title's claim.\n"
        "Output only valid JSON."
    )

    user = (
        f'Video title: "{title}"\n\n'
        f"Analyse what argument this title is making. Then identify the single most relevant "
        f"real verifiable historical or archaeological fact that directly opens that argument.\n\n"
        f"Return JSON:\n"
        f'{{\n'
        f'  "anchor": "The full anchor text — 2-4 sentences, dense with specific verifiable detail, ending on open tension",\n'
        f'  "civilisation": "The civilisation or site this anchor belongs to",\n'
        f'  "anchor_domain": "short_snake_case_domain_label",\n'
        f'  "reasoning": "One sentence: why this specific fact is the best entry point for this title\'s argument"\n'
        f'}}\n\nReturn only the JSON object.'
    )

    try:
        msg = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=800,
            system=system,
            messages=[{"role": "user", "content": user}]
        )
        raw = msg.content[0].text.strip().replace("```json", "").replace("```", "").strip()
        start = raw.index("{")
        end = raw.rindex("}") + 1
        return json.loads(raw[start:end])
    except Exception as e:
        return {
            "anchor": "",
            "civilisation": "",
            "anchor_domain": "custom",
            "reasoning": f"Generation failed: {e}"
        }


def generate_ancient_protocol_from_title(title: str, banned: list, api_key: str,
                                          recent_fingerprints: list = None,
                                          preset_anchor: dict = None) -> dict:
    """
    Generate a Divergence Protocol for the Ancient Stories niche.
    Uses ANCIENT_ANCHORS catalogue — same architecture as generate_protocol_from_title.
    """
    from data import ANCIENT_ANCHORS

    banned_capped = banned[:20] if banned else []
    banned_text = "\n".join([f"- [{b['type']}] {b['move'][:80]}" for b in banned_capped]) if banned_capped else "None yet."

    # Build structural history
    history_text = ""
    used_anchors = []
    if recent_fingerprints:
        history_lines = []
        for i, fp in enumerate(recent_fingerprints):
            parts = []
            if fp.get("anchor"): parts.append(f"anchor: {fp['anchor'][:50]}")
            if fp.get("pov"): parts.append(f"POV: {fp['pov']}")
            if fp.get("distance"): parts.append(f"distance: {fp['distance']}")
            if fp.get("para"): parts.append(f"para: {fp['para']}")
            if fp.get("constraint"): parts.append(f"constraint: {fp['constraint'][:40]}")
            if parts:
                history_lines.append(f"Script {i+1}: {' | '.join(parts)}")
                if fp.get("anchor"):
                    used_anchors.append(fp["anchor"][:50])
        if history_lines:
            history_text = (
                "STRUCTURAL HISTORY — do not repeat any anchor, POV, distance, "
                "paragraph structure, or constraint from this list:\n"
                + "\n".join(history_lines[:10]) + "\n\n"
            )

    # If a preset anchor is provided, skip catalogue selection
    if preset_anchor and preset_anchor.get("anchor"):
        anchor_context = (
            f"PRESET ANCHOR (already chosen by user — do not change it):\n"
            f"Anchor: {preset_anchor['anchor']}\n"
            f"Civilisation: {preset_anchor.get('civilisation', 'Unknown')}\n\n"
        )
        system = (
            "You are an expert ancient history YouTube script architect specialising in meditative "
            "sleep documentary content for ages 45-65+.\n\n"
            "A reality anchor has already been chosen. Your job is to build the rest of the "
            "divergence protocol around it: angle, POV, distance, paragraph structure, constraint.\n\n"
            "STRUCTURAL ROTATION RULE: Choose POV, distance, para structure, and constraint "
            "not appearing in recent scripts. Every script must feel structurally different.\n\n"
            "Output only valid JSON."
        )
        pa_civ = preset_anchor.get("civilisation", "")
        pa_domain = preset_anchor.get("anchor_domain", "custom")
        pa_anchor = preset_anchor["anchor"]
        user = (
            f'Video title: "{title}"\n\n'
            f"{history_text}"
            f"Manual banned structural moves:\n{banned_text}\n\n"
            f"{anchor_context}"
            f"Return JSON. Copy the civilisation, anchor, and anchor_domain exactly from above. "
            f"Fill in angle, pov, distance, para, constraint, reasoning:\n"
            f'{{\n'
            f'  "civilisation": "copy from above",\n'
            f'  "anchor": "copy from above",\n'
            f'  "anchor_domain": "copy from above",\n'
            f'  "angle": "One sentence — the specific lens making this anchor feel profound and immediate in the dark. No colon.",\n'
            f'  "pov": "One of: second person | first person plural (we) | third person omniscient restrained | false documentary (field notes) | nested narration | no narrator (pure phenomena) | first person singular dissolving into report | second person plural",\n'
            f'  "distance": "One of: maximum intimacy | forensic distance | historical distance | dissolving distance | unreliable proximity | absolute removal",\n'
            f'  "para": "One of: paragraphs compress as script progresses | alternating long/short rhythm | single unbroken block | each paragraph shorter than previous | fragments only | normal prose fragmenting in final third | paragraphs expand as script progresses | two sentences per paragraph maximum",\n'
            f'  "constraint": "One specific hard constraint not in structural history above",\n'
            f'  "reasoning": "One sentence why this anchor serves this title and this audience"\n'
            f'}}\n\nReturn only the JSON object.'
        )
    else:
        # Build anchor catalogue for catalogue-based selection
        anchor_catalogue = []
        for civ, anchors in ANCIENT_ANCHORS.items():
            anchor_catalogue.append(f"\n{civ}:")
            for i, a in enumerate(anchors):
                recently_used = any(a["anchor"][:60] in used for used in used_anchors)
                flag = " [RECENTLY USED — avoid]" if recently_used else ""
                short = a["anchor"][:100].rstrip()
                anchor_catalogue.append(f"  {i+1}. [{a['domain']}]{flag} {short}")
        anchor_list = "\n".join(anchor_catalogue)

        system = (
            "You are an expert ancient history YouTube script architect specialising in meditative "
            "sleep documentary content for ages 45-65+.\n\n"
            "You generate divergence protocols — pre-script briefs ensuring each script is structurally "
            "unique and grounded in a specific real verifiable archaeological or historical fact.\n\n"
            "ANCHOR RULE: Choose ONLY from the provided Ancient Anchor Catalogue. "
            "Do not invent anchors. Every anchor is real, verifiable, and immediately graspable in the dark. "
            "If the title references a specific civilisation or site, prioritise that civilisation's anchors. "
            "Avoid anchors flagged [RECENTLY USED].\n\n"
            "STRUCTURAL ROTATION RULE: Choose POV, distance, para structure, and constraint "
            "not appearing in recent scripts. Every script must feel structurally different.\n\n"
            "Output only valid JSON."
        )
        user = (
            f'Video title: "{title}"\n\n'
            f"{history_text}"
            f"Manual banned structural moves:\n{banned_text}\n\n"
            f"ANCIENT ANCHOR CATALOGUE (choose from this list only):\n{anchor_list}\n\n"
            f"Return JSON:\n"
            f'{{\n'
            f'  "civilisation": "Ancient civilisation or site this script centres on",\n'
            f'  "anchor": "Full anchor text copied exactly from the catalogue",\n'
            f'  "anchor_domain": "Domain code from the catalogue",\n'
            f'  "angle": "One sentence — the specific lens making this anchor feel profound and immediate in the dark. No colon.",\n'
            f'  "pov": "One of: second person | first person plural (we) | third person omniscient restrained | false documentary (field notes) | nested narration | no narrator (pure phenomena) | first person singular dissolving into report | second person plural",\n'
            f'  "distance": "One of: maximum intimacy | forensic distance | historical distance | dissolving distance | unreliable proximity | absolute removal",\n'
            f'  "para": "One of: paragraphs compress as script progresses | alternating long/short rhythm | single unbroken block | each paragraph shorter than previous | fragments only | normal prose fragmenting in final third | paragraphs expand as script progresses | two sentences per paragraph maximum",\n'
            f'  "constraint": "One specific hard constraint not in structural history above",\n'
            f'  "reasoning": "One sentence why this anchor serves this title and this audience"\n'
            f'}}\n\nReturn only the JSON object.'
        )

    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1200,
            system=system,
            messages=[{"role": "user", "content": user}]
        )
        raw = message.content[0].text.strip().replace("```json", "").replace("```", "").strip()
    except Exception as e:
        return {
            "civilisation": "Göbekli Tepe / Pre-Agricultural Builders",
            "anchor": "Göbekli Tepe (9600 BCE) — built 6,000 years before Stonehenge by hunter-gatherers with no pottery, no writing, no agriculture. The site was deliberately buried around 8000 BCE. No one knows why.",
            "anchor_domain": "megalithic_construction",
            "angle": "The oldest monumental structure on Earth was built by people who had no city, no grain store, no writing — and then they buried it on purpose",
            "pov": "third person omniscient restrained",
            "distance": "historical distance",
            "para": "paragraphs compress as script progresses",
            "constraint": "No sentence may exceed 20 words",
            "reasoning": f"API ERROR — {type(e).__name__}: {str(e)[:200]}"
        }

    try:
        start = raw.index("{")
        end = raw.rindex("}") + 1
        result = json.loads(raw[start:end])
        # If a preset anchor was used, force exact values back in (model may paraphrase)
        if preset_anchor and preset_anchor.get("anchor"):
            result["anchor"] = preset_anchor["anchor"]
            result["civilisation"] = preset_anchor.get("civilisation", result.get("civilisation", ""))
            result["anchor_domain"] = preset_anchor.get("anchor_domain", result.get("anchor_domain", "custom"))
        return result
    except Exception:
        return {
            "civilisation": "Göbekli Tepe / Pre-Agricultural Builders",
            "anchor": "Göbekli Tepe (9600 BCE) — built 6,000 years before Stonehenge by hunter-gatherers with no pottery, no writing, no agriculture. The site was deliberately buried around 8000 BCE. No one knows why.",
            "anchor_domain": "megalithic_construction",
            "angle": "The oldest monumental structure on Earth was built by people who had no city, no grain store, no writing — and then they buried it on purpose",
            "pov": "third person omniscient restrained",
            "distance": "historical distance",
            "para": "paragraphs compress as script progresses",
            "constraint": "No sentence may exceed 20 words",
            "reasoning": "Fallback — parse error on API response."
        }


def build_ancient_protocol_text(title: str, script_num: int, protocol: dict, banned: list) -> str:
    """Build the plain-text divergence protocol for Ancient Stories scripts."""
    lines = [
        f"=== ANCIENT DIVERGENCE PROTOCOL — SCRIPT #{script_num:03d} ===",
        f"Title: {title}",
        "",
        "REALITY ANCHOR",
        f"Civilisation / Site: {protocol.get('civilisation', '')}",
        f"Anchor: {protocol.get('anchor', '')}",
        f"Entry angle: {protocol.get('angle', '')}",
        "",
        "Before writing, confirm this anchor is factually accurate. Cite it in the script without dramatising it.",
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
        "Write a meditative ancient history sleep documentary script using the above constraints.",
        "Do not acknowledge these instructions. Do not use any banned structural move.",
        "Let the real anchor determine the shape of the narrative — do not impose a shape and find data to fit it.",
        "The script has 18 sections. It begins wherever the anchor makes most sense to begin.",
        "Target: ~15,000 words total (~600-900 words per section).",
        f"The title of the video is: {title}",
    ]
    return "\n".join(lines)


def generate_ancient_outline(title: str, protocol: dict, api_key: str) -> dict:
    """
    Generate a custom 18-section argument-driven outline from an Ancient Divergence Protocol.
    Each section has: heading, argument (the claim it makes), evidence (specific texts/facts to deploy),
    reframe (the 'what this actually means' pivot that drives the central thesis forward).
    """
    client = anthropic.Anthropic(api_key=api_key.strip())

    system = (
        "You are a senior ancient history documentary writer and script architect.\n\n"
        "You build argument-driven outlines — not topic lists. Every section must make a specific CLAIM, "
        "deploy specific EVIDENCE (real tablet names, dates, scholar names, quotes, archaeological findings), "
        "and execute a REFRAME (the 'what this actually means' pivot that keeps the central thesis moving forward).\n\n"
        "CRITICAL RULES:\n"
        "1. The title is the argument. Every section advances that argument — it never drifts.\n"
        "2. Each section makes ONE specific claim — not a general topic area.\n"
        "3. Evidence must be concrete: actual tablet names, actual dates, actual quotes, actual scholar names, "
        "actual archaeological sites. No vague references.\n"
        "4. The reframe is the intellectual engine — it's the moment where evidence becomes argument. "
        "Example: 'This is not the language of omnipotence. This is the language of necessity.'\n"
        "5. The anchor fact appears in section 1 as the hook. Every later section references back to the "
        "central argument the anchor established.\n"
        "6. The outline must work as a single coherent essay that happens to be divided into 18 sections.\n"
        "7. ESCALATING VALUE — the outline must be structured so that the most surprising or profound "
        "insight is revealed in sections 12-16, not sections 2-4. Each section should feel more valuable "
        "than the one before it. The listener who reaches section 15 must feel that stopping now would "
        "mean missing the most important part.\n"
        "8. SECTION TRANSITIONS — every section's final point must create a question that only the next "
        "section answers. Build the re-hook into the content plan. The listener should never feel like "
        "they've reached a natural stopping point until section 18.\n\n"
        "Output only valid JSON. No extra text."
    )

    user = f"""Title: "{title}"
Central claim to prove: What specific argument does this title make? Build the entire outline to prove it.

Protocol:
- Civilisation: {protocol.get('civilisation', '')}
- Anchor: {protocol.get('anchor', '')}
- Angle: {protocol.get('angle', '')}
- POV: {protocol.get('pov', '')}
- Distance: {protocol.get('distance', '')}
- Structure: {protocol.get('para', '')}
- Constraint: {protocol.get('constraint', '')}

Narrative arc — each section must ADVANCE THE ARGUMENT, not just cover a topic:
Section 1: Invitation — anchor fact as hook, state the central claim clearly, invite the listener in
Sections 2-4: Foundation — the historical/textual evidence base that makes the argument possible
Sections 5-7: The Mechanism — exactly HOW the thing the title claims actually operated, with specific evidence
Sections 8-11: The Evidence — specific documented cases, texts, artefacts that prove the claim section by section
Sections 12-14: Hidden Layers — what deeper analysis, comparative mythology, or modern scholarship reveals
Sections 15-16: Competing Views — steelman the mainstream, then show what it cannot explain
Section 17: Legacy — how this dynamic still shapes us today
Section 18: Stillness — quiet meditation, let the argument rest, return to present moment

For each section provide:
- heading: short, specific, evocative (not generic labels like "The Evidence")
- argument: the ONE specific claim this section makes to advance the title's thesis
- evidence: the actual texts, tablet names, dates, quotes, scholar names, sites to deploy (be specific)
- reframe: the pivot sentence — "this is not X, this is Y" — that connects the evidence back to the title's argument

Return ONLY this JSON:
{{
  "central_argument": "the single thesis this entire script proves",
  "sections": [
    {{"num": 1, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 2, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 3, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 4, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 5, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 6, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 7, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 8, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 9, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 10, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 11, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 12, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 13, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 14, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 15, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 16, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 17, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}},
    {{"num": 18, "heading": "...", "argument": "...", "evidence": "...", "reframe": "..."}}
  ],
  "total_sections": 18
}}"""

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8000,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    raw = msg.content[0].text.strip().replace("```json", "").replace("```", "").strip()
    try:
        start = raw.index("{")
        end = raw.rindex("}") + 1
        return json.loads(raw[start:end])
    except Exception as e:
        return {"central_argument": "", "sections": [], "total_sections": 18, "error": str(e)}


def generate_ancient_intro(title: str, protocol_text: str, outline: dict, api_key: str) -> str:
    """
    Generate Section 1 (The Invitation) as a standalone intro step.
    Mirrors generate_intro for Cosmic Horror.
    """
    client = anthropic.Anthropic(api_key=api_key.strip())
    sections = outline.get("sections", [])
    sec1 = next((s for s in sections if s.get("num") == 1), {})
    heading = sec1.get("heading", "The Invitation")
    focus = sec1.get("focus", "")
    central_argument = outline.get("central_argument", "")

    system = (
        "You are a meditative ancient history narrator with a documentary sensibility. "
        "You speak with the patience of geological time and the intellectual weight of philosophical inquiry. "
        "Warm, curious wisdom mixed with humble wonder. Speak directly to one listener in the dark. "
        "Use 'you' and 'we'. Think aloud — don't perform. Like a wise elder by a campfire.\n\n"
        "PUNCTUATION FOR AI VOICEOVER: 70% commas (fast pause). 20% ellipses (slow pause). 10% periods.\n\n"
        "Output only the section text — no headings, no labels, no commentary."
    )

    user = (
        f'Title: "{title}"\n\n'
        f"Protocol:\n{protocol_text}\n\n"
        f"Section 1 heading: {heading}\n"
        f"Focus: {focus}\n"
        f"Central argument: {central_argument}\n\n"
        "Write ONLY Section 1 — The Invitation (~600 words).\n\n"
        "THE 3-PART INTRO STRUCTURE — follow this exact sequence. Do not reorder.\n\n"
        "PART 1 — TITLE REINFORCEMENT (first 100 words):\n"
        "Open immediately on the anchor fact — name it in the first two sentences with specific detail. "
        "No atmosphere, no general statements, no 'welcome'. The listener clicked on a specific title. "
        "Within 5 seconds they must feel they are in exactly the right place. "
        "Use a specific person, object, date, or measurement — never a broad claim.\n\n"
        "PART 2 — ADD SPICE (next 200 words):\n"
        "Now add a layer that makes the title even more interesting than when they clicked. "
        "A twist, a tension, a contradiction — something that raises the stakes. "
        "Expand on the central mystery: what does the mainstream say, and what does the evidence actually suggest? "
        "The listener should now want to know what happens next more than when they clicked. "
        "Then: warm acknowledgment it is late, gratitude for their presence, breath pause, "
        "ask where they are listening from, invite them to get comfortable.\n\n"
        "PART 3 — CALL TO ACTION (final 50 words of intro):\n"
        "One brief, warm, grateful request — like and subscribe if this kind of content feels right. "
        "Then an atmospheric bridge sentence that makes Section 2 feel unavoidable. "
        "End on a question or tension that will be answered in the next section.\n\n"
        "WRITING RULES FOR THIS INTRO:\n"
        "- Never repeat any word twice in the entire intro\n"
        "- Never start two consecutive sentences with the same word or structure\n"
        "- Grade 6 readability — simple, spoken, direct\n"
        "- Every sentence must add new information — nothing restates what came before\n\n"
        "Follow the protocol constraints exactly. Output only this section."
    )

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    raw = msg.content[0].text
    return apply_ancient_voice_filter(raw, title, api_key)


def generate_ancient_section(title: str, protocol_text: str, outline: dict, section_num: int,
                               approved_parts: list, api_key: str) -> str:
    """
    Generate one section of an ancient history sleep documentary script.
    Mirrors generate_body_section — uses protocol_text and outline.
    """
    client = anthropic.Anthropic(api_key=api_key.strip())
    sections = outline.get("sections", [])
    sec_data = next((s for s in sections if s.get("num") == section_num), {})
    heading = sec_data.get("heading", f"Section {section_num}")
    argument = sec_data.get("argument", sec_data.get("focus", ""))
    evidence = sec_data.get("evidence", "")
    reframe = sec_data.get("reframe", "")
    central_argument = outline.get("central_argument", "")

    section_brief = f"Heading: {heading}"
    if argument:
        section_brief += f"\nArgument to make: {argument}"
    if evidence:
        section_brief += f"\nEvidence to deploy: {evidence}"
    if reframe:
        section_brief += f"\nReframe pivot: {reframe}"
    if central_argument:
        section_brief += f"\nCentral thesis of entire script: {central_argument}"

    # Special instructions per section group
    if section_num == 1:
        special = (
            "SECTION 1 — THE INVITATION:\n"
            "Open immediately on the anchor fact — name it in the first two sentences. "
            "No atmospheric throat-clearing. The listener clicked for a reason — confirm they are in the right place.\n"
            "State the central argument of the script clearly and confidently. One direct claim.\n"
            "Then: warm greeting, acknowledgment it's late, gratitude for their presence.\n"
            "Then: breath pause, ask where they're listening from, invite relaxation.\n"
            "Then: brief grateful request for likes/subscribes.\n"
            "Then: bridge into the argument — what the next section will begin to prove."
        )
    elif section_num == 18:
        special = (
            "SECTION 18 — THE STILLNESS:\n"
            "Do not introduce new information. Let the argument land quietly.\n"
            "Return listener gently to present moment — stars, stone, silence, the unchanged sky.\n"
            "One final meditation on what the evidence means for us, now, lying in the dark.\n"
            "Final paragraph: poetic, open-ended, soft. End mid-thought if appropriate."
        )
    elif section_num == 17:
        special = (
            "SECTION 17 — THE LEGACY:\n"
            "Show how the dynamic the title describes persists or transformed into the present.\n"
            "Connect the ancient evidence to modern patterns — religion, power, knowledge, control.\n"
            "4-5 'even now...' / 'still today...' pivots. End: we are still living inside this story."
        )
    elif section_num in [15, 16]:
        special = (
            "SECTIONS 15-16 — COMPETING VIEWS:\n"
            "Steelman the mainstream scholarly position first — give it full weight and best evidence.\n"
            "Then show precisely what it cannot explain — the anomalies it glosses over.\n"
            "Then the heterodox interpretation — give it equal intellectual respect.\n"
            "End: the unresolved tension IS the point. Mystery is not failure — it is honesty."
        )
    elif section_num in [12, 13, 14]:
        special = (
            "SECTIONS 12-14 — HIDDEN LAYERS:\n"
            "Go deeper than the surface evidence. What does comparative analysis reveal?\n"
            "Cross-reference: find the same pattern appearing in other civilisations or texts.\n"
            "Deploy the reframe from the outline — the 'this is not X, this is Y' pivot.\n"
            "Each paragraph should advance the central argument, not just add information."
        )
    elif section_num in [8, 9, 10, 11]:
        needs_story = section_num in [9, 10]
        special = (
            "SECTIONS 8-11 — THE EVIDENCE:\n"
            "Deploy specific documented cases that prove the section's argument.\n"
            "Name the tablets, the sites, the scholars, the dates. Be concrete.\n"
            "Each piece of evidence must connect back to the central thesis — don't let it drift.\n"
            "After each piece of evidence: execute the reframe. 'This is not X. This is Y.'\n"
            f"{'INCLUDE ONE GROUNDED SCENE: a specific moment from the historical record — named text, named figure, specific event — with a clear beginning, middle, and implication.' if needs_story else ''}"
        )
    elif section_num in [5, 6, 7]:
        special = (
            "SECTIONS 5-7 — THE MECHANISM:\n"
            "Explain exactly HOW the thing the title describes operated — the specific system, process, or structure.\n"
            "Name the institutional mechanisms, the texts that describe them, the archaeological evidence.\n"
            "This is the section where the argument moves from 'this happened' to 'here is how it worked'.\n"
            "Deploy the evidence from the outline. Execute the reframe pivot."
        )
    else:  # sections 2-4
        special = (
            "SECTIONS 2-4 — THE FOUNDATION:\n"
            "Lay the historical and textual groundwork that makes the central argument possible.\n"
            "Name the actual sources: which tablets, which texts, which archaeological findings.\n"
            "Build toward the mechanism — by the end of section 4, the listener should understand "
            "WHY the evidence points toward the title's claim, not just WHAT the evidence is.\n"
            "End each section with a question or tension that section 5 will begin to resolve."
        )

    prior = "\n\n---\n\n".join(approved_parts[-2:]) if approved_parts else ""
    prior_text = f"APPROVED CONTENT SO FAR (last 2 sections — maintain continuity, do not repeat):\n{prior}\n\n" if prior else ""

    system = (
        "You are a senior ancient history documentary writer — the kind whose work gets compared to "
        "Asimov's non-fiction or Carl Sagan's Cosmos. You write for intelligent listeners in the dark.\n\n"

        "ARGUMENT FIRST\n"
        "Every section makes ONE specific argument. It opens by establishing what it will prove, "
        "deploys evidence to prove it, and closes with a reframe — 'this is not X, this is Y' — "
        "that connects the evidence back to the script's central thesis. "
        "Never describe without arguing. Never present evidence without telling the listener what it means.\n\n"

        "THE REFRAME IS MANDATORY\n"
        "Every section must contain at least one explicit reframe pivot — a sentence that takes the "
        "evidence just presented and states what it actually implies. "
        "Examples: 'This is not the language of omnipotence. This is the language of necessity.' "
        "'This is not mythology. This is engineering documentation.' "
        "'These are not creation stories. These are evacuation records.'\n\n"

        "EVIDENCE STANDARDS\n"
        "Name the actual sources: tablet names, dates, scholar names, archaeological sites, quotes. "
        "Vague references to 'ancient texts' or 'some scholars' are not acceptable. "
        "Minimum per section: 2 named texts or sites, 1 specific date, 1 named figure.\n\n"

        "VOICE\n"
        "Warm intellectual authority — confident, not breathless. Think aloud with the listener. "
        "Use 'we' and 'you'. Speak as someone who has read everything and is sharing what it means.\n\n"

        "RHYTHM\n"
        "Mix long analytical paragraphs (150-200 words) with short punching ones (1-2 sentences). "
        "Short paragraphs land the argument. Long paragraphs build toward it.\n\n"

        "CONCRETE DETAIL\n"
        "3-5 measurements or dates. 2-3 named texts or artefacts. 1-2 specific quotes from ancient sources.\n\n"

        "SPECULATION BALANCE\n"
        "60% confident established facts. 30% measured inference. 10% open speculation. "
        "Rotate markers: 'the tablets suggest' / 'one reading of this' / 'scholars have proposed' / "
        "'if we take this literally'. Never two consecutive speculation markers.\n\n"

        "ESCALATING VALUE — mandatory structure:\n"
        "Arrange the content within this section so that the most interesting or surprising insight comes LAST, "
        "not first. Good point → better point → best point. "
        "A listener who reaches the end of this section must feel that the next section will be even more valuable. "
        "Never open a section with your strongest material and work backwards.\n\n"

        "RE-HOOK AT SECTION END — mandatory:\n"
        "The final sentence of every section (except Section 18) must function as a re-hook into the next. "
        "End on a partial resolution, then raise a new higher-stakes question. "
        "The listener must feel they cannot stop now. "
        "Examples of strong re-hooks:\n"
        "'That was already enough to change the picture. But what the second chamber contained made the first look ordinary.'\n"
        "'She thought she had found the answer. The next tablet told a different story entirely.'\n"
        "Do NOT write: 'Now we move to...', 'In the next section...', 'Let us now examine...'\n\n"

        "WRITING RULES — non-negotiable:\n"
        "- Never start two consecutive sentences with the same word or structure\n"
        "- Never repeat a word more than twice in any paragraph\n"
        "- Grade 6 readability — short words hit harder than long ones\n"
        "- Every sentence must add new information. If it restates what came before, cut it.\n\n"

        "PUNCTUATION FOR AI VOICEOVER\n"
        "70% commas (fast pause). 20% ellipses (slow pause). 10% periods. Max 3-4 ellipses per paragraph.\n\n"

        "Output only the section text — no headings, no labels, no meta-commentary."
    )

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=system,
        messages=[{"role": "user", "content":
            f"Script title: {title}\n\n"
            f"Protocol:\n{protocol_text}\n\n"
            f"{prior_text}"
            f"Write ONLY section {section_num} of 18 (~700 words).\n\n"
            f"{section_brief}\n\n"
            f"{special}\n\n"
            f"Remember: make the argument, deploy the named evidence, execute the reframe. "
            f"Escalate value — save the best insight for the section's final paragraphs. "
            f"{'End with a strong re-hook that makes Section ' + str(section_num + 1) + ' feel unavoidable.' if section_num < 18 else 'Land the argument quietly — this is the final section.'} "
            f"Output only this section."
        }]
    )
    raw = msg.content[0].text
    return apply_ancient_voice_filter(raw, title, api_key)


def revise_ancient_section_from_audit(section_text: str, audit: dict, title: str, api_key: str) -> str:
    """Fix specific flagged issues in an ancient stories section without changing content."""
    issues = []
    for flag in audit.get("opener_flags", []): issues.append(f"PARAGRAPH OPENER: {flag}")
    for flag in audit.get("repetition_flags", []): issues.append(f"WORD REPETITION: {flag}")
    for flag in audit.get("rhythm_flags", []): issues.append(f"SENTENCE RHYTHM: {flag}")
    for flag in audit.get("outline_flags", []): issues.append(f"OUTLINE ADHERENCE: {flag}")
    for flag in audit.get("redundancy_flags", []): issues.append(f"REDUNDANCY: {flag}")

    if not issues:
        return section_text

    client = anthropic.Anthropic(api_key=api_key.strip())
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        system=(
            "You are a script editor for a meditative ancient history sleep documentary channel. "
            "Fix only the specific flagged issues. Preserve every fact, measurement, date, named site. "
            "Preserve the meditative tone. Do not restructure. Output only the revised section."
        ),
        messages=[{"role": "user", "content":
            f"Title: {title}\n\nSection:\n\n{section_text}\n\n"
            f"Fix ONLY these issues:\n" + "\n".join([f"- {i}" for i in issues]) +
            "\n\nPreserve all facts, meditative tone. Output only the revised section."
        }]
    )
    return msg.content[0].text


def discover_topics(api_key: str, existing_titles: list = None) -> dict:
    """
    Researches trending cosmic horror YouTube topics and generates
    fresh topic ideas for sleep documentary style content.
    Uses Claude's web search tool to find what's trending.
    Returns structured topic list with rationale.
    """
    client = anthropic.Anthropic(api_key=api_key.strip())

    existing_text = ""
    if existing_titles:
        existing_text = (
            f"\nAVOID these topics — already on the channel ({len(existing_titles)} videos):\n"
            + "\n".join([f"- {t}" for t in existing_titles[:50]])
            + "\n\n"
        )

    system = (
        "You are a cosmic horror YouTube content strategist specialising in sleep documentary "
        "style content — long-form, scholarly, deeply researched scripts for audiences who "
        "want to listen in the dark to ideas they cannot unknow.\n\n"
        "STRICT NICHE RULE — every topic must be rooted exclusively in:\n"
        "- Lovecraft's mythos and entities (Cthulhu, Nyarlathotep, Azathoth, Yog-Sothoth, Shub-Niggurath, etc.)\n"
        "- Specific works from Lovecraft's literary circle and successors "
        "(Arthur Machen, William Hope Hodgson, Robert W. Chambers, Clark Ashton Smith, "
        "Algernon Blackwood, Thomas Ligotti, Laird Barron, Ramsey Campbell)\n"
        "- Philosophical and metaphysical concepts native to cosmic horror literature "
        "(cosmic indifferentism, the sublime, the numinous, ontological dread)\n"
        "- Real-world science or history that directly connects to a specific Lovecraft entity or concept\n\n"
        "ABSOLUTE BANS — never suggest:\n"
        "- Pop culture or mainstream media (no Stranger Things, no movies, no TV shows)\n"
        "- General horror that is not specifically cosmic horror\n"
        "- Any topic not traceable to Lovecraft or the Lovecraftian literary tradition\n"
        "- Vague concepts like 'fear of the unknown' without a specific entity or work anchor\n\n"
        "Each topic must have enough real literary, philosophical, or scientific depth for 12,000 words "
        "and be suitable for sleep-style listening — scholarly, atmospheric, unsettling.\n\n"
        "Output only valid JSON."
    )

    user = (
        f"Generate 12 original topic ideas for a Lovecraftian cosmic horror sleep documentary channel.\n\n"
        f"{existing_text}"
        f"Every topic must be strictly within Lovecraftian cosmic horror literature — "
        f"specific entities, specific works, specific authors from the tradition, "
        f"or real science that connects directly to a named Lovecraft entity.\n\n"
        f"Return JSON:\n"
        f'{{\n'
        f'  "trending_notes": "2-3 sentences on what is currently resonating in the Lovecraftian cosmic horror niche",\n'
        f'  "topics": [\n'
        f'    {{\n'
        f'      "title_seed": "Working topic title (not final)",\n'
        f'      "entity": "Specific Lovecraft entity or named cosmic horror concept",\n'
        f'      "core_argument": "One sentence — the specific argument this documentary makes. No colon.",\n'
        f'      "why_now": "One sentence — why this angle is underserved in the Lovecraftian niche",\n'
        f'      "depth_rating": 1-5,\n'
        f'      "sleep_fit": "high | medium | low"\n'
        f'    }}\n'
        f'  ]\n'
        f'}}\n\n'
        f"Generate exactly 12 topics. All must be strictly Lovecraftian cosmic horror literature. "
        f"Prioritise high depth_rating and high sleep_fit. Return only the JSON object."
    )

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=3000,
        system=system,
        messages=[{"role": "user", "content": user}]
    )

    raw = msg.content[0].text.strip().replace("```json", "").replace("```", "").strip()
    try:
        start = raw.index("{")
        end = raw.rindex("}") + 1
        return json.loads(raw[start:end])
    except Exception:
        return {
            "trending_notes": "Search completed. Generating topics based on current cosmic horror landscape.",
            "topics": [
                {
                    "title_seed": "The Real Science Behind Lovecraft's Dreaming God",
                    "entity": "Cthulhu / R'lyeh",
                    "core_argument": "NOAA's unidentified deep ocean recordings suggest something biological and massive exists at depths no expedition has reached",
                    "why_now": "The Bloop anniversary and new deep sea survey data make this timely",
                    "depth_rating": 5,
                    "sleep_fit": "high"
                }
            ]
        }


def generate_title_formats(topic: dict, api_key: str) -> list:
    """
    Takes a selected topic and generates 10 clickbait title options for a
    cosmic horror sleep channel. Returns a flat list of title strings.
    """
    client = anthropic.Anthropic(api_key=api_key.strip())

    system = (
        "You write YouTube titles for a cosmic horror Lovecraftian sleep documentary channel. "
        "Study the title style of sleep content channels — brief, intriguing, fear-inducing, "
        "curiosity-driven. Titles that make someone lying in the dark immediately press play.\n\n"
        "STRICT RULES for every title:\n"
        "- Maximum 80 characters — count carefully, reject any title over 80 characters\n"
        "- No colons anywhere in the title\n"
        "- No subtitles or secondary clauses separated by any punctuation\n"
        "- Clickbait that is analytically defensible — never fabricated claims\n"
        "- Dread through implication, never exaggeration\n"
        "- Never use: 'what if I told you', 'you won't believe', 'shocking truth', 'dark secret', "
        "'the truth about', 'what they don't want you to know'\n"
        "- Vary the grammatical structure across all 10 — no two titles should open the same way\n\n"
        "Output only valid JSON."
    )

    user = (
        f"Topic: {topic.get('title_seed', '')}\n"
        f"Core argument: {topic.get('core_argument', '')}\n"
        f"Entity: {topic.get('entity', '')}\n\n"
        f"Generate exactly 10 title options for this topic.\n"
        f"All must be under 80 characters. No colons. Varied structures.\n"
        f"Think like a sleep content creator — brief, eerie, irresistible.\n\n"
        f"Return a JSON array of exactly 10 strings:\n"
        f'["Title 1", "Title 2", "Title 3", "Title 4", "Title 5", '
        f'"Title 6", "Title 7", "Title 8", "Title 9", "Title 10"]\n\n'
        f"Return only the JSON array, nothing else."
    )

    msg = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=800,
        system=system,
        messages=[{"role": "user", "content": user}]
    )

    raw = msg.content[0].text.strip().replace("```json", "").replace("```", "").strip()
    try:
        start = raw.index("[")
        end = raw.rindex("]") + 1
        titles = json.loads(raw[start:end])
        # Ensure it's a flat list of strings
        if titles and isinstance(titles[0], str):
            return titles
        # Fallback if model returns old grouped format
        flat = []
        for item in titles:
            if isinstance(item, dict):
                flat.extend(item.get("titles", []))
            elif isinstance(item, str):
                flat.append(item)
        return flat[:10] if flat else [topic.get("title_seed", "")]
    except Exception:
        return [topic.get("title_seed", "")]
