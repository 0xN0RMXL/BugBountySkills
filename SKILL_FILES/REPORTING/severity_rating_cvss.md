# SKILL: Severity Rating with CVSS
## Version: 1.0 | Domain: reporting

---

## CVSS v3.1 BASE METRICS
- **Attack Vector (AV)** — Network / Adjacent / Local / Physical
- **Attack Complexity (AC)** — Low / High
- **Privileges Required (PR)** — None / Low / High
- **User Interaction (UI)** — None / Required
- **Scope (S)** — Unchanged / Changed
- **Confidentiality (C)** — None / Low / High
- **Integrity (I)** — None / Low / High
- **Availability (A)** — None / Low / High

## QUICK MAPPING

| Bug | Vector | Score |
|-----|--------|-------|
| Pre-auth RCE on public web | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 9.8 Critical |
| Auth RCE | AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H | 8.8 High |
| Stored XSS in admin panel | AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N | 9.0 Critical |
| Reflected XSS | AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N | 6.1 Medium |
| IDOR (full user read) | AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N | 6.5 Medium |
| Open redirect | AV:N/AC:L/PR:N/UI:R/S:C/C:N/I:L/A:N | 4.7 Medium |
| Subdomain takeover (cookie scope) | AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N | 9.6 Critical |
| SSRF → IMDS | AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H | 9.9 Critical |
| Self-XSS | AV:L/AC:H/PR:L/UI:R/S:U/C:L/I:L/A:N | 2.3 Low |

## CVSS v4.0 (Jan 2024+)
Newer scoring includes Threat (Exploit Maturity) and Environmental metrics. H1/Bugcrowd still default to v3.1.

## CALCULATORS
- https://www.first.org/cvss/calculator/3-1
- https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator

## TIPS
- Always show the vector string in the report.
- If your vector seems generous, add 1-2 sentences justifying.
- For BOLA on PII: C:H, not C:L.
- For ATO via auth bypass: usually C:H/I:H/A:N.

## REFERENCES
FIRST.org CVSS spec, OWASP Risk Rating Methodology
