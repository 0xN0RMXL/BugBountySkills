# BugBountySkills

> An obsessive, expert-tier knowledge base + AI skill system for professional bug bounty hunting, security research, and penetration testing.

**615 markdown files. ~76,000 lines.** Recon → Vulnerabilities → Exploitation → Reporting → Mindset, all source-backed and copy-paste ready.

---

## Table of Contents

- [What this is](#what-this-is)
- [Who it's for](#who-its-for)
- [What's inside](#whats-inside)
- [Repository layout](#repository-layout)
- [How to use it with each AI agent](#how-to-use-it-with-each-ai-agent)
  - [Claude (recommended)](#claude-recommended)
  - [ChatGPT](#chatgpt)
  - [GitHub Copilot](#github-copilot)
  - [Local models (Ollama, LM Studio, etc.)](#local-models-ollama-lm-studio-etc)
  - [Cursor / Continue.dev / Aider](#cursor--continuedev--aider)
- [Skill activation triggers](#skill-activation-triggers)
- [Without an AI — pure docs](#without-an-ai--pure-docs)
- [Tool stack](#tool-stack)
- [Daily hunt workflow](#daily-hunt-workflow)
- [Updating the system](#updating-the-system)
- [Quality bar](#quality-bar)
- [References](#references)
- [License & disclaimer](#license--disclaimer)

---

## What this is

A modular markdown repository designed to:

1. **Be loaded into any LLM as a skill system** — give your AI assistant elite-tier bug bounty expertise on demand.
2. **Be used as a personal Obsidian / Git knowledge vault** — every technique, payload, checklist, and methodology in one place.
3. **Be runnable as documentation** — every command, payload, and code snippet is copy-paste-ready.

It is **not**:
- A scanner / automated tool (it documents tools; it doesn't execute them for you)
- An exploit framework (it documents techniques; PoCs are your responsibility)
- Generic OWASP boilerplate (every file is source-backed and operationally specific)

---

## Who it's for

- **Bug bounty hunters** on HackerOne / Bugcrowd / Intigriti / YesWeHack / Immunefi
- **Penetration testers** doing web / API / mobile / cloud / source-code engagements
- **Security researchers** doing variant analysis, vuln research, exploit dev
- **Red teamers** building offensive playbooks
- **AppSec engineers** stress-testing their own products

---

## What's inside

| Section | Files | What |
|---------|-------|------|
| `MASTER_SYSTEM_PROMPTS/` | 4 | Drop-in system prompts for Claude, ChatGPT, Copilot, local models |
| `SKILL_FILES/` | 174 | Loadable AI skill modules — recon, every vuln class, SCR, automation, scripting, payloads, exploit dev, reporting, platforms, mindset |
| `KNOWLEDGE_BASE/` | 383 | Per-topic deep dives (HTTP smuggling, SSRF→IMDS, JWT alg:none, race conditions, prototype pollution, etc.) |
| `CHECKLISTS/` | 51 | Per-vuln-class and per-recon-stage operational checklists |
| `REFERENCE/` | — | Source-PDF text extracts + browser extensions list |
| `INDEX.md` | 1 | Full navigation tree of the entire repo |
| `QUICK_REFERENCE.md` | 1 | One-page operational cheatsheet |
| `DAY1_SETUP.md` | 1 | How to deploy and start hunting |

**Coverage:**

- **Recon** — passive/active subdomain, DNS, JS analysis, Wayback, port scan, fingerprinting, GitHub/Google/Shodan dorks, cloud recon (AWS/GCP/Azure), mobile app recon, API discovery, content discovery, full automation pipeline
- **Web vulnerabilities** — XSS (all contexts), SQLi (all DBs), SSRF, SSTI (all engines), XXE, RCE, LFI/RFI, open redirect, CORS, CSRF, clickjacking, IDOR/BOLA/BFLA, auth bypass, 2FA bypass, JWT, OAuth, SAML, race conditions, mass assignment, HTTP request smuggling, HPP, cache poisoning, web cache deception, business logic, subdomain takeover, dependency confusion, prototype pollution, deserialization, file upload, GraphQL, WebSocket, postMessage, DOM clobbering, iframe attacks, CSP bypass, WAF bypass, Cloudflare bypass, rate limiting bypass, account takeover chains, host header attacks
- **API** — auth/authz attacks, mass assignment, REST/GraphQL/gRPC, fuzzing methodology
- **LLM/AI** — prompt injection (direct + indirect), jailbreaks, data exfil, plugin/tool abuse, RAG poisoning, supply chain, model extraction, DoS, full LLM testing methodology
- **Mobile** — Android (static, dynamic, intents, deep links, WebView), iOS (static, dynamic, URL schemes), mobile API, certificate pinning bypass, mobile auth
- **Infra** — cloud misconfig (AWS/GCP/Azure), S3, Kubernetes, Docker, network pentest
- **Source Code Review** — Python, JS/Node, Java/Spring, PHP, Ruby/Rails, Go, Rust, .NET/C#, C++, Solidity, dangerous functions, secrets detection, dependency analysis, IaC, CI/CD
- **Automation** — program/scope/asset monitoring, recon pipelines, Nuclei templates, ffuf, Burp, notifications, VPS setup, Docker, workflow orchestration, custom tooling
- **Scripting** — Bash / Python / Go / JS / Rust / Ruby hunting scripts, one-liner collection, regex patterns
- **Payloads** — XSS / SQLi / SSRF / SSTI / XXE / RCE / LFI / open redirect / CSRF / JWT / WAF bypass / polyglots / prototype pollution / deserialization / prompt injection (PayloadsAllTheThings style)
- **Exploit dev** — PoC writing, chain building, impact amplification, mitigation bypass, zero-day research
- **Reporting** — methodology, CVSS, impact statements, PoC docs, remediation, H1/Bugcrowd/Intigriti templates, email disclosure, escalation/dispute templates
- **Platform intelligence** — H1, Bugcrowd, Intigriti, YesWeHack, Immunefi specifics + program selection + triage communication
- **Mindset/strategy** — target selection, prioritization, time management, dupe avoidance, staying ahead of patches, continuous learning system

---

## Repository layout

```
BugBountySkills/
├── README.md                       (this file)
├── INDEX.md                        (full navigation)
├── QUICK_REFERENCE.md              (1-page cheatsheet)
├── DAY1_SETUP.md                   (deploy + start hunting)
│
├── MASTER_SYSTEM_PROMPTS/
│   ├── claude_master_system_prompt.md
│   ├── chatgpt_master_system_prompt.md
│   ├── github_copilot_instructions.md
│   └── local_model_system_prompt.md
│
├── SKILL_FILES/
│   ├── 00_core_identity_and_behavior.md
│   ├── RECON/                      (16 files)
│   ├── VULNERABILITIES/
│   │   ├── WEB/                    (41 files)
│   │   ├── API/                    (9)
│   │   ├── LLM_AI/                 (10)
│   │   ├── MOBILE/                 (11)
│   │   └── INFRA/                  (7)
│   ├── SOURCE_CODE_REVIEW/         (16)
│   ├── AUTOMATION/                 (12)
│   ├── SCRIPTING/                  (8)
│   ├── PAYLOADS/                   (15)
│   ├── EXPLOIT_DEVELOPMENT/        (5)
│   ├── REPORTING/                  (10)
│   ├── PLATFORM_INTELLIGENCE/      (7)
│   └── MINDSET_STRATEGY/           (6)
│
├── KNOWLEDGE_BASE/                 (383 micro-topic deep dives)
├── CHECKLISTS/                     (51 operational checklists)
└── REFERENCE/                      (source PDFs as text + extension list)
```

---

## How to use it with each AI agent

### Claude (recommended)

Best fit. Long context, strong technical depth, follows skill triggers reliably.

**Option A — Claude Project (best):**
1. https://claude.ai → Projects → **+ New project** → name it `BugBounty Hunter Oracle`.
2. **Project instructions / Custom instructions** → paste the entire contents of [`MASTER_SYSTEM_PROMPTS/claude_master_system_prompt.md`](MASTER_SYSTEM_PROMPTS/claude_master_system_prompt.md).
3. **Project knowledge** → upload the markdown files. Recommended subset to fit within knowledge limits:
   - All of `SKILL_FILES/PAYLOADS/`
   - All of `SKILL_FILES/RECON/`
   - All of `SKILL_FILES/VULNERABILITIES/WEB/` and `/API/`
   - All of `KNOWLEDGE_BASE/` (any 50-100 most-relevant)
   - `INDEX.md`, `QUICK_REFERENCE.md`
4. Use Claude **Sonnet 4.x** or **Opus 4.x**.
5. Activate skills by typing trigger phrases: `RECON MODE`, `PAYLOAD xss`, `REPORT MODE`, etc. (See [Skill activation triggers](#skill-activation-triggers).)

**Option B — Claude Code (CLI):**
```bash
git clone https://github.com/0xN0RMXL/BugBountySkills.git
cd BugBountySkills
claude  # opens with repo as context
```
Then ask: "Load `MASTER_SYSTEM_PROMPTS/claude_master_system_prompt.md` as your system prompt and use the rest of this repo as your skill library."

**Option C — Anthropic API:**
```python
import anthropic
client = anthropic.Anthropic()
with open("MASTER_SYSTEM_PROMPTS/claude_master_system_prompt.md") as f:
    system = f.read()
msg = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=8000,
    system=system,
    messages=[{"role":"user","content":"RECON MODE — give me a passive recon plan for *.example.com"}]
)
```

---

### ChatGPT

**Option A — Custom GPT (best):**
1. https://chatgpt.com/gpts/editor → **Create**.
2. **Instructions** → paste [`MASTER_SYSTEM_PROMPTS/chatgpt_master_system_prompt.md`](MASTER_SYSTEM_PROMPTS/chatgpt_master_system_prompt.md).
3. **Knowledge** → upload markdown files (max 20 files / 512MB total in standard GPT). Prioritize `INDEX.md`, payloads, and the WEB/API skill files.
4. **Capabilities** → Web Browsing ON, Code Interpreter ON.
5. Save as private GPT. Use trigger phrases as with Claude.

**Option B — Custom Instructions (free / Plus):**
1. Settings → Personalization → Custom Instructions.
2. **About you** → "I am a professional bug bounty hunter…"
3. **How to respond** → paste a condensed version of `chatgpt_master_system_prompt.md`.

**Option C — OpenAI API:**
```python
from openai import OpenAI
client = OpenAI()
with open("MASTER_SYSTEM_PROMPTS/chatgpt_master_system_prompt.md") as f:
    system = f.read()
resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role":"system","content":system},
        {"role":"user","content":"PAYLOAD xss — give me top 10 polyglots"}
    ]
)
```

---

### GitHub Copilot

Auto-loads instructions from `.github/copilot-instructions.md` in your **own** repo.

```bash
# In YOUR target repo (not this one):
mkdir -p .github
cp /path/to/BugBountySkills/MASTER_SYSTEM_PROMPTS/github_copilot_instructions.md .github/copilot-instructions.md
git add .github/copilot-instructions.md
git commit -m "Add bug bounty skill instructions for Copilot"
```

Now Copilot will:
- Suggest hunting scripts in correct languages
- Flag vulnerable code patterns when reading source
- Generate Nuclei templates from observed patterns
- Auto-suggest payloads in test files

For **Copilot Chat** workspace mode, also add `BugBountySkills/` as a workspace reference.

---

### Local models (Ollama, LM Studio, etc.)

The local-model prompt is **aggressively compressed** for smaller context windows.

**Ollama:**
```bash
# Create a Modelfile
cat > Modelfile <<'EOF'
FROM llama3.1:70b
SYSTEM """
$(cat MASTER_SYSTEM_PROMPTS/local_model_system_prompt.md)
"""
PARAMETER temperature 0.3
PARAMETER num_ctx 32768
EOF

ollama create bbai -f Modelfile
ollama run bbai
```

**LM Studio:**
1. Load any 70B+ model (Llama 3.1, Qwen 2.5, Mixtral 8x22B).
2. Set context to ≥32k.
3. Paste `local_model_system_prompt.md` into System Prompt field.

**RAG over the full repo (recommended for local):**
```bash
pip install chromadb langchain sentence-transformers
# index every .md file in this repo into Chroma
# use llama.cpp / Ollama as LLM backend
# query with skill triggers; RAG retrieves relevant skill files
```

A starter RAG script is in [`SKILL_FILES/AUTOMATION/custom_tool_development.md`](SKILL_FILES/AUTOMATION/custom_tool_development.md).

---

### Cursor / Continue.dev / Aider

**Cursor:**
1. Clone this repo into your workspace (or as a sibling folder).
2. Cursor Settings → **Rules for AI** → paste `claude_master_system_prompt.md`.
3. Use `@BugBountySkills` in chat to reference the repo.

**Continue.dev:**
- Edit `~/.continue/config.json` → add `customCommands` for `RECON MODE`, `PAYLOAD <class>`, etc., each pointing at the relevant skill file.

**Aider:**
```bash
aider --read MASTER_SYSTEM_PROMPTS/claude_master_system_prompt.md \
      --read SKILL_FILES/00_core_identity_and_behavior.md \
      <files-you're-reviewing>
```

---

## Skill activation triggers

Once the system prompt is loaded, activate skill modules by typing:

| Trigger | Loads |
|---------|-------|
| `RECON MODE` | All of `SKILL_FILES/RECON/` |
| `WEB MODE` | All of `SKILL_FILES/VULNERABILITIES/WEB/` |
| `API MODE` | All of `SKILL_FILES/VULNERABILITIES/API/` |
| `LLM MODE` | All of `SKILL_FILES/VULNERABILITIES/LLM_AI/` |
| `MOBILE MODE` | All of `SKILL_FILES/VULNERABILITIES/MOBILE/` |
| `INFRA MODE` | All of `SKILL_FILES/VULNERABILITIES/INFRA/` |
| `SCR MODE` | All of `SKILL_FILES/SOURCE_CODE_REVIEW/` |
| `PAYLOAD <class>` | `SKILL_FILES/PAYLOADS/<class>_payloads*.md` |
| `EXPLOIT MODE` | All of `SKILL_FILES/EXPLOIT_DEVELOPMENT/` |
| `REPORT MODE` | All of `SKILL_FILES/REPORTING/` |
| `STRATEGY MODE` | All of `SKILL_FILES/MINDSET_STRATEGY/` |
| `H1 MODE` / `BC MODE` / `INTI MODE` | Platform-specific tactics |

Example session:
```
You: RECON MODE — *.acme.tld, recently added to scope
AI: [follows passive_recon → subdomain_enumeration → asset_discovery skill files,
     produces a runnable subfinder/httpx/nuclei pipeline tailored to the target]

You: PAYLOAD xss — context: HTML attribute, single-quote escape, CSP script-src 'self'
AI: [retrieves attribute-context payloads + 'self' CSP bypass techniques]

You: REPORT MODE — IDOR on /api/v2/users/:id/invoices
AI: [generates HackerOne-ready report following hackerone_report_template.md]
```

---

## Without an AI — pure docs

You don't need an AI to use this. Treat it as an Obsidian vault or Git wiki:

```bash
git clone https://github.com/0xN0RMXL/BugBountySkills.git
cd BugBountySkills

# Open as Obsidian vault
obsidian --vault $PWD

# Or just grep
rg -l "ssrf" KNOWLEDGE_BASE/
rg "alg:none" SKILL_FILES/
```

Start with [`INDEX.md`](INDEX.md) for navigation, [`QUICK_REFERENCE.md`](QUICK_REFERENCE.md) for one-page cheatsheet, [`DAY1_SETUP.md`](DAY1_SETUP.md) for environment setup.

---

## Tool stack

The skill files assume the following toolchain (full install in `SKILL_FILES/AUTOMATION/vps_setup_hunting.md`):

```
Recon:        subfinder, amass, assetfinder, chaos, httpx, dnsx, naabu, masscan,
              nmap, katana, hakrawler, gau, waybackurls, gowitness, aquatone,
              ffuf, feroxbuster, dirsearch, arjun, paramspider, x8

Vuln scan:    nuclei, dalfox, sqlmap, kxss, gf, qsreplace, anew, notify

Web:          Burp Suite Pro + Param Miner + Turbo Intruder + DOM Invader +
              HTTP Request Smuggler + Autorize + JWT Editor

Mobile:       jadx, apktool, frida, objection, mobsf, Burp + Magisk root

Cloud:        aws-cli, gcloud, az, cloud_enum, ScoutSuite, prowler, kube-hunter

SCR:          semgrep, codeql, trufflehog, gitleaks

LLM:          garak, promptfoo, custom prompt-injection harnesses

Web3:         foundry, slither, mythril, echidna
```

---

## Daily hunt workflow

```
06:00  Pipeline output review (overnight notify alerts)
07:00  Deep manual hunt on prioritized target (per RECON + WEB skill files)
10:00  Write reports for verified bugs (REPORTING skill files)
13:00  Pivot to second target / fuzz queue
16:00  Triage replies, payouts, learning
```

See [`SKILL_FILES/MINDSET_STRATEGY/time_management_hunting.md`](SKILL_FILES/MINDSET_STRATEGY/time_management_hunting.md) for details.

---

## Updating the system

This repo is designed to grow. Recommended additions over time:

- New techniques you learn → append to relevant `KNOWLEDGE_BASE/<topic>.md`
- New tools → add to `SKILL_FILES/AUTOMATION/` or `/SCRIPTING/`
- New chains → add to `SKILL_FILES/EXPLOIT_DEVELOPMENT/exploit_chain_building.md`
- New disclosed reports → add as case studies under `KNOWLEDGE_BASE/`
- Quarterly: bump skill file `Version:` headers, append change log

Contributions welcome via PR.

---

## Quality bar

Every file in this repo aims to meet:

1. **No generic content** — specific, technical, actionable
2. **Source-backed** — references uploaded sources or known public references
3. **Tool-complete** — exact tool, exact command, exact flags
4. **Payload-ready** — real, working payloads (not placeholders)
5. **Chain-aware** — shows how to chain for higher impact
6. **Bypass-included** — defenses + their bypasses documented inline
7. **Platform-calibrated** — H1/BC/Intigriti/YWH/Immunefi nuances flagged
8. **Massive** — exhaustive over concise where possible
9. **Copy-paste ready** — commands and payloads work as-is
10. **Continuously updatable** — append new techniques without restructuring

---

## References

This system synthesizes knowledge from:

- **PortSwigger Web Security Academy** — labs and research blog
- **HackerOne Hacktivity** — top P1 disclosed reports
- **Bugcrowd VRT** + **PayloadsAllTheThings**
- **The Web Application Hacker's Handbook** (WAHH) — Stuttard / Pinto
- **Bug Bounty Bootcamp** — Vickie Li
- **The Tangled Web** — Michal Zalewski
- **JavaScript for Hackers** — Gareth Heyes
- **Black Hat Python** — Justin Seitz
- **zseano's methodology**, **jhaddix Bug Hunter's Methodology Day 1 + 2**
- **NahamSec / Stök / IppSec / LiveOverflow** content
- **Trail of Bits / Doyensec / NCC Group** research
- **OWASP Cheat Sheet Series** + Testing Guide
- Community Discord/Twitter — @albinowax, @garethheyes, @james_kettle, @samwcyo, @nahamsec

Each skill file lists its specific references at the bottom.

---

## License & disclaimer

**License:** Use however you want for legal security research, bug bounty hunting, authorized penetration testing, and defensive security work.

**Disclaimer:** Everything in this repo is for use against systems you have **explicit written authorization** to test (your own, your employer's, or a public bug bounty program with you in scope). Unauthorized testing is illegal in most jurisdictions. The author / contributors take no responsibility for misuse.

Stay in scope. Hack ethically. Report responsibly.

---

**Happy hunting.**

— Maintained by [@0xN0RMXL](https://github.com/0xN0RMXL)
