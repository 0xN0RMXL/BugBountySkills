# QUICK REFERENCE — BugBounty-AI-System

One-page operational cheatsheet. Bookmark this.

## ACTIVATION TRIGGERS (load corresponding skill)

| Trigger | Skill loaded |
|---------|--------------|
| `RECON MODE` | SKILL_FILES/RECON/* |
| `WEB MODE` | SKILL_FILES/VULNERABILITIES/WEB/* |
| `API MODE` | SKILL_FILES/VULNERABILITIES/API/* |
| `LLM MODE` | SKILL_FILES/VULNERABILITIES/LLM_AI/* |
| `MOBILE MODE` | SKILL_FILES/VULNERABILITIES/MOBILE/* |
| `INFRA MODE` | SKILL_FILES/VULNERABILITIES/INFRA/* |
| `SCR MODE` | SKILL_FILES/SOURCE_CODE_REVIEW/* |
| `PAYLOAD <class>` | SKILL_FILES/PAYLOADS/<class>.md |
| `EXPLOIT MODE` | SKILL_FILES/EXPLOIT_DEVELOPMENT/* |
| `REPORT MODE` | SKILL_FILES/REPORTING/* |
| `STRATEGY MODE` | SKILL_FILES/MINDSET_STRATEGY/* |

## HUNT WORKFLOW

```
1. RECON → enumerate, fingerprint, prioritize (16_recon_automation_pipeline.md)
2. ANALYSIS → map auth model, parameters, surfaces (BHM Day 2)
3. HUNT → manual + nuclei + fuzzing on prioritized assets
4. EXPLOIT → PoC + chain to maximize impact
5. REPORT → impact, repro, remediation
6. FOLLOWUP → respond fast to triage, escalate respectfully
```

## TOP-VALUE ENDPOINTS

- /api/admin/*, /api/internal/*
- /oauth/authorize, /oauth/token, /sso/*
- /upload, /import, /export, /backup
- /search, /filter, /sort, /preview
- /webhook, /callback
- /graphql, /api/v[0-9]+/*
- /actuator/* (Spring), /admin (most CMSes)
- /.git, /.env, /.well-known/*

## TOP-VALUE PARAMETERS

id, user, account, org, tenant, redirect, next, return, callback, url, file, path, template, view, cmd, exec, eval, query, search, q, filter, email, role, permission, is_admin, _method, _csrf, format, output

## CRITICAL CHAINS

| Chain | Outcome |
|-------|---------|
| XSS in admin → ATO | Critical |
| SSRF → IMDS → AWS keys | Critical |
| Subdomain takeover + cookie scope | Critical (ATO) |
| Open redirect + OAuth | Critical (ATO) |
| Race + IDOR | Critical (priv esc / fraud) |
| PP + gadget | RCE |
| LFI + log poisoning | RCE |
| File upload polyglot + Web Apache | RCE |

## DAILY TOOL STACK

```
subfinder | httpx | nuclei | katana | gau | dalfox | sqlmap | ffuf | Burp Pro | Frida | Semgrep | trufflehog
```

## REFERENCES (top 10)

1. PortSwigger Web Security Academy
2. HackerOne Hacktivity (top P1 disclosed)
3. PayloadsAllTheThings
4. PortSwigger Research Blog
5. zseanos-methodology.pdf
6. Bug Hunters Methodology Day 1 + 2 (jhaddix)
7. Web Application Hacker's Handbook
8. JavaScript for Hackers (Gareth Heyes)
9. The Tangled Web (Michal Zalewski)
10. Black Hat Python (Justin Seitz)
