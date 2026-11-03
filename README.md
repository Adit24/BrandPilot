# BrandPilot — Codex 48 Round 3

**Evidence-linked brand governance before content goes live.**

BrandPilot is a Streamlit-based brand governance prototype that reviews marketing content against configurable brand guidelines, approved terminology and approved facts. It combines deterministic content checks, visual asset screening and human review with an audit trail.

## Features implemented

### 1. Content review
- Configure brand name, guidelines, preferred terminology and approved facts.
- Paste content or upload PDF, DOCX, TXT and Markdown files.
- Extract text from supported documents, retaining PDF page markers.
- Detect terminology drift, unsupported promotional claims, numeric claims, hype language, basic accessibility issues and readability concerns.
- Display severity, flagged text, rationale, evidence/rule, suggested correction and confidence.
- Edit a draft and submit a revised version for a new review.

### 2. Visual brand and asset verification
- Upload an approved reference logo and a marketing creative.
- Compare image features using OpenCV.
- Display feature-match score, good matches and reference feature count.
- Flag potential logo matches for human verification.

This is automated visual screening, not definitive logo recognition or brand-compliance certification.

### 3. Review workflow and audit trail
- Reviewer identity fields for reviewer name and role (Creator, Reviewer or Admin).
- Human decisions: Needs review, Changes requested and Approved by human.
- Optional reviewer comments.
- Review history stored in local JSON.
- Review decision events recorded in a SQLite audit database, including reviewer, role, decision, comment and timestamp.

**Access-control limitation:** Reviewer names and roles are currently self-declared. The prototype does not implement authenticated accounts, permission enforcement or isolated multi-user workspaces. SQLite persistence is local and is not a managed production database.

## Technical architecture

| Layer | Technology | Purpose |
|---|---|---|
| User interface | Streamlit | Dashboard and review workflow |
| Content analysis | Python, regular expressions | Deterministic brand checks |
| Document ingestion | pypdf, python-docx | PDF and DOCX text extraction |
| Visual screening | OpenCV, Pillow | Logo feature comparison |
| Review history | JSON | Local review records |
| Audit trail | SQLite | Decision-event records |
| Optional AI | Google GenAI SDK | Additional contextual analysis when API access is configured |

### Project structure

```text
BrandPilot/
├── app.py
├── requirements.txt
├── README.md
├── services/
│   ├── document_reader.py
│   └── visual_checker.py
├── database/
│   └── audit_store.py
├── modules/
├── uploads/
└── .gitignore
```

## Run locally

Requirements: Python 3.10 or later.

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\streamlit.exe run app.py
```

Open the local URL displayed by Streamlit, usually `http://localhost:8501`.

## Optional AI integration

Gemini analysis is optional. Without a working API key, deterministic checks continue to run.

Set `GEMINI_API_KEY` through your environment or hosting secrets. Never commit API keys or confidential data.

AI integration should be considered unavailable unless a successful API request has been verified.

## Testing performed

- Launched the application locally.
- Verified PDF document upload and extracted text appearing in the editable draft.
- Verified document page markers in extracted PDF content.
- Uploaded an approved logo and a marketing creative and ran visual comparison.
- Verified feature-match metrics and human-verification warning.
- Created review records and checked review history.
- Changed review decisions and entered reviewer comments.
- Verified that changing fields does not create audit entries; saving a decision creates one audit event.
- Verified SQLite audit records contain reviewer identity, role, decision, comment and timestamp.

Testing is a prototype-level manual verification, not a formal security, accessibility or performance audit.

## Known limitations

- Content checks use heuristics and can produce false positives or miss issues.
- Visual feature matching can be affected by resizing, cropping, rotation and image quality.
- A high visual match score does not certify brand compliance; a low score does not prove an asset is missing.
- PDF extraction depends on selectable text; scanned documents may require OCR.
- Reviewer roles are not authenticated or enforced.
- JSON and SQLite files are local prototype storage; hosted deployments may require external persistent storage.
- Accessibility checks do not establish WCAG conformance.
- Human review remains necessary before publication.

## Improvements and roadmap

### Delivered in Round 3
1. **Visual Brand and Asset Verification:** Implemented reference-logo versus creative feature comparison.
2. **Document Ingestion and Content Workflow:** Implemented PDF, DOCX, TXT and Markdown ingestion into the existing review workflow.
3. **Review Audit Trail:** Implemented SQLite-backed decision-event records and reviewer identity/role fields. Full authentication, role enforcement and workspace isolation remain future work.

### Future roadmap
- Authentication and permission-enforced Creator, Reviewer and Admin roles.
- Isolated brand workspaces and managed database persistence.
- OCR for scanned PDFs and richer document-format support.
- More robust logo detection, approved asset libraries and brand-colour checks.
- Controlled webhook/API integration with external content workflows.
- Expanded automated testing and deployment monitoring.

## Project links

- **GitHub:** https://github.com/Adit24/BrandPilot
- **Live application:** https://brandpilot-adit-codex48.streamlit.app/

---

**BrandPilot — Codex 48 Round 3**

Human review is required before publication. Automated checks assist reviewers; they do not replace them.