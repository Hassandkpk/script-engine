import streamlit as st


def _client():
    try:
        from supabase import create_client, Client
        url: str = st.secrets["SUPABASE_URL"]
        key: str = st.secrets["SUPABASE_KEY"]
        client: Client = create_client(url, key)
        return client
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return None


def load_data():
    empty = {"scripts": [], "banned": [], "settings": {}}
    try:
        db = _client()
        if not db:
            return empty

        res = db.table("banned_moves").select("*").order("created_at").execute()
        banned = [{"move": r["move"], "type": r["type"]} for r in (res.data or [])]

        res2 = db.table("scripts").select("*").order("created_at").execute()
        scripts = []
        for r in (res2.data or []):
            scripts.append({
                "id": r["script_num"],
                "date": r["created_at"],
                "protocol": r.get("protocol", ""),
                "script": r.get("script_text", ""),
                "anchor": r.get("anchor", ""),
                "pov": r.get("pov", ""),
                "constraint": r.get("constraint_rule", ""),
                "word_target": r.get("word_target", ""),
                "tone": r.get("tone", ""),
            })

        return {"scripts": scripts, "banned": banned, "settings": {}}

    except Exception as e:
        st.warning(f"Could not load data: {e}")
        return empty


def save_banned(banned: list):
    try:
        db = _client()
        if not db:
            return
        db.table("banned_moves").delete().gte("id", 0).execute()
        if banned:
            rows = [{"move": b["move"], "type": b["type"]} for b in banned]
            db.table("banned_moves").insert(rows).execute()
    except Exception as e:
        st.error(f"Failed to save ban list: {e}")


def save_script(script_record: dict):
    try:
        db = _client()
        if not db:
            return
        db.table("scripts").insert({
            "script_num": script_record["id"],
            "protocol": script_record.get("protocol", ""),
            "script_text": script_record.get("script", ""),
            "anchor": script_record.get("anchor", ""),
            "pov": script_record.get("pov", ""),
            "constraint_rule": script_record.get("constraint", ""),
            "word_target": script_record.get("word_target", ""),
            "tone": script_record.get("tone", ""),
        }).execute()
    except Exception as e:
        st.error(f"Failed to save script: {e}")


def load_recent_fingerprints(limit: int = 15) -> list:
    try:
        db = _client()
        if not db:
            return []
        res = db.table("scripts").select(
            "anchor, pov, constraint_rule, word_target, tone, protocol, created_at"
        ).order("created_at", desc=True).limit(limit).execute()

        fingerprints = []
        for r in (res.data or []):
            protocol_text = r.get("protocol", "")
            distance = ""
            para = ""
            for line in protocol_text.splitlines():
                if line.lower().startswith("narrative distance:"):
                    distance = line.split(":", 1)[-1].strip()
                if line.lower().startswith("paragraph structure:"):
                    para = line.split(":", 1)[-1].strip()
            fingerprints.append({
                "anchor": r.get("anchor", ""),
                "pov": r.get("pov", ""),
                "distance": distance,
                "para": para,
                "constraint": r.get("constraint_rule", ""),
                "tone": r.get("tone", ""),
            })
        return fingerprints
    except Exception:
        return []


def load_channel() -> dict:
    try:
        db = _client()
        if not db:
            return {}
        res = db.table("channel_settings").select("*").limit(1).execute()
        if res.data:
            return res.data[0]
        return {}
    except Exception:
        return {}


def save_channel(channel_id: str, channel_url: str, channel_name: str):
    try:
        db = _client()
        if not db:
            return
        db.table("channel_settings").upsert({
            "id": 1,
            "channel_id": channel_id,
            "channel_url": channel_url,
            "channel_name": channel_name,
        }).execute()
    except Exception as e:
        st.error(f"Failed to save channel: {e}")
