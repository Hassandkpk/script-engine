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
        # Delete all existing rows then reinsert — simplest approach for a small list
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
