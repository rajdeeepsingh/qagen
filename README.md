# QaGen — AI-Powered QA Automation

> Generate test cases with NVIDIA NIM and run API tests with pytest

## What it does
- Generates test cases from feature descriptions using NVIDIA NIM
- Runs automated API tests with pytest (JSONPlaceholder + ReqRes)
- CI via GitHub Actions on push/PR
- n8n + GitHub webhooks (coming soon)

## Tech Stack
- Python, pytest, requests
- Allure (test reporting)
- NVIDIA NIM (OpenAI-compatible API)
- GitHub Actions (CI)
- n8n (orchestration) — planned

## Project Status
Phase 3 in progress — AI test case generation working with NVIDIA

## Roadmap
- [x] Project setup
- [x] Phase 1: Manual API testing with requests
- [x] Phase 2: Automated tests with pytest
- [x] GitHub Actions CI pipeline
- [x] Phase 3: AI test case generation (NVIDIA NIM)
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

Add your NVIDIA API key to `.env`:
```env
NVIDIA_API_KEY=nvapi-your_key_here
```

Generate test cases:
```bash
python scripts/generate_tests.py
```

## Author
Built by [Rajdeep Singh] while learning Python
