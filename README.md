# ◈ Cosmic Horror Script Engine

A Streamlit tool for producing structurally unique cosmic horror YouTube scripts — built on the Divergence Protocol system. Fully cloud-hosted: GitHub repo + Streamlit Cloud + Supabase database. No local files needed.

## Stack

| Layer | Service | Cost |
|---|---|---|
| UI + hosting | Streamlit Cloud | Free |
| Repo | GitHub | Free |
| Database | Supabase | Free tier |
| AI | Anthropic Claude | Pay per use |

---

## One-time setup

### 1. Supabase — create your database

1. Go to [supabase.com](https://supabase.com) and create a free account
2. Create a new project (pick any name, any region)
3. Once the project is ready, go to **SQL Editor** and run this:

```sql
create table scripts (
  id bigint generated always as identity primary key,
  script_num int not null,
  created_at timestamptz default now(),
  protocol text,
  script_text text,
  anchor text,
  pov text,
  constraint_rule text,
  word_target text,
  tone text
);

create table banned_moves (
  id bigint generated always as identity primary key,
  created_at timestamptz default now(),
  move text not null,
  type text not null
);
```

4. Go to **Project Settings → API** and copy:
   - **Project URL** → this is your `SUPABASE_URL`
   - **anon / public key** → this is your `SUPABASE_KEY`

---

### 2. GitHub — push the repo

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/cosmic-horror-script-engine.git
git push -u origin main
```

---

### 3. Streamlit Cloud — deploy

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **New app** → connect your GitHub repo → set main file to `app.py`
3. Before deploying, click **Advanced settings → Secrets** and paste:

```toml
ANTHROPIC_API_KEY = "sk-ant-your-key-here"
SUPABASE_URL = "https://your-project-id.supabase.co"
SUPABASE_KEY = "your-supabase-anon-key-here"
```

4. Click **Deploy**

That's it. The app is live, the database is permanent, and no keys are ever in the repo.

---

## Features

- **Divergence Protocol** — Roll domain anchors, entry angles, format constraints. Generates a pre-script brief.
- **Script Generator** — Claude writes the full script from your protocol. Export to PDF or Word.
- **Title Machine** — Rage-bait, curiosity-gap, institutional villain, and anomaly titles generated from your script.
- **Script History** — All saved scripts with metadata. Re-export any time.
- **Anti-Pattern Log** — Permanent record of structural moves already used. Grows every script. Export/import as JSON.

---

## Project structure

```
app.py                          — Main Streamlit app
data.py                         — Anchor/angle/format/constraint arrays
storage.py                      — Supabase read/write
generator.py                    — Anthropic API calls
exporter.py                     — PDF and Word export
requirements.txt                — Python dependencies
.streamlit/
    secrets.toml.example        — Key template (safe to commit)
```

> `secrets.toml` and `data_store.json` are in `.gitignore` — never committed.

---

## Workflow

1. Open **Divergence Protocol** → roll anchor, angle, constraints → generate brief
2. Send brief to **Script Generator** → generate → export PDF/Word
3. Send script to **Title Machine** → generate titles
4. Save script to history
5. Log the structural moves you used in **Anti-Pattern Log**

After 20 scripts, the ban list forces the AI out of every default pattern it has.
