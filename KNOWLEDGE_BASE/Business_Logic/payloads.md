---
vuln_type: "Business_Logic"
file_type: "payloads"
total_reports: "65"
avg_bounty: "932"
max_bounty: "2000"
severity_distribution: "critical:13% high:23% medium:20% low:44%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Business_Logic", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Business Logic — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.
> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
.domain.com "20241107 01:02:03"
.sub.domain.com "unlimited"
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1085079](https://hackerone.com/reports/1085079)

## Context-Specific Payloads

#### Payload 2

```javascript
curl ldap://localhost:1388
curl: result.c:930: try_read1msg: Assertion `!BER_BVISEMPTY( &resoid )' failed.
Aborted (core dumped)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1166993](https://hackerone.com/reports/1166993)

## Advanced Payloads

#### Payload 1

```javascript
.domain.com "20241107 01:02:03"
.sub.domain.com "unlimited"
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1085079](https://hackerone.com/reports/1085079)

## WAF Bypass Payloads

#### Payload 3

```javascript
Free Shipping Promo Code (pick one):
United ████: ████████
International: ███
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1189282](https://hackerone.com/reports/1189282)

## Encoding & Obfuscation

#### Payload 1

```javascript
.domain.com "20241107 01:02:03"
.sub.domain.com "unlimited"
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1085079](https://hackerone.com/reports/1085079)

## Polyglot Payloads

#### Payload 1

```javascript
.domain.com "20241107 01:02:03"
.sub.domain.com "unlimited"
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1085079](https://hackerone.com/reports/1085079)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
.domain.com "20241107 01:02:03"
.sub.domain.com "unlimited"
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1085079](https://hackerone.com/reports/1085079)

## Chained Payloads

#### Payload 3

```javascript
Free Shipping Promo Code (pick one):
United ████: ████████
International: ███
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1189282](https://hackerone.com/reports/1189282)

