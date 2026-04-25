---
vuln_type: "Account_Takeover"
file_type: "payloads"
total_reports: "90"
avg_bounty: "87"
max_bounty: "125"
severity_distribution: "critical:3% high:3% medium:92% low:2%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Account_Takeover", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Account Takeover — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
2020-03-20 08:12:15 - main - <br>Module: change password (4.1.2)<br>change_password=yes;/forum/forum_auth.php;login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1004536](https://hackerone.com/reports/1004536)

## Context-Specific Payloads

#### Payload 1

```javascript
2020-03-20 08:12:15 - main - <br>Module: change password (4.1.2)<br>change_password=yes;/forum/forum_auth.php;login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1004536](https://hackerone.com/reports/1004536)

## Advanced Payloads

#### Payload 2

```javascript
POST /__852585b6003eba25.nsf/forgotpassword.html?OpenForm&Seq=1 HTTP/1.1
Host: www.██████
Cookie: _ga=GA1.2.1700054986.1696324867; _ga_CSLL4ZEK4L=GS1.1.1696324866.1.1.1696324913.0.0.0;... This report describes a Account_Takeover issue affecting the target application surface. The disclosed finding is titled "Full account takeover..." and indicates exploitable input handling weaknesses. Observed report context: Hi Team I just checking this Url https://██████ and notice that when you request to forget password ,website send temp password in forget password request my password in request is: ███ Poc:
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1046630](https://hackerone.com/reports/1046630)

## WAF Bypass Payloads

#### Payload 1

```javascript
2020-03-20 08:12:15 - main - <br>Module: change password (4.1.2)<br>change_password=yes;/forum/forum_auth.php;login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1004536](https://hackerone.com/reports/1004536)

## Encoding & Obfuscation

#### Payload 1

```javascript
2020-03-20 08:12:15 - main - <br>Module: change password (4.1.2)<br>change_password=yes;/forum/forum_auth.php;login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1004536](https://hackerone.com/reports/1004536)

## Polyglot Payloads

#### Payload 1

```javascript
2020-03-20 08:12:15 - main - <br>Module: change password (4.1.2)<br>change_password=yes;/forum/forum_auth.php;login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1004536](https://hackerone.com/reports/1004536)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
2020-03-20 08:12:15 - main - <br>Module: change password (4.1.2)<br>change_password=yes;/forum/forum_auth.php;login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1004536](https://hackerone.com/reports/1004536)

## Chained Payloads

#### Payload 2

```javascript
POST /__852585b6003eba25.nsf/forgotpassword.html?OpenForm&Seq=1 HTTP/1.1
Host: www.██████
Cookie: _ga=GA1.2.1700054986.1696324867; _ga_CSLL4ZEK4L=GS1.1.1696324866.1.1.1696324913.0.0.0;... This report describes a Account_Takeover issue affecting the target application surface. The disclosed finding is titled "Full account takeover..." and indicates exploitable input handling weaknesses. Observed report context: Hi Team I just checking this Url https://██████ and notice that when you request to forget password ,website send temp password in forget password request my password in request is: ███ Poc:
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1046630](https://hackerone.com/reports/1046630)

