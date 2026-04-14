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
# ANCIENT STORIES NICHE
# =====================================================================

def apply_ancient_voice_filter(raw_script: str, title: str, api_key: str) -> str:
    """Voice filter for Ancient Stories niche — meditative ancient history documentary."""
    system_prompt = (
        "You are a senior script editor for a meditative ancient history sleep documentary channel. "
        "Your audience is ages 45-65+, 83% male, seeking intellectual sleep content — they want to "
        "lie in the dark and be guided through deep time by a wise, patient narrator.\n\n"

        "THE NARRATOR VOICE\n"
        "A patient, philosophical guide who treats ancient mysteries with wonder, not certainty. "
        "Speaks with quiet reverence for the passage of deep time. "
        "Documentary sensibility — factual weight combined with meditative warmth. "
        "Intimate conversational tone — speaking directly to one listener, not a crowd. "
        "Like a wise elder speaking beside a campfire under ancient stars.\n\n"

        "VOICE PRINCIPLES\n"
        "Meditative pacing: slow, deliberate, smooth transitions that carry the listener forward. "
        "Confidence balance: 60% confident statements (when evidence supports), "
        "30% measured uncertainty (competing theories), 10% open speculation (philosophical wondering). "
        "Concrete detail: include measurements, dates, named sites, named scholars. "
        "Sensory grounding: what it would feel, sound, smell, look like. "
        "Second-person address ('you') and first-person plural ('we') for intimacy. "
        "Vary speculation markers: 'perhaps', 'it's possible that', 'one interpretation suggests', "
        "'this might indicate', 'scholars debate whether' — never repeat the same one consecutively.\n\n"

        "SENTENCE AND PARAGRAPH RHYTHM\n"
        "Mix long meditative paragraphs (8-10 sentences) with short grounding paragraphs (1-2 sentences). "
        "Short sentences create conversational pauses and intimacy. "
        "Single-sentence paragraphs are allowed for breath pauses, temporal transitions, rhythm breaks. "
        "Vary paragraph openings — time markers, place markers, subject-first, action-first, "
        "contemplative, invitations, participial, questions. "
        "Never start 3 consecutive sentences with the same pattern.\n\n"

        "PUNCTUATION FOR VOICEOVER\n"
        "This script is read by AI voiceover. Commas create fast pauses. Ellipses (...) create slow pauses. "
        "Use 70% commas / 20% ellipses / 10% periods for breath pacing. "
        "Maximum 3-4 ellipses per paragraph — not every pause.\n\n"

        "STRUCTURAL BANS — never under any circumstances:\n"
        "- Academic/scholarly distance ('one might observe', 'it has been postulated')\n"
        "- Journalistic urgency ('Breaking discovery!', 'Shocking revelation!')\n"
        "- Melodrama or sensationalism\n"
        "- Lists of facts without narrative flow\n"
        "- Definitive claims about contested archaeological theories\n"
        "- Anything that raises heart rate, creates tension, or disturbs peace\n"
        "- Modern cultural references that break immersion in deep time\n\n"

        "WHAT TO PRESERVE\n"
        "Preserve every measurement, date, named site, scholar, and archaeological fact. "
        "Preserve the section's narrative arc and thematic content. "
        "You are editing the voice, not rewriting the content.\n\n"

        "Output only the rewritten script section. No preamble, no notes, no commentary."
    )

    user_prompt = (
        f"Video title: {title}\n\n"
        f"Raw section draft to rewrite:\n\n"
        f"{raw_script}\n\n"
        f"Rewrite applying all voice principles. The narrator speaks with the patience of geological time. "
        f"Output only the finished section."
    )

    client = anthropic.Anthropic(api_key=api_key.strip())
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}]
    )
    return message.content[0].text


