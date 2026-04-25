---
vuln_type: "CSRF"
file_type: "readme"
total_reports: "289"
avg_bounty: "350"
max_bounty: "500"
severity_distribution: "critical:1% high:2% medium:4% low:93%"
owasp_categories: ["A04:2021"]
common_cwe: ["CWE-352"]
last_updated: "2026-04-09"
tags: ["CSRF", "web", "api", "A04", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# CSRF — Complete Hunter's Reference

Cross-Site Request Forgery leverages the browser's automatic inclusion of ambient credentials (like cookies). The attacker crafts a state-changing request and tricks an authenticated victim into executing it, letting the attacker inherit their capabilities.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 289
> **Average bounty:** $350
> **Highest bounty on record:** $500 — [Report #3253725](https://hackerone.com/reports/3253725) if 289 > 0 else 'N/A'
> **Dominant severity:** Low (93% of reports)
> **Most affected industry:** crypto (16% of reports)
> **OWASP category:** A04:2021 — Vulnerability
> **Most common CWE:** CWE-352 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 10 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 6 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 3 tools with exact commands |
| [[bypasses\|Bypasses]] | 3 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 289 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 289 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like U.S. Dept Of Defense and others in the crypto industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.
## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #3253725](https://hackerone.com/reports/3253725) | Brave Software | High | $500 | General | SameSite restrictions are... |
| 2 | [Report #2513333](https://hackerone.com/reports/2513333) | Mozilla | Low | $500 | General | csrftoken not unique to session or... |
| 3 | [Report #1668489](https://hackerone.com/reports/1668489) | crm.na1.insightly.com | Medium | $50 | General | CSRF vulnerability allows... |
| 4 | [Report #2652603](https://hackerone.com/reports/2652603) | U.S. Dept Of Defense | Critical | N/A | State-Changing CSRF | CSRF Attack on... |
| 5 | [Report #2697588](https://hackerone.com/reports/2697588) | U.S. Dept Of Defense | Critical | N/A | State-Changing CSRF | CSRF Attack leads to... |
| 6 | [Report #2919623](https://hackerone.com/reports/2919623) | IBM | Critical | N/A | General | There is a POST based CSRF issue over... |
| 7 | [Report #2699029](https://hackerone.com/reports/2699029) | U.S. Dept Of Defense | High | N/A | General | CSRF leads to Account... |
| 8 | [Report #2712857](https://hackerone.com/reports/2712857) | U.S. Dept Of Defense | High | N/A | General | CSRF leads to Account... |
| 9 | [Report #2736979](https://hackerone.com/reports/2736979) | U.S. Dept Of Defense | High | N/A | General | CSRF to XSS |
| 10 | [Report #2999394](https://hackerone.com/reports/2999394) | WordPress | High | N/A | Login CSRF | Pivilege escalation of any new... |

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
