---
vuln_type: "XSS"
file_type: "readme"
total_reports: "1563"
avg_bounty: "424"
max_bounty: "3800"
severity_distribution: "critical:1% high:2% medium:97% low:0%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-79", "CWE-80"]
last_updated: "2026-04-09"
tags: ["XSS", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# XSS — Complete Hunter's Reference

XSS exists wherever user-controlled input reaches the DOM or HTTP response without sufficient context-aware encoding. In practice this means anywhere the application reflects, stores, or constructs HTML, JavaScript, URLs, or CSS using attacker-controlled values — which in real programs is far more surface area than most developers realize.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 1563
> **Average bounty:** $424
> **Highest bounty on record:** $3,800 — [Report #1695604](https://hackerone.com/reports/1695604) if 1563 > 0 else 'N/A'
> **Dominant severity:** Medium (95% of reports)
> **Most affected industry:** ecommerce (22% of reports)
> **OWASP category:** A03:2021 — Vulnerability
> **Most common CWE:** CWE-79 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 16 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 277 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 8 tools with exact commands |
| [[bypasses\|Bypasses]] | 5 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 1563 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 1563 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like U.S. Dept Of Defense and others in the ecommerce industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.


## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #1695604](https://hackerone.com/reports/1695604) | cdn.shopify.com | High | $3,800 | General | DoS Vulnerability via Cache... |
| 2 | [Report #1935628](https://hackerone.com/reports/1935628) | GitLab | Low | $1,060 | XSS via File Upload | HTML injection possible with soft... |
| 3 | [Report #2521419](https://hackerone.com/reports/2521419) | Basecamp | Critical | $1,000 | Stored XSS | Stored XSS on trix editor version... |
| 4 | [Report #1941767](https://hackerone.com/reports/1941767) | MetaMask | Critical | $800 | CSP Bypass XSS | MetaMask Browser (on Android) does... |
| 5 | [Report #2520694](https://hackerone.com/reports/2520694) | Internet Bug Bounty | Low | $568 | General | Possible XSS... |
| 6 | [Report #3211031](https://hackerone.com/reports/3211031) | Cloudflare Public Bug Bou | Medium | $550 | General | `use-mcp`'s... |
| 7 | [Report #2931636](https://hackerone.com/reports/2931636) | Internet Bug Bounty | Medium | $541 | General | ActionView sanitize... |
| 8 | [Report #2931639](https://hackerone.com/reports/2931639) | Internet Bug Bounty | Medium | $541 | General | ActionView sanitize... |
| 9 | [Report #2931688](https://hackerone.com/reports/2931688) | Internet Bug Bounty | Medium | $541 | XSS via File Upload | ActionView sanitize... |
| 10 | [Report #2931691](https://hackerone.com/reports/2931691) | Internet Bug Bounty | Medium | $541 | General | ActionView sanitize... |

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