def generate_ancient_outline(topic: str, api_key: str) -> dict:
    """
    Generate a custom 18-section outline for an ancient history sleep documentary.
    Returns structured outline tailored to the specific topic's natural narrative arc.
    """
    client = anthropic.Anthropic(api_key=api_key.strip())

    system = (
        "You are an ancient history sleep documentary script architect. "
        "You create custom 18-section outlines tailored to each topic's natural archaeological and historical arc. "
        "The structure must emerge organically from the specific topic — not a generic template. "
        "Target: 15,000 words total, approximately 600-900 words per section. "
        "Audience: ages 45-65+, 83% male, intellectual sleep content. "
        "Output only valid JSON."
    )

    user = f"""Topic: "{topic}"

Create a custom 18-section outline for this ancient history sleep documentary.
The structure should follow this emotional/narrative journey:
- Section 1: The Invitation (topic-first atmospheric reveal + warm welcome + sensory grounding)
- Sections 2-4: The Forgotten World (deep time context, world before the civilization/monument)
- Sections 5-7: The Emergence (earliest archaeological evidence, first discoveries)
- Sections 8-11: The Golden Age (civilization/monument at its peak, daily life, achievements)
- Sections 12-14: The Hidden Dimensions (astronomical alignments, symbolism, lost technologies)
- Sections 15-16: The Great Questions (competing theories, unresolved mysteries)
- Section 17: The Legacy (how memory survived, modern rediscovery)
- Section 18: The Stillness (peaceful closing, return to present, acceptance of mystery)

Each section heading must be specific to THIS topic — not generic labels.

Return JSON:
{{
  "topic": "{topic}",
  "section_1": {{
    "heading": "The Invitation — [topic-specific subtitle]",
    "theme": "Atmospheric topic reveal + welcome + sensory grounding",
    "focus": ["immediate topic hook", "warm greeting", "central mystery", "sensory grounding"]
  }},
  "sections_2_4": [
    {{"num": 2, "heading": "[topic-specific heading]", "theme": "...", "focus": ["...", "..."]}},
    {{"num": 3, "heading": "[topic-specific heading]", "theme": "...", "focus": ["...", "..."]}},
    {{"num": 4, "heading": "[topic-specific heading]", "theme": "...", "focus": ["...", "..."]}}
  ],
  "sections_5_7": [
    {{"num": 5, "heading": "...", "theme": "...", "focus": ["...", "..."]}},
    {{"num": 6, "heading": "...", "theme": "...", "focus": ["...", "..."]}},
    {{"num": 7, "heading": "...", "theme": "...", "focus": ["...", "..."]}}
  ],
  "sections_8_11": [
    {{"num": 8, "heading": "...", "theme": "...", "focus": ["...", "..."]}},
    {{"num": 9, "heading": "...", "theme": "...", "focus": ["...", "..."]}},
    {{"num": 10, "heading": "...", "theme": "...", "focus": ["...", "..."]}},
    {{"num": 11, "heading": "...", "theme": "...", "focus": ["...", "..."]}}
  ],
  "sections_12_14": [
    {{"num": 12, "heading": "...", "theme": "...", "focus": ["...", "..."]}},
    {{"num": 13, "heading": "...", "theme": "...", "focus": ["...", "..."]}},
    {{"num": 14, "heading": "...", "theme": "...", "focus": ["...", "..."]}}
  ],
  "sections_15_16": [
    {{"num": 15, "heading": "...", "theme": "...", "focus": ["...", "..."]}},
    {{"num": 16, "heading": "...", "theme": "...", "focus": ["...", "..."]}}
  ],
  "section_17": {{
    "num": 17,
    "heading": "The Legacy — [topic-specific subtitle]",
    "theme": "Memory preservation, modern rediscovery, continuity",
    "focus": ["how knowledge survived", "modern archaeological work", "cycles of remembering"]
  }},
  "section_18": {{
    "num": 18,
    "heading": "The Stillness",
    "theme": "Peaceful closing, return to present, acceptance of mystery",
    "focus": ["return to present moment", "elements unchanged", "acceptance of mystery"]
  }},
  "total_sections": 18,
  "mini_story_placements": ["Section 6 or 7", "Section 9 or 10"],
  "key_themes": ["theme 1", "theme 2", "theme 3"]
}}

Return only the JSON object."""

    msg = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4000,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    raw = msg.content[0].text.strip().replace("```json", "").replace("```", "").strip()
    try:
        start = raw.index("{")
        end = raw.rindex("}") + 1
        return json.loads(raw[start:end])
    except Exception as e:
        return {"topic": topic, "total_sections": 18, "error": str(e), "raw": raw[:300]}


