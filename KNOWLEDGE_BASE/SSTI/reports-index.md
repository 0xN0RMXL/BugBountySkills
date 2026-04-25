---
vuln_type: "SSTI"
file_type: "index"
total_reports: "10"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["SSTI", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


## SSTI — Complete Reports Index

**Total reports:** 10
**Date range:** 2013-01-15 to 2026-04-09
**Total bounty value:** $0
**Average bounty:** $0
**Median bounty:** $0

## Hall of Fame — Top 10 by Bounty
### 1. [Report #1104349](https://hackerone.com/reports/1104349) — N/A — Glovo
**Program:** Glovo
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 2. [Report #1265344](https://hackerone.com/reports/1265344) — N/A — Acronis
**Program:** Acronis
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 3. [Report #1537543](https://hackerone.com/reports/1537543) — N/A — U.S. Dept Of Defense
**Program:** U.S. Dept Of Defense
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 4. [Report #1537694](https://hackerone.com/reports/1537694) — N/A — U.S. Dept Of Defense
**Program:** U.S. Dept Of Defense
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 5. [Report #2234564](https://hackerone.com/reports/2234564) — N/A — Mars
**Program:** Mars
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 6. [Report #271960](https://hackerone.com/reports/271960) — N/A — Rockstar Games
**Program:** Rockstar Games
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 7. [Report #299241](https://hackerone.com/reports/299241) — N/A — Informatica
**Program:** Informatica
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 8. [Report #423541](https://hackerone.com/reports/423541) — N/A — Shopify
**Program:** Shopify
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 9. [Report #904672](https://hackerone.com/reports/904672) — N/A — Node.js third-party modules
**Program:** Node.js third-party modules
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 10. [Report #942103](https://hackerone.com/reports/942103) — N/A — Ruby on Rails
**Program:** Ruby on Rails
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

## All Reports

| ID | Title | Program | Severity | Bounty | Sub-type | Quality | URL |
|----|-------|---------|----------|--------|----------|---------|-----|
| 1104349 | Server Side Template Injection on... | Glovo | low | N/A | General | 9 | [link](https://hackerone.com/reports/1104349) |
| 1265344 | Self-DoS due to template injection... | Acronis | low | N/A | General | 9 | [link](https://hackerone.com/reports/1265344) |
| 1537543 | ██████████ vulnerable... | U.S. Dept Of Defense | low | N/A | General | 9 | [link](https://hackerone.com/reports/1537543) |
| 1537694 | ███ vulnerable to... | U.S. Dept Of Defense | low | N/A | General | 9 | [link](https://hackerone.com/reports/1537694) |
| 2234564 | Client Side Template Injection to... | Mars | low | N/A | General | 9 | [link](https://hackerone.com/reports/2234564) |
| 271960 | Client-side Template... | Rockstar Games | low | N/A | General | 9 | [link](https://hackerone.com/reports/271960) |
| 299241 | [marketplace.informatica.com] -... | Informatica | low | N/A | General | 9 | [link](https://hackerone.com/reports/299241) |
| 423541 | H1514 Server Side Template... | Shopify | low | N/A | General | 9 | [link](https://hackerone.com/reports/423541) |
| 904672 | Server-side... | Node.js third-party modules | low | N/A | General | 9 | [link](https://hackerone.com/reports/904672) |
| 942103 | Server-side template... | Ruby on Rails | low | N/A | General | 9 | [link](https://hackerone.com/reports/942103) |

## Filter This Index with Dataview

```dataview
TABLE id, title, program_name, severity_label, bounty_usd, url
FROM "SSTI"
WHERE file_type = "index"
WHERE bounty_usd > 5000
SORT bounty_usd DESC
```
