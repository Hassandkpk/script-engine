import anthropic
import json


def generate_script(protocol: str, word_target: str, tone: str, api_key: str) -> str:
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

    # Sanitise inputs — strip nulls and non-UTF8 characters that cause BadRequestError
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
    return message.content[0].text


def generate_protocol_from_title(title: str, banned: list, api_key: str) -> dict:
    """Given a video title, auto-generate a full divergence protocol — anchor, angle, format, constraint."""

    banned_text = "\n".join([f"- [{b['type']}] {b['move']}" for b in banned]) if banned else "None yet."

    system = """You are an expert cosmic horror YouTube script architect. 
Given a video title, you generate a complete divergence protocol — a pre-script brief that ensures 
the resulting script is structurally unique, grounded in real data, and avoids all AI default patterns.
You output only valid JSON. No preamble, no explanation."""

    user = f"""Video title: "{title}"

Banned structural moves already used in previous scripts (do not repeat any):
{banned_text}

Generate a divergence protocol for this title. Return a JSON object with exactly these fields:

{{
  "anchor": "A specific real-world data domain that grounds this topic in verifiable science, history, or data — not vague, very specific",
  "angle": "The exact cognitive lens that makes this real data feel cosmically wrong or unsettling — one specific sentence",
  "pov": "One of: second person, first person plural (we), third person omniscient restrained, false documentary (field notes), nested narration, no narrator (pure phenomena), first person singular dissolving into report, second person plural",
  "distance": "One of: maximum intimacy, forensic distance, historical distance, dissolving distance (starts far collapses close), unreliable proximity, absolute removal",
  "para": "One of: paragraphs compress as script progresses, alternating long/short rhythm, single unbroken block, each paragraph shorter than previous, fragments only, normal prose fragmenting in final third, paragraphs expand as script progresses, two sentences per paragraph maximum",
  "constraint": "One specific hard constraint that bans a particular writing device or forces an unusual structural rule — must be different from all banned moves listed above",
  "reasoning": "One sentence explaining why this anchor specifically fits this title"
}}

Rules:
- The anchor must connect to REAL verifiable data — scientific papers, historical records, measurable phenomena
- Do not choose any anchor, POV, or constraint that matches the banned moves list
- The constraint must be specific and enforceable, not vague
- Return only the JSON object, nothing else"""

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
            "anchor": "Deep time geology — strata that should not exist in the sequence they do",
            "angle": "The data was always there. It was only noticed during archiving, years later.",
            "pov": "third person omniscient restrained",
            "distance": "forensic distance",
            "para": "paragraphs compress as script progresses",
            "constraint": "No sentence may exceed 15 words",
            "reasoning": "Fallback protocol used due to JSON parse error."
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
        "Rage-bait (resolves to truth)": "provocative titles that sound outrageous but are analytically defensible — the rage-bait resolves into a real argument",
        "Curiosity gap": "titles that create an irresistible knowledge gap — the viewer cannot not click",
        "Institutional villain": "titles that frame an institution (WTA, NASA, government body) as the structural antagonist — not accusing individuals of malice",
        "Scientific anomaly": "titles that foreground a real data anomaly — makes the science the horror",
        "Fear — personal threat": "titles that make the viewer feel personally implicated or at risk",
        "Archival revelation": "titles framed as discovered or suppressed information — the document was not meant to be found",
    }

    style_prompts = "\n".join([f"- {s}: {style_descriptions.get(s, s)}" for s in styles])

    system = """You generate YouTube titles for cosmic horror content. Your titles:
- Are tied to real, defensible claims — never fabricated
- Never use banned phrases like 'what if I told you', 'you won't believe', 'shocking truth'
- Are varied in structure — no two titles use the same grammatical pattern
- Are specific, not generic
- Sound like a human editor wrote them, not an AI
Output only valid JSON."""

    user = f"""Based on this script content, generate {count} title options for each of these styles:

{style_prompts}

Script content:
{script[:3000]}

Return a JSON array like this:
[
  {{"style": "Style name", "titles": ["Title 1", "Title 2", "Title 3"]}},
  ...
]

Return only the JSON array, nothing else."""

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