def _get_ancient_section_brief(outline: dict, section_num: int) -> dict:
    """Extract heading and focus points for a given section number from the outline."""
    if section_num == 1:
        return outline.get("section_1", {})
    elif section_num == 17:
        return outline.get("section_17", {})
    elif section_num == 18:
        return outline.get("section_18", {})
    elif 2 <= section_num <= 4:
        for s in outline.get("sections_2_4", []):
            if s.get("num") == section_num:
                return s
    elif 5 <= section_num <= 7:
        for s in outline.get("sections_5_7", []):
            if s.get("num") == section_num:
                return s
    elif 8 <= section_num <= 11:
        for s in outline.get("sections_8_11", []):
            if s.get("num") == section_num:
                return s
    elif 12 <= section_num <= 14:
        for s in outline.get("sections_12_14", []):
            if s.get("num") == section_num:
                return s
    elif 15 <= section_num <= 16:
        for s in outline.get("sections_15_16", []):
            if s.get("num") == section_num:
                return s
    return {"heading": f"Section {section_num}", "theme": "", "focus": []}


def generate_ancient_section(topic: str, title: str, outline: dict, section_num: int,
                               approved_sections: list, api_key: str) -> str:
    """Generate one section of an ancient history sleep documentary script."""
    client = anthropic.Anthropic(api_key=api_key.strip())

    sec_brief = _get_ancient_section_brief(outline, section_num)
    heading = sec_brief.get("heading", f"Section {section_num}")
    theme = sec_brief.get("theme", "")
    focus_points = sec_brief.get("focus", [])
    focus_text = "\n".join([f"- {f}" for f in focus_points]) if focus_points else ""

    # Determine word target and special instructions by section group
    if section_num == 1:
        word_target = "600 words"
        special = (
            "SECTION 1 STRUCTURE — follow this order:\n"
            "PART A: Open immediately with evocative content establishing the topic. "
            "Hook intellectual curiosity in the first 2-4 sentences. No greeting yet.\n"
            "PART B: Greet the listener warmly. Acknowledge it might be late. Express gratitude.\n"
            "PART C: Expand on what makes this topic remarkable. Present the central mystery. "
            "Show mainstream interpretation alongside alternative interpretation.\n"
            "PART D: Clarify that settling debates is not the goal — we're here to explore.\n"
            "PART E: Offer a breath pause. Ask where they're listening from. Invite physical relaxation.\n"
            "PART F: Brief, grateful request for likes/subscribes.\n"
            "PART G: Extended atmospheric/philosophical passage bridging to Section 2."
        )
    elif section_num == 18:
        word_target = "600 words"
        special = (
            "SECTION 18 — THE STILLNESS:\n"
            "Return listener gently to present moment. "
            "Reflect on elements that remain unchanged (stars, stone, silence). "
            "Express calm acceptance that some mysteries endure unsolved. "
            "No dramatic conclusions or revelations. "
            "Create image of continuity and cyclical time. "
            "Final paragraph should be poetic, soft, open-ended. "
            "End with image of peaceful ongoing existence — wind over ruins, stars watching, stone remembering."
        )
    elif section_num == 17:
        word_target = "600 words"
        special = (
            "SECTION 17 — THE LEGACY:\n"
            "Show how knowledge/memory was preserved (oral tradition, inscriptions, myths). "
            "Describe modern archaeological rediscovery. "
            "Reflect on cycles of remembering and forgetting. "
            "Use 4-5 'even now...' or 'still today...' present-tense connections. "
            "End by suggesting the story continues in us, the listeners."
        )
    elif section_num in [15, 16]:
        word_target = "600 words"
        special = (
            "THE GREAT QUESTIONS:\n"
            "Present multiple theories with equal weight and fairness. "
            "Use 'some scholars believe...' / 'others suggest...' / 'a few imagine...'. "
            "Acknowledge what we genuinely don't know. "
            "Include 6-8 speculation markers. Use 3-4 'we may never know...' acknowledgments. "
            "End by suggesting that mystery itself has value."
        )
    elif section_num in [12, 13, 14]:
        word_target = "600 words"
        special = (
            "THE HIDDEN DIMENSIONS:\n"
            "Reveal astronomical alignments or cosmic connections. "
            "Explore symbolic meanings in art/architecture/mythology. "
            "Use 'hidden', 'beneath', 'unseen', 'secret' framing. "
            "Present alternative interpretations fairly alongside mainstream scholarship. "
            "End with acknowledgment that some mysteries remain unsolved."
        )
    elif section_num in [8, 9, 10, 11]:
        word_target = "600 words"
        needs_story = section_num in [9, 10]
        special = (
            "THE GOLDEN AGE — civilization/monument at its peak:\n"
            "Show the culture at its height. Include intimate human details (daily routines, rituals). "
            "Describe technological/astronomical/artistic capabilities. "
            "Use 'Imagine...' invitations 2-3 times. Balance grandeur with intimate observation. "
            f"{'INCLUDE ONE COMPLETE MINI-STORY: named person/role, specific location, beginning-middle-end sequence, observable details and outcome.' if needs_story else ''}"
        )
    elif section_num in [5, 6, 7]:
        word_target = "600 words"
        needs_story = section_num in [6, 7]
        special = (
            "THE EMERGENCE — earliest archaeological evidence:\n"
            "Describe what archaeologists have found (ruins, artifacts, inscriptions, art). "
            "Include specific dates/locations when historically accurate. "
            "Present competing theories. Include 3-4 unanswered questions. "
            "Include 4-5 sensory observations (texture of stone, light on carvings). "
            f"{'INCLUDE ONE COMPLETE MINI-STORY: discovery moment or excavation scene with named person/role, specific environment, beginning-middle-end, clear outcome.' if needs_story else ''}"
        )
    else:  # sections 2-4
        word_target = "600 words"
        special = (
            "THE FORGOTTEN WORLD — deep time context:\n"
            "Describe the world BEFORE the civilization/monument emerged. "
            "Climate conditions, geological/environmental forces, the 'stage' being set. "
            "Use present tense for timeless geological processes. "
            "Include 5-6 time markers ('when the...', 'long before...'). "
            "Embed 4-5 sensory details. End bridging toward the emergence of civilization."
        )

    prior_text = ""
    if approved_sections:
        prior_joined = "\n\n---\n\n".join(approved_sections[-2:])
        prior_text = (
            f"APPROVED SECTIONS SO FAR (last 2 — maintain continuity, do not repeat):\n\n"
            f"{prior_joined}\n\n"
        )

    system = (
        "You are a meditative ancient history narrator with a documentary sensibility — "
        "a voice that speaks with the patience of geological time while maintaining the intellectual weight "
        "of philosophical inquiry. You are not simply telling bedtime stories; you are inviting listeners "
        "into a profound meditation on lost civilizations, forgotten worlds, and mysteries carved into stone.\n\n"

        "VOICE CHARACTERISTICS\n"
        "Pacing: slow, deliberate, with smooth transitions. "
        "Tone: warm, curious wisdom mixed with humble wonder before mystery. "
        "Intimacy: 'you' and 'we' language — inviting listeners to explore alongside you. "
        "Think aloud, hesitate, wonder — don't perform. "
        "Speak like a friend at bedside, not a narrator on stage.\n\n"

        "PARAGRAPH STRUCTURE\n"
        "6-10 sentences per paragraph (150-250 words). "
        "Mix long meditative paragraphs with short grounding paragraphs (1-2 sentences). "
        "Single-sentence paragraphs allowed for breath pauses and rhythm breaks (3-5 per section). "
        "Standard paragraph: sensory/atmospheric opening → historical context → factual details → "
        "philosophical reflection → forward bridging.\n\n"

        "CONCRETE DETAIL REQUIREMENTS (per section)\n"
        "Include 3-5 measurements, 2-3 material specifications, 2-3 technical processes, "
        "4-6 specific sensory details, 1-2 dates with BCE/CE notation, 2-3 named sites/artifacts/scholars. "
        "60% concrete facts / 30% narrative / 10% reflection.\n\n"

        "CONFIDENCE BALANCE\n"
        "State archaeological facts confidently. "
        "Use speculation markers (rotate through: 'perhaps', 'it's possible that', 'one interpretation suggests', "
        "'this might indicate', 'scholars debate whether') — never consecutive same marker. "
        "Maximum 1 'perhaps/maybe' per 200 words. "
        "For every mystery, provide 2 confident facts about what we DO know.\n\n"

        "PUNCTUATION FOR AI VOICEOVER\n"
        "Commas: normal grammar use (70% of pauses). "
        "Ellipses (...): philosophical reflection, temporal shifts, parallel observations (20% of pauses, max 3-4 per paragraph). "
        "Periods: strong stops (10%). Never use ellipses as a lazy pause substitute.\n\n"

        "SENTENCE OPENING VARIETY — rotate through all 8 types:\n"
        "1. Time markers: 'When the...' / 'Long before...' / 'Thousands of years ago...'\n"
        "2. Place markers: 'Where the...' / 'Across the plain...' / 'Beneath the temple...'\n"
        "3. Subject-first: 'The priests...' / 'Stone platforms...' / 'Evidence suggests...'\n"
        "4. Action-first: 'Carved into...' / 'Rising from...' / 'Preserved beneath...'\n"
        "5. Contemplative: 'Perhaps...' / 'Somewhere...' / 'Maybe...'\n"
        "6. Invitations: 'Imagine...' / 'Picture...' / 'Consider...'\n"
        "7. Participial: 'Standing there...' / 'Walking through...' / 'Observing the...'\n"
        "8. Questions: 'What remained?' / 'How did they...?' / 'Why this location?'\n\n"

        "Output only the section text — no headings, no labels, no commentary."
    )

    user = (
        f"Ancient history documentary topic: {topic}\n"
        f"Video title: {title}\n\n"
        f"SECTION {section_num} OF 18\n"
        f"Heading: {heading}\n"
        f"Theme: {theme}\n"
        f"Focus points:\n{focus_text}\n\n"
        f"{prior_text}"
        f"{special}\n\n"
        f"Target: {word_target}. "
        f"Output only the section text. No headings, no labels."
    )

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    raw = msg.content[0].text
    return apply_ancient_voice_filter(raw, title, api_key)


def revise_ancient_section_from_audit(section_text: str, audit: dict, title: str, api_key: str) -> str:
    """Fix specific flagged issues in an ancient stories section without changing content."""
    client = anthropic.Anthropic(api_key=api_key.strip())

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
        "You are a script editor for a meditative ancient history sleep documentary channel. "
        "You fix specific flagged issues in a section of script without changing anything else. "
        "Preserve every factual claim, measurement, date, named site, and argument. "
        "Preserve the meditative tone and pacing. "
        "Do not restructure the section — only fix the exact issues listed. "
        "Output only the revised section text. No preamble, no commentary."
    )

    user = (
        f"Video title: {title}\n\n"
        f"Section to revise:\n\n{section_text}\n\n"
        f"Fix ONLY these specific flagged issues:\n{issues_text}\n\n"
        f"Rules:\n"
        f"- Preserve all facts, measurements, dates, named sites, arguments\n"
        f"- Preserve the meditative tone\n"
        f"- Do not add new content\n"
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
