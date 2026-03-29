import requests
import anthropic
import streamlit as st
import json


def get_youtube_api_key() -> str:
    try:
        return st.secrets["YOUTUBE_API_KEY"]
    except Exception:
        return ""


def resolve_channel_id(channel_input: str, api_key: str) -> tuple:
    """
    Takes a channel URL, @handle, or raw ID.
    Returns (channel_id, channel_name) or (None, None) on failure.
    """
    channel_input = channel_input.strip()

    # Raw channel ID
    if channel_input.startswith("UC") and "/" not in channel_input:
        r = requests.get(
            "https://www.googleapis.com/youtube/v3/channels",
            params={"part": "snippet", "id": channel_input, "key": api_key},
            timeout=10
        )
        d = r.json()
        if d.get("items"):
            return channel_input, d["items"][0]["snippet"]["title"]
        return None, None

    # Extract handle or channel path from URL
    import re
    match = re.search(r"youtube\.com/(?:channel/|@)([\w\-]+)", channel_input)
    if match:
        handle = match.group(1)
        if handle.startswith("UC"):
            r = requests.get(
                "https://www.googleapis.com/youtube/v3/channels",
                params={"part": "snippet", "id": handle, "key": api_key},
                timeout=10
            )
            d = r.json()
            if d.get("items"):
                return handle, d["items"][0]["snippet"]["title"]
            return None, None
        else:
            # Search by handle
            r = requests.get(
                "https://www.googleapis.com/youtube/v3/channels",
                params={"part": "snippet", "forHandle": handle, "key": api_key},
                timeout=10
            )
            d = r.json()
            if d.get("items"):
                ch = d["items"][0]
                return ch["id"], ch["snippet"]["title"]
            return None, None

    return None, None


def get_channel_videos(channel_id: str, api_key: str, max_results: int = 100) -> list:
    """Fetch up to max_results video titles from a channel."""
    titles = []
    page_token = ""
    fetched = 0

    while fetched < max_results:
        batch = min(50, max_results - fetched)
        params = {
            "part": "snippet",
            "channelId": channel_id,
            "type": "video",
            "maxResults": batch,
            "order": "date",
            "key": api_key,
        }
        if page_token:
            params["pageToken"] = page_token

        r = requests.get(
            "https://www.googleapis.com/youtube/v3/search",
            params=params,
            timeout=15
        )
        d = r.json()

        if d.get("error"):
            raise Exception(d["error"]["message"])

        for item in d.get("items", []):
            title = item.get("snippet", {}).get("title", "")
            if title:
                titles.append(title)

        fetched += len(d.get("items", []))
        page_token = d.get("nextPageToken", "")
        if not page_token:
            break

    return titles


def check_concept(new_title: str, existing_titles: list, api_key: str) -> dict:
    """
    Uses Claude to check whether the new title covers a concept
    already published on the channel.
    Returns dict with status (green/yellow/red), reason, matches.
    """
    if not existing_titles:
        return {
            "status": "green",
            "reason": "No existing videos to compare against.",
            "matches": [],
            "skipped": True
        }

    client = anthropic.Anthropic(api_key=api_key)

    system = (
        "You are a YouTube content strategist. You analyze whether a new video concept "
        "has already been covered on a channel. Different titles can cover the same core concept — "
        "you look at the underlying idea, argument, and framing, not just keywords. "
        "Output only valid JSON."
    )

    titles_text = "\n".join([f"{i+1}. {t}" for i, t in enumerate(existing_titles)])

    user = f"""New title: "{new_title}"

Existing channel videos ({len(existing_titles)} titles):
{titles_text}

Analyze whether the new title covers a concept already explored in the existing videos.
Consider: same core argument, same subject from same angle, same reveal or thesis, same entity/topic with same framing.

Return JSON:
{{
  "status": "green" | "yellow" | "red",
  "reason": "one clear sentence explaining the verdict",
  "matches": ["existing title 1", "existing title 2"]
}}

Status guide:
- green: genuinely new concept not covered before
- yellow: adjacent to existing content but different enough to proceed with caution
- red: this concept or a close variant has already been published

Return only the JSON object."""

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
        return {"status": "green", "reason": "Check inconclusive — proceeding.", "matches": []}
