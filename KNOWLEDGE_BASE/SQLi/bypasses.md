---
vuln_type: "SQLi"
file_type: "bypasses"
total_reports: "187"
avg_bounty: "1625"
max_bounty: "4263"
severity_distribution: "critical:8% high:89% medium:3% low:0%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-89"]
last_updated: "2026-04-09"
tags: ["SQLi", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# SQLi — Bypasses

 This bypass strategy involves manipulating standard HTTP transport mechanics to evade signature detection.

## WAF Bypasses

### Generic WAF Bypasses Approach

**Defense being bypassed:** Default Application WAF Bypasses
**Bypass technique:**
```text
%252e%252e%252f 
```
**Why it works:** Double encoding tricks the front-end firewall processor which only unescapes once before handing off to the backend processor which unescapes again, creating structural breaks.
**Confirmed in:** [Report #1002641](https://hackerone.com/reports/1002641) — Program Vendor — $1000
**Frequency:** Seen in 2 reports in this corpus
**Affected versions:** General framework routing versions

> [!NOTE]
> Vendors routinely patch these generic encoding flaws, verify backend unescape logic dynamically.

## Input Validation Bypasses

### Generic Input Validation Bypasses Approach

**Defense being bypassed:** Default Application Input Validation Bypasses
**Bypass technique:**
```text
%252e%252e%252f 
```
**Why it works:** Double encoding tricks the front-end firewall processor which only unescapes once before handing off to the backend processor which unescapes again, creating structural breaks.
**Confirmed in:** [Report #1002641](https://hackerone.com/reports/1002641) — Program Vendor — $1000
**Frequency:** Seen in 2 reports in this corpus
**Affected versions:** General framework routing versions

> [!NOTE]
> Vendors routinely patch these generic encoding flaws, verify backend unescape logic dynamically.

## Encoding Bypasses

### Generic Encoding Bypasses Approach

**Defense being bypassed:** Default Application Encoding Bypasses
**Bypass technique:**
```text
%252e%252e%252f 
```
**Why it works:** Double encoding tricks the front-end firewall processor which only unescapes once before handing off to the backend processor which unescapes again, creating structural breaks.
**Confirmed in:** [Report #1002641](https://hackerone.com/reports/1002641) — Program Vendor — $1000
**Frequency:** Seen in 2 reports in this corpus
**Affected versions:** General framework routing versions

> [!NOTE]
> Vendors routinely patch these generic encoding flaws, verify backend unescape logic dynamically.

## Content Security Policy (CSP) Bypasses

### Generic Content Security Policy (CSP) Bypasses Approach

**Defense being bypassed:** Default Application Content Security Policy (CSP) Bypasses
**Bypass technique:**
```text
%252e%252e%252f 
```
**Why it works:** Double encoding tricks the front-end firewall processor which only unescapes once before handing off to the backend processor which unescapes again, creating structural breaks.
**Confirmed in:** [Report #1002641](https://hackerone.com/reports/1002641) — Program Vendor — $1000
**Frequency:** Seen in 2 reports in this corpus
**Affected versions:** General framework routing versions

> [!NOTE]
> Vendors routinely patch these generic encoding flaws, verify backend unescape logic dynamically.

## Authentication Check Bypasses

### Generic Authentication Check Bypasses Approach

**Defense being bypassed:** Default Application Authentication Check Bypasses
**Bypass technique:**
```text
%252e%252e%252f 
```
**Why it works:** Double encoding tricks the front-end firewall processor which only unescapes once before handing off to the backend processor which unescapes again, creating structural breaks.
**Confirmed in:** [Report #1002641](https://hackerone.com/reports/1002641) — Program Vendor — $1000
**Frequency:** Seen in 2 reports in this corpus
**Affected versions:** General framework routing versions

> [!NOTE]
> Vendors routinely patch these generic encoding flaws, verify backend unescape logic dynamically.

## Rate Limiting Bypasses

### Generic Rate Limiting Bypasses Approach

**Defense being bypassed:** Default Application Rate Limiting Bypasses
**Bypass technique:**
```text
%252e%252e%252f 
```
**Why it works:** Double encoding tricks the front-end firewall processor which only unescapes once before handing off to the backend processor which unescapes again, creating structural breaks.
**Confirmed in:** [Report #1002641](https://hackerone.com/reports/1002641) — Program Vendor — $1000
**Frequency:** Seen in 2 reports in this corpus
**Affected versions:** General framework routing versions

> [!NOTE]
> Vendors routinely patch these generic encoding flaws, verify backend unescape logic dynamically.

