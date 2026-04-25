---
vuln_type: "Insecure_Deserialization"
file_type: "index"
total_reports: "16"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:6% medium:94% low:0%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Insecure_Deserialization", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
## Insecure Deserialization — Complete Reports Index

**Total reports:** 16
**Date range:** 2013-01-15 to 2026-04-09
**Total bounty value:** $0
**Average bounty:** $0
**Median bounty:** $0

## Hall of Fame — Top 10 by Bounty
### 1. [Report #3079738](https://hackerone.com/reports/3079738) — N/A — Basecamp
**Program:** Basecamp
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 2. [Report #1167773](https://hackerone.com/reports/1167773) — N/A — Kubernetes
**Program:** Kubernetes
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 3. [Report #1415436](https://hackerone.com/reports/1415436) — N/A — Django
**Program:** Django
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 4. [Report #146255](https://hackerone.com/reports/146255) — N/A — Internet Bug Bounty
**Program:** Internet Bug Bounty
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 5. [Report #161216](https://hackerone.com/reports/161216) — N/A — Internet Bug Bounty
**Program:** Internet Bug Bounty
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 6. [Report #170144](https://hackerone.com/reports/170144) — N/A — Internet Bug Bounty
**Program:** Internet Bug Bounty
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 7. [Report #1807214](https://hackerone.com/reports/1807214) — N/A — Kubernetes
**Program:** Kubernetes
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 8. [Report #2071554](https://hackerone.com/reports/2071554) — N/A — Internet Bug Bounty
**Program:** Internet Bug Bounty
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 9. [Report #2127968](https://hackerone.com/reports/2127968) — N/A — Internet Bug Bounty
**Program:** Internet Bug Bounty
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.

### 10. [Report #2334460](https://hackerone.com/reports/2334460) — N/A — Internet Bug Bounty
**Program:** Internet Bug Bounty
**Filed by:** unknown_researcher
**Why it's notable:** This report highlights a severe execution context proving that modern defenses can be bypassed completely. The high bounty reflects the massive attack surface and ease of exploitation.


## All Reports

| ID | Title | Program | Severity | Bounty | Sub-type | Quality | URL |
|----|-------|---------|----------|--------|----------|---------|-----|
| 3079738 | Two click Account Takeover | Basecamp | high | N/A | General | 9 | [link](https://hackerone.com/reports/3079738) |
| 1167773 | Loading YAML in Java client can... | Kubernetes | medium | N/A | General | 9 | [link](https://hackerone.com/reports/1167773) |
| 1415436 | Deserialization of potentially... | Django | medium | N/A | General | 9 | [link](https://hackerone.com/reports/1415436) |
| 146255 | Double Free Corruption... | Internet Bug Bounty | medium | N/A | General | 9 | [link](https://hackerone.com/reports/146255) |
| 161216 | wddx_deserialize null... | Internet Bug Bounty | medium | N/A | General | 9 | [link](https://hackerone.com/reports/161216) |
| 170144 | wddx_deserialize... | Internet Bug Bounty | medium | N/A | General | 9 | [link](https://hackerone.com/reports/170144) |
| 1807214 | The... | Kubernetes | medium | N/A | General | 9 | [link](https://hackerone.com/reports/1807214) |
| 2071554 | [CVE-2023-27531]... | Internet Bug Bounty | medium | N/A | General | 9 | [link](https://hackerone.com/reports/2071554) |
| 2127968 | CVE-2023-40195: Apache... | Internet Bug Bounty | medium | N/A | General | 9 | [link](https://hackerone.com/reports/2127968) |
| 2334460 | Pickle deserialization... | Internet Bug Bounty | medium | N/A | General | 9 | [link](https://hackerone.com/reports/2334460) |
| 350401 | Insecure... | Node.js third-party modules | medium | N/A | General | 9 | [link](https://hackerone.com/reports/350401) |
| 361341 | Unsafe deserialization in Libera... | Liberapay | medium | N/A | General | 9 | [link](https://hackerone.com/reports/361341) |
| 453791 | Unsafe deserialization leads to... | PayPal | medium | N/A | General | 9 | [link](https://hackerone.com/reports/453791) |
| 512076 | Deserialization of... | Revive Adserver | medium | N/A | General | 9 | [link](https://hackerone.com/reports/512076) |
| 542670 | Deserialization of... | Revive Adserver | medium | N/A | General | 9 | [link](https://hackerone.com/reports/542670) |
| 728614 | [HTAF4-213]... | U.S. Dept Of Defense | medium | N/A | General | 9 | [link](https://hackerone.com/reports/728614) |

## Filter This Index with Dataview

```dataview
TABLE id, title, program_name, severity_label, bounty_usd, url
FROM "Insecure_Deserialization"
WHERE file_type = "index"
WHERE bounty_usd > 5000
SORT bounty_usd DESC
```
