---
vuln_type: "Information_Disclosure"
file_type: "payloads"
total_reports: "556"
avg_bounty: "2257"
max_bounty: "25000"
severity_distribution: "critical:7% high:6% medium:13% low:74%"
owasp_categories: ["A02:2021"]
common_cwe: ["CWE-200"]
last_updated: "2026-04-09"
tags: ["Information_Disclosure", "web", "api", "A02", "hunter-kb"]
related_vulns: ["Broken_Access_Control", "SSRF"]
---
# Information Disclosure — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
stack trace
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1007702](https://hackerone.com/reports/1007702)

#### Payload 2

```javascript
phpinfo()
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1008364](https://hackerone.com/reports/1008364)

#### Payload 3

```javascript
.htaccess
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1018608](https://hackerone.com/reports/1018608)

## Context-Specific Payloads

#### Payload 4

```javascript
debug mode
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1021906](https://hackerone.com/reports/1021906)

#### Payload 5

```javascript
secret =
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1026196](https://hackerone.com/reports/1026196)

## Advanced Payloads

#### Payload 6

```javascript
password     =
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1038129](https://hackerone.com/reports/1038129)

#### Payload 7

```javascript
Debug Mode
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1050196](https://hackerone.com/reports/1050196)

#### Payload 8

```javascript
PHPinfo
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1050454](https://hackerone.com/reports/1050454)

## WAF Bypass Payloads

#### Payload 9

```javascript
.config
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1057269](https://hackerone.com/reports/1057269)

## Encoding & Obfuscation

#### Payload 10

```javascript
Traceback
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1061204](https://hackerone.com/reports/1061204)

## Polyglot Payloads

#### Payload 11

```javascript
Stack trace
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1063114](https://hackerone.com/reports/1063114)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
stack trace
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1007702](https://hackerone.com/reports/1007702)

## Chained Payloads

#### Payload 12

```javascript
AKIAJRT6BUQHIPYENYWQ
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1063371](https://hackerone.com/reports/1063371)


