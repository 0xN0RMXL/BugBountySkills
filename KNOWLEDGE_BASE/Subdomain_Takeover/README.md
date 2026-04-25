---
vuln_type: "Subdomain_Takeover"
file_type: "readme"
total_reports: "165"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:2% medium:2% low:96%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Subdomain_Takeover", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Subdomain Takeover — Complete Hunter's Reference

Subdomain Takeover represents a critical security oversight in implementing subdomain takeover paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 165
> **Average bounty:** $0
> **Highest bounty on record:** $0 — [Report #2542372](https://hackerone.com/reports/2542372) if 165 > 0 else 'N/A'
> **Dominant severity:** Low (96% of reports)
> **Most affected industry:** infra (26% of reports)
> **OWASP category:** A00:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 6 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 8 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 4 tools with exact commands |
| [[bypasses\|Bypasses]] | 1 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 165 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 165 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like Mozilla and others in the infra industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.

 This vulnerability class represents a critical breakdown in software architecture.

## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #2542372](https://hackerone.com/reports/2542372) | MTN Group | Critical | N/A | General | FULL ACCOUNT TAKEOVER |
| 2 | [Report #1851886](https://hackerone.com/reports/1851886) | Mars | High | N/A | General | Bug Report #23JAN135 (subdomain... |
| 3 | [Report #1851895](https://hackerone.com/reports/1851895) | Mars | High | N/A | General | Bug Report #23JAN136 (subdomain... |
| 4 | [Report #2523677](https://hackerone.com/reports/2523677) | RATELIMITED | High | N/A | General | Subdomain takeover in GitLab... |
| 5 | [Report #3324823](https://hackerone.com/reports/3324823) | U.S. Dept Of Defense | High | N/A | General | Account Takeover via... |
| 6 | [Report #1018790](https://hackerone.com/reports/1018790) | Acronis | Low | N/A | General | Subdomains takeover of ... |
| 7 | [Report #1094063](https://hackerone.com/reports/1094063) | Nextcloud | Low | N/A | General | Take over a mail account due... |
| 8 | [Report #1102537](https://hackerone.com/reports/1102537) | TikTok | Low | N/A | General | Subdomain Takeover via Unclaimed... |
| 9 | [Report #1179193](https://hackerone.com/reports/1179193) | Palo Alto Software | Low | N/A | General | Subdomain takeover of... |
| 10 | [Report #1180697](https://hackerone.com/reports/1180697) | Zego | Low | N/A | General | Subdomain takeover of v.zego.com |

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
