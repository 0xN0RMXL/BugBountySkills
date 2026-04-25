---
vuln_type: "API_Security"
file_type: "readme"
total_reports: "409"
avg_bounty: "1022"
max_bounty: "2162"
severity_distribution: "critical:0% high:2% medium:3% low:95%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["API_Security", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# API Security — Complete Hunter's Reference

API Security represents a critical security oversight in implementing api security paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 409
> **Average bounty:** $1,022
> **Highest bounty on record:** $2,162 — [Report #2939104](https://hackerone.com/reports/2939104) if 409 > 0 else 'N/A'
> **Dominant severity:** Low (95% of reports)
> **Most affected industry:** saas (10% of reports)
> **OWASP category:** A00:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 6 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 24 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 5 tools with exact commands |
| [[bypasses\|Bypasses]] | 5 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 409 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 409 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like U.S. Dept Of Defense and others in the saas industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.
## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #2939104](https://hackerone.com/reports/2939104) | Internet Bug Bounty | Medium | $2,162 | General | CVE-2024-56374: ... |
| 2 | [Report #2721478](https://hackerone.com/reports/2721478) | Internet Bug Bounty | High | $505 | General | `std::process::Command`... |
| 3 | [Report #2913312](https://hackerone.com/reports/2913312) | Node.js | High | $400 | General | Usage of unsafe random function in... |
| 4 | [Report #1820146](https://hackerone.com/reports/1820146) | Glassdoor | Critical | N/A | General | Full account takeover without... |
| 5 | [Report #2635315](https://hackerone.com/reports/2635315) | MTN Group | Critical | N/A | General | Yet Another OTP code Leaked in... |
| 6 | [Report #2954547](https://hackerone.com/reports/2954547) | IBM | Critical | N/A | General | Weak credentials found in Jenkins endpoint |
| 7 | [Report #3241102](https://hackerone.com/reports/3241102) | Monero | Critical | N/A | General | Reported Denial of Service |
| 8 | [Report #1544236](https://hackerone.com/reports/1544236) | crm.na1.insightly.com, | High | N/A | General | returnUrl= allow attacker to... |
| 9 | [Report #2412583](https://hackerone.com/reports/2412583) | Rootstock Labs | High | N/A | General | Crafted smart contract can... |
| 10 | [Report #3048061](https://hackerone.com/reports/3048061) | Unknown Program | High | N/A | General | [Xenoblade Chronicles X:... |

## Quick-Start Hunting Checklist

- [ ] Identify all input vectors reflecting into the target application response.
- [ ] Check exactly how special characters (<, >, ", ', `, {) are handled by the server.
- [ ] Attempt out-of-band correlation by submitting external blind payloads (Burp Collaborator).
- [ ] Test the exact same parameter against different content-types or APIs.
- [ ] Attempt HTTP parameter pollution by sending duplicate keys: `?id=1&id=2`.
- [ ] Inject known bypass techniques like null bytes `%00` or URL encoding cascades.
- [ ] Determine the exact framework parsing logic vs validation logic.
- [ ] Escalate to sensitive business logical flows if any reflection/injection succeeds.
- [ ] Leverage account-specific identifiers to check cross-tenant data leakage.
- [ ] Map all unauthenticated and authenticated state boundaries.

## Related Vulnerability Types

This vulnerability frequently appears alongside or enables these types:
- [[SSTI/README|SSTI]] — Server-side template injection can escalate impact constraints
- [[Open_Redirect/README|Open Redirect]] — Often chainable to upgrade impact
- [[CSRF/README|CSRF]] — Can be combined for unauthorized execution of actions
