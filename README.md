# QaGen — AI-Powered QA Automation

> Automatically generate test cases and run API tests using Claude AI + Python

## What it does
- Generates test cases from API descriptions using Claude AI (planned)
- Runs automated API tests with pytest
- Integrates with GitHub via n8n webhooks (coming soon)

## Tech Stack
- Python, pytest, requests
- Allure (test reporting)
- Claude API (Anthropic) — planned
- n8n (orchestration) — planned
- GitHub Actions (CI) — planned

## Project Status
Phase 2 complete — automated API tests for JSONPlaceholder and ReqRes

## Roadmap
- [x] Project setup
- [x] Phase 1: Manual API testing with requests
- [x] Phase 2: Automated tests with pytest
- [ ] Phase 3: AI test case generation (Claude API)
- [ ] Phase 4: n8n + GitHub automation pipeline

## Getting Started
```bash
git clone https://github.com/rajdeeepsingh/qagen.git
cd qagen
copy .env.example .env
python -m pip install -r requirements.txt
python -m pytest tests/ -v
```

On macOS/Linux, use `cp .env.example .env` instead of `copy`.

## Author
Built by [Rajdeep Singh] while learning Python
