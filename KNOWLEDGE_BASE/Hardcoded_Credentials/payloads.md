---
vuln_type: "Hardcoded_Credentials"
file_type: "payloads"
total_reports: "39"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Hardcoded_Credentials", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Hardcoded Credentials — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
password=admin
username=admin
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1083531](https://hackerone.com/reports/1083531)

## Context-Specific Payloads

#### Payload 1

```javascript
password=admin
username=admin
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1083531](https://hackerone.com/reports/1083531)

## Advanced Payloads

#### Payload 2

```javascript
password=admin username=admin
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1168104](https://hackerone.com/reports/1168104)

## WAF Bypass Payloads

#### Payload 1

```javascript
password=admin
username=admin
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1083531](https://hackerone.com/reports/1083531)

## Encoding & Obfuscation

#### Payload 1

```javascript
password=admin
username=admin
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1083531](https://hackerone.com/reports/1083531)

## Polyglot Payloads

#### Payload 1

```javascript
password=admin
username=admin
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1083531](https://hackerone.com/reports/1083531)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
password=admin
username=admin
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1083531](https://hackerone.com/reports/1083531)

## Chained Payloads

#### Payload 2

```javascript
password=admin username=admin
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1168104](https://hackerone.com/reports/1168104)

