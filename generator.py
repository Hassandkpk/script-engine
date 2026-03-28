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

    system = """You are a cosmic horror YouTube script writer. You produce scripts that:
- Are tied to real, verifiable data — never fabricated facts
- Never repeat structural patterns across scripts
- Do not use clichéd horror tropes
- Let the data determine the shape of the horror
- Write with forensic precision, not purple prose
- Sound like real human narration, not AI-generated content

You follow the divergence protocol exactly. You do not acknowledge the protocol in your output.
You output only the script — no preamble, no notes, no commentary."""

    user = f"""Follow this divergence protocol precisely:

{protocol}

Tone: {tone_map.get(tone, tone)}
Target length: {word_map.get(word_target, word_target)}

Write the complete script now. Output nothing but the script itself."""

    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        system=system,
        messages=[{"role": "user", "content": user}]
    )
    return message.content[0].text


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
        model="claude-opus-4-5",
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
