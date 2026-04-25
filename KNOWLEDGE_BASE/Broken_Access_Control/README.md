---
vuln_type: "Broken_Access_Control"
file_type: "readme"
total_reports: "470"
avg_bounty: "1128"
max_bounty: "10000"
severity_distribution: "critical:10% high:10% medium:10% low:70%"
owasp_categories: ["A01:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Broken_Access_Control", "web", "api", "A01", "hunter-kb"]
related_vulns: ["Information_Disclosure", "SSRF"]
---


# Broken Access Control — Complete Hunter's Reference

Broken Access Control represents a critical security oversight in implementing broken access control paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 470
> **Average bounty:** $1,128
> **Highest bounty on record:** $10,000 — [Report #3124517](https://hackerone.com/reports/3124517) if 470 > 0 else 'N/A'
> **Dominant severity:** Low (70% of reports)
> **Most affected industry:** saas (12% of reports)
> **OWASP category:** A01:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 10 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 9 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 3 tools with exact commands |
| [[bypasses\|Bypasses]] | 5 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 470 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 470 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like U.S. Dept Of Defense and others in the saas industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.
## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #3124517](https://hackerone.com/reports/3124517) | GitHub | High | $10,000 | Horizontal Privilege Escalation | Arbitrary Read of Another Users... |
| 2 | [Report #2967634](https://hackerone.com/reports/2967634) | Reddit | High | $7,500 | General | Exposed proxy allows to access... |
| 3 | [Report #2885269](https://hackerone.com/reports/2885269) | partners.shopify.com | Critical | $3,500 | Vertical Privilege Escalation | Shopify Partners Invitation Process... |
| 4 | [Report #2855610](https://hackerone.com/reports/2855610) | Unknown Program | High | $1,600 | Vertical Privilege Escalation | Staff with Restricted Permissions... |
| 5 | [Report #2891449](https://hackerone.com/reports/2891449) | proze.yelp.com | Critical | $1,250 | Vertical Privilege Escalation | Object Level access control leads to... |
| 6 | [Report #3027461](https://hackerone.com/reports/3027461) | Cloudflare Public Bug Bou | High | $1,250 | API Authorization Bypass | Bypass of... |
| 7 | [Report #2528293](https://hackerone.com/reports/2528293) | GitLab | High | $1,160 | General | IDOR Exposes All Machine Learning... |
| 8 | [Report #2293343](https://hackerone.com/reports/2293343) | GitLab | Critical | $1,000 | General | Account Takeover via Password Reset... |
| 9 | [Report #3360354](https://hackerone.com/reports/3360354) | Nextcloud | High | $750 | General | WebAuthn app was updated based on... |
| 10 | [Report #3178999](https://hackerone.com/reports/3178999) | HackerOne | Critical | $500 | General | Account takeover of existing... |

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
