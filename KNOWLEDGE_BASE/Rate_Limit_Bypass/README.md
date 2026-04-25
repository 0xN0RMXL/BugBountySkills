---
vuln_type: "Rate_Limit_Bypass"
file_type: "readme"
total_reports: "184"
avg_bounty: "200"
max_bounty: "200"
severity_distribution: "critical:1% high:1% medium:3% low:95%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Rate_Limit_Bypass", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Rate Limit Bypass — Complete Hunter's Reference

Rate Limit Bypass represents a critical security oversight in implementing rate limit bypass paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 184
> **Average bounty:** $200
> **Highest bounty on record:** $200 — [Report #2915502](https://hackerone.com/reports/2915502) if 184 > 0 else 'N/A'
> **Dominant severity:** Low (95% of reports)
> **Most affected industry:** saas (15% of reports)
> **OWASP category:** A00:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 6 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 6 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 3 tools with exact commands |
| [[bypasses\|Bypasses]] | 3 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 184 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 184 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like Nextcloud and others in the saas industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.

 This vulnerability class represents a critical breakdown in software architecture.

## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #2915502](https://hackerone.com/reports/2915502) | XVIDEOS | High | $200 | General | Lack of Rate Limiting on Account... |
| 2 | [Report #2748003](https://hackerone.com/reports/2748003) | U.S. Dept Of Defense | Critical | N/A | General | Lack of rate limiting... |
| 3 | [Report #2860983](https://hackerone.com/reports/2860983) | Mozilla | Critical | N/A | General | Denial of Access to Static... |
| 4 | [Report #3085889](https://hackerone.com/reports/3085889) | lichess.org | Critical | N/A | General | Weak Rate Limiting Controls in the... |
| 5 | [Report #3174778](https://hackerone.com/reports/3174778) | Mars | High | N/A | General | No Rate Limiting on Password Attempts... |
| 6 | [Report #1780399](https://hackerone.com/reports/1780399) | MTN Group | Medium | N/A | General | No rate limit in OTP code sending |
| 7 | [Report #3160210](https://hackerone.com/reports/3160210) | Lichess | Medium | N/A | General | Improper Authentication Throttling... |
| 8 | [Report #418767](https://hackerone.com/reports/418767) | HackerOne | Medium | N/A | General | Hacker can bypass 2FA requirement... |
| 9 | [Report #1029723](https://hackerone.com/reports/1029723) | Stripo Inc | Low | N/A | General | No rate limiting for subscribe... |
| 10 | [Report #1040471](https://hackerone.com/reports/1040471) | Khan Academy | Low | N/A | General | Login page vulnerable to... |

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
