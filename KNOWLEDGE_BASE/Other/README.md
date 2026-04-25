---
vuln_type: "Other"
file_type: "readme"
total_reports: "3258"
avg_bounty: "1465"
max_bounty: "12500"
severity_distribution: "critical:0% high:0% medium:3% low:97%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Other", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Other — Complete Hunter's Reference

Other represents a critical security oversight in implementing other paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 3258
> **Average bounty:** $1,465
> **Highest bounty on record:** $12,500 — [Report #3113398](https://hackerone.com/reports/3113398) if 3258 > 0 else 'N/A'
> **Dominant severity:** Low (97% of reports)
> **Most affected industry:** saas (10% of reports)
> **OWASP category:** A00:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 6 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 248 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 8 tools with exact commands |
| [[bypasses\|Bypasses]] | 9 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 3258 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 3258 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like Nextcloud and others in the saas industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.

 This vulnerability class represents a critical breakdown in software architecture.

## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #3113398](https://hackerone.com/reports/3113398) | HackerOne | High | $12,500 | General | Internal Access to Hackerone... |
| 2 | [Report #2795558](https://hackerone.com/reports/2795558) | Internet Bug Bounty | Medium | $2,162 | General | CVE-2024-41990:... |
| 3 | [Report #2881639](https://hackerone.com/reports/2881639) | Internet Bug Bounty | Medium | $2,162 | General | CVE-2024-45230 -... |
| 4 | [Report #2645836](https://hackerone.com/reports/2645836) | Internet Bug Bounty | Medium | $2,142 | General | [CVE-2024-35176] DoS... |
| 5 | [Report #2658447](https://hackerone.com/reports/2658447) | Internet Bug Bounty | Medium | $2,142 | General | CVE-2024-7347: Buffer... |
| 6 | [Report #2806356](https://hackerone.com/reports/2806356) | Cosmos | Low | $2,000 | General | Heap-Buffer-Overread in... |
| 7 | [Report #2987782](https://hackerone.com/reports/2987782) | Internet Bug Bounty | High | $541 | General | Possible DoS by memory... |
| 8 | [Report #3013913](https://hackerone.com/reports/3013913) | Internet Bug Bounty | Medium | $541 | General | [CVE-2025-27219] Denial... |
| 9 | [Report #3108869](https://hackerone.com/reports/3108869) | Internet Bug Bounty | Medium | $541 | General | Denial of Service by... |
| 10 | [Report #3002543](https://hackerone.com/reports/3002543) | Internet Bug Bounty | High | $505 | General | CVE-2024-43398: DoS... |

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
