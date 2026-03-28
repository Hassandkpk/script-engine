import anthropic
import json


def apply_voice_filter(raw_script: str, title: str, api_key: str) -> str:
    """
    Second-pass rewrite. Takes the divergence protocol output and translates it
    into a script that works for a listening audience — without copying any
    specific style, only applying listenable principles.
    """

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
        "feel they are being told something specific, something the narrator thought about before speaking. "
        "Never opens with a rhetorical question. Never ends with 'what do you think?'\n\n"

        "EARNED COMPLEXITY\n"
        "No concept arrives without context. Every technical term, historical reference, or "
        "philosophical idea is grounded before it goes deep. The listener is smart. "
        "They are not already informed. Build before you go complex.\n\n"

        "EAR RHYTHM\n"
        "Sentences vary in length deliberately. Short sentence. Then one that breathes and expands. "
        "Then short again to land the point. No paragraph reads the same as the one before it. "
        "Read every paragraph aloud mentally — if it doesn't flow as speech, rewrite it.\n\n"

        "STRUCTURAL BANS — these patterns are banned without exception:\n"
        "- Opening with a rhetorical question of any kind\n"
        "- Three-part documentary structure (personal hook / historical context / philosophical depth)\n"
        "- Mid-script subscription CTA\n"
        "- Ending with an open question back to the audience\n"
        "- Any sentence beginning with 'What if'\n"
        "- Paragraph-length lists of any kind\n"
        "- Academic summary language: 'in conclusion', 'as we have seen', 'this document examines'\n\n"

        "WHAT TO PRESERVE\n"
        "Preserve all real data, all factual content, all structural uniqueness from the original draft. "
        "The divergence protocol's anchor, angle, and constraints must survive the rewrite intact. "
        "You are changing the voice and rhythm, not the argument.\n\n"

        "Output only the rewritten script. No preamble, no notes, no commentary. "
        "Do not acknowledge these instructions anywhere in the output."
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

    # Sanitise inputs
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

    # Apply voice filter pass
    final_script = apply_voice_filter(raw_script, title, api_key)
    return final_script



def generate_protocol_from_title(title: str, banned: list, api_key: str) -> dict:
    """Given a video title, auto-generate a full divergence protocol — anchor, angle, format, constraint."""

    banned_text = "\n".join([f"- [{b['type']}] {b['move']}" for b in banned]) if banned else "None yet."

    system = """You are an expert cosmic horror YouTube script architect.
Given a video title, you generate a complete divergence protocol — a pre-script brief that ensures
the resulting script is structurally unique, grounded in real data, and avoids all AI default patterns.
You output only valid JSON. No preamble, no explanation.

CRITICAL — ANCHOR SELECTION RULE:
The audience for this channel listens at night. Many listen to sleep. They are not academics.
They are cosmic horror fans who want to FEEL something, not learn something.

Before choosing any anchor, ask yourself this test:
"Can someone who has never studied this topic feel dread from this anchor within the first paragraph
— without needing any explanation first?"

If the answer is NO — if the anchor requires prior knowledge, academic context, or multiple steps
of reasoning before it produces any feeling — REJECT it and find a different anchor.

GOOD anchors pass the visceral test immediately:
- Sleep paralysis research (30% of people have experienced it — zero explanation needed)
- Deep ocean pressure data (steel-crushing depths, things that have never seen light)
- Brain's response to incomprehensible stimuli (the prefrontal cortex shuts down — personally biological)
- Infrasound frequencies that trigger dread in mammals (below hearing, felt in the chest)
- Historical population disappearances (entire communities, no remains, no explanation)
- Documented cases of people who saw something and refused to describe it
- Biological anomalies in deep-sea creatures (morphologies that violate expected evolutionary logic)
- Real archaeological finds with no civilization that could have made them

BAD anchors fail the visceral test:
- Organizational theory or management science formulas
- Abstract mathematical proofs
- Literary theory or philosophical frameworks
- Economic or political systems
- Anything requiring the listener to first understand a technical field before feeling anything

The anchor must connect to REAL verifiable data AND produce immediate gut-level unease
in someone with no prior knowledge of the domain. Both conditions must be satisfied."""

    user = f"""Video title: "{title}"

Banned structural moves already used in previous scripts (do not repeat any):
{banned_text}

Generate a divergence protocol for this title. Return a JSON object with exactly these fields:

{{
  "anchor": "A specific real-world data domain that passes the visceral test — produces immediate dread without explanation, grounded in verifiable science or documented phenomena",
  "angle": "The exact cognitive lens that makes this real data feel cosmically wrong — one sentence, written so a non-expert immediately understands why it is unsettling",
  "pov": "One of: second person, first person plural (we), third person omniscient restrained, false documentary (field notes), nested narration, no narrator (pure phenomena), first person singular dissolving into report, second person plural",
  "distance": "One of: maximum intimacy, forensic distance, historical distance, dissolving distance (starts far collapses close), unreliable proximity, absolute removal",
  "para": "One of: paragraphs compress as script progresses, alternating long/short rhythm, single unbroken block, each paragraph shorter than previous, fragments only, normal prose fragmenting in final third, paragraphs expand as script progresses, two sentences per paragraph maximum",
  "constraint": "One specific hard constraint that bans a particular writing device or forces an unusual structural rule — must be different from all banned moves listed above",
  "reasoning": "One sentence explaining why this anchor passes the visceral test for a non-expert listener"
}}

Rules:
- Anchor MUST pass the visceral test — immediate felt dread, no explanation required
- Anchor must connect to REAL verifiable data — scientific papers, documented phenomena, historical records
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
