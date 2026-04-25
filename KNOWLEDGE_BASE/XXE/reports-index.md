---
vuln_type: "XXE"
file_type: "index"
total_reports: "14"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A05:2021"]
common_cwe: ["CWE-611"]
last_updated: "2026-04-09"
tags: ["XXE", "web", "api", "A05", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


## XXE — Complete Reports Index

**Total reports:** 14
**Date range:** 2013-01-15 to 2026-04-09
**Total bounty value:** $0
**Average bounty:** $0
**Median bounty:** $0

## Hall of Fame — Top 10 by Bounty
### 1. [Report #105753](https://hackerone.com/reports/105753) — N/A — Informatica
**Program:** Informatica
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 2. [Report #1156748](https://hackerone.com/reports/1156748) — N/A — Elastic
**Program:** Elastic
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 3. [Report #130661](https://hackerone.com/reports/130661) — N/A — Moneybird
**Program:** Moneybird
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 4. [Report #150520](https://hackerone.com/reports/150520) — N/A — Informatica
**Program:** Informatica
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 5. [Report #188743](https://hackerone.com/reports/188743) — N/A — U.S. Dept Of Defense
**Program:** U.S. Dept Of Defense
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 6. [Report #227880](https://hackerone.com/reports/227880) — N/A — U.S. Dept Of Defense
**Program:** U.S. Dept Of Defense
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 7. [Report #248668](https://hackerone.com/reports/248668) — N/A — X / xAI
**Program:** X / xAI
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 8. [Report #25537](https://hackerone.com/reports/25537) — N/A — Internet Bug Bounty
**Program:** Internet Bug Bounty
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 9. [Report #296622](https://hackerone.com/reports/296622) — N/A — VK.com
**Program:** VK.com
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 10. [Report #312543](https://hackerone.com/reports/312543) — N/A — Semrush
**Program:** Semrush
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

## All Reports

| ID | Title | Program | Severity | Bounty | Sub-type | Quality | URL |
|----|-------|---------|----------|--------|----------|---------|-----|
| 105753 | [app.informaticaondemand.com] XXE | Informatica | low | N/A | General | 9 | [link](https://hackerone.com/reports/105753) |
| 1156748 | XXE in Enterprise Search's App... | Elastic | low | N/A | General | 9 | [link](https://hackerone.com/reports/1156748) |
| 130661 | XXE issue | Moneybird | low | N/A | General | 9 | [link](https://hackerone.com/reports/130661) |
| 150520 | XXE at Informatica sub-domain | Informatica | low | N/A | General | 9 | [link](https://hackerone.com/reports/150520) |
| 188743 | XXE on DoD web server | U.S. Dept Of Defense | low | N/A | General | 9 | [link](https://hackerone.com/reports/188743) |
| 227880 | XXE in DoD website... | U.S. Dept Of Defense | low | N/A | General | 9 | [link](https://hackerone.com/reports/227880) |
| 248668 | XXE on sms-be-vip.twitter.com in... | X / xAI | low | N/A | General | 9 | [link](https://hackerone.com/reports/248668) |
| 25537 | external entity... | Internet Bug Bounty | low | N/A | General | 9 | [link](https://hackerone.com/reports/25537) |
| 296622 | Blind XXE on pu.vk.com | VK.com | low | N/A | General | 9 | [link](https://hackerone.com/reports/296622) |
| 312543 | XXE in Site Audit function exposing... | Semrush | low | N/A | General | 9 | [link](https://hackerone.com/reports/312543) |
| 483774 | XXE on https://duckduckgo.com | DuckDuckGo | low | N/A | General | 9 | [link](https://hackerone.com/reports/483774) |
| 500515 | XXE at... | Starbucks | low | N/A | General | 9 | [link](https://hackerone.com/reports/500515) |
| 715949 | [HTA2] XXE on... | U.S. Dept Of Defense | low | N/A | General | 9 | [link](https://hackerone.com/reports/715949) |
| 762251 | Singapore - XXE at... | Starbucks | low | N/A | General | 9 | [link](https://hackerone.com/reports/762251) |

## Filter This Index with Dataview

```dataview
TABLE id, title, program_name, severity_label, bounty_usd, url
FROM "XXE"
WHERE file_type = "index"
WHERE bounty_usd > 5000
SORT bounty_usd DESC
```
