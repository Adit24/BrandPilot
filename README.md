# BrandPilot — Codex 48 Round 2 MVP

Evidence-linked brand governance before content goes live.

## Implemented
- Editable brand guidelines, approved terminology, and approved facts.
- Paste-in text review and `.txt` / `.md` upload.
- Rule-based terminology, risky claim, unsupported number, hype, basic accessibility/inclusive language, and readability checks.
- Explainable findings with severity, flagged text, rationale, source/rule, and suggested correction.
- Human decision workflow: Needs review, Changes requested, Approved by human, and reviewer comment.
- Editable revision and re-review flow.
- Local JSON review history.
- Optional Gemini AI analysis when configured; deterministic checks work without an API key.

## Run locally
Python 3.10+ recommended.

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\streamlit.exe run app.py
```

## Optional Gemini integration
Set `GEMINI_API_KEY` in the environment or hosting secrets. Never commit keys.

```powershell
$env:GEMINI_API_KEY="YOUR_KEY_HERE"
.venv\Scripts\streamlit.exe run app.py
```

For Streamlit Community Cloud, add under App settings → Secrets:
```toml
GEMINI_API_KEY = "your-key"
```

## Deploy
1. Push the project to a public GitHub repository.
2. Deploy `app.py` from https://share.streamlit.io/.
3. Configure `GEMINI_API_KEY` in secrets if you want AI analysis; without it, deterministic checks still work.
4. Test the public link in a private/incognito window.

## Limitations
This is a hackathon prototype. Source support matching and accessibility checks are heuristic. It does not guarantee truth, legal compliance, WCAG conformance, or security certification. JSON persistence is intended for a single-user demo. Human review is required.
