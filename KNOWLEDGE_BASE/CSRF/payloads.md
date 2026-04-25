---
vuln_type: "CSRF"
file_type: "payloads"
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


# CSRF — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components. This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
token
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1003468](https://hackerone.com/reports/1003468)

#### Payload 2

```javascript
Token
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1006306](https://hackerone.com/reports/1006306)

## Context-Specific Payloads

#### Payload 3

```javascript
<form action=
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1010522](https://hackerone.com/reports/1010522)

## Advanced Payloads

#### Payload 4

```javascript
SameSite
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1010806](https://hackerone.com/reports/1010806)

## WAF Bypass Payloads

#### Payload 5

```javascript
<form  action=
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1014593](https://hackerone.com/reports/1014593)

## Encoding & Obfuscation

#### Payload 1

```javascript
token
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1003468](https://hackerone.com/reports/1003468)

## Polyglot Payloads

#### Payload 6

```javascript
TOKEN
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1018270](https://hackerone.com/reports/1018270)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
token
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1003468](https://hackerone.com/reports/1003468)

## Chained Payloads

#### Payload 6

```javascript
TOKEN
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1018270](https://hackerone.com/reports/1018270)


