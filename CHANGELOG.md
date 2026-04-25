# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2025-04-25 (Initial Release)

### Added

- 615 markdown files, ~76,000 lines.
- 4 master system prompts (Claude · ChatGPT · Copilot · local models).
- 174 skill files across all domains:
  - 16 RECON modules
  - 41 WEB vulnerability modules
  - 9 API · 10 LLM/AI · 11 MOBILE · 7 INFRA modules
  - 16 SOURCE_CODE_REVIEW modules
  - 12 AUTOMATION · 8 SCRIPTING · 15 PAYLOADS modules
  - 5 EXPLOIT_DEVELOPMENT · 10 REPORTING · 7 PLATFORM_INTELLIGENCE · 6 MINDSET_STRATEGY modules
- 383 KNOWLEDGE_BASE micro-topic deep dives.
- 51 CHECKLISTS (per-vuln-class + per-recon-stage).
- `DAY1_SETUP.md`, `QUICK_REFERENCE.md`, `INDEX.md`.
- Full tool stack documentation.
- Skill activation trigger system (`RECON MODE`, `WEB MODE`, `PAYLOAD <class>`, etc.).

### Fixed

- Stripped duplicate-sentence/paragraph filler from 272 KB files (PR #2).
  KB directory shrunk from 22 MB to 3.8 MB.

## [Unreleased]

### Planned

- Web3 / Solidity skill files (expanded).
- GraphQL-specific KB entries (20+).
- Custom Nuclei template library.
- RAG setup script for local model deployment.
- GitHub Actions: auto-validate markdown format on PR (added in 1.1).
- Per-program skill files for HackerOne top-50 programs.
- Burp Suite extensions catalog with per-extension hunting workflow.
- Real H1 disclosed-report writeups (top 100 P1s, parsed and indexed).
