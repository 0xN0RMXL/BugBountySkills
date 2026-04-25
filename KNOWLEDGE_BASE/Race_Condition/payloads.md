---
vuln_type: "Race_Condition"
file_type: "payloads"
total_reports: "66"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:4% high:6% medium:6% low:84%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Race_Condition", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Race Condition — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
if(stat(filename, &sb) == -1 || !S_ISREG(sb.st_mode)) {
    /* a non-regular file, fallback to direct fopen() */
    *fh = fopen(filename, FOPEN_WRITETEXT);
...
}
...
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1019457](https://hackerone.com/reports/1019457)

## Context-Specific Payloads

#### Payload 2

```javascript
:54:curl/lib/socks_gssapi.c
static gss_ctx_id_t gss_context = GSS_C_NO_CONTEXT;
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1035320](https://hackerone.com/reports/1035320)

## Advanced Payloads

#### Payload 3

```javascript
POST /graphql HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 778
Accept: */*
X-Auth-Token: ████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Origin:... This report describes a Race_Condition issue affecting the target application surface. The disclosed finding is titled "Race condition in claiming..." and indicates exploitable input handling weaknesses. Observed report context: Hi, **Summary:** I was invited to a private program and I tried to get test credentials so a request as follows was sent to your server:
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1037430](https://hackerone.com/reports/1037430)

## WAF Bypass Payloads

#### Payload 1

```javascript
if(stat(filename, &sb) == -1 || !S_ISREG(sb.st_mode)) {
    /* a non-regular file, fallback to direct fopen() */
    *fh = fopen(filename, FOPEN_WRITETEXT);
...
}
...
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1019457](https://hackerone.com/reports/1019457)

## Encoding & Obfuscation

#### Payload 4

```javascript
POST /cabinet/stripeapi/v1/projects/298427/emails/folders HTTP/1.1
Host: my.stripo.email
Connection: close
Content-Length: 23
Accept: application/json, text/plain, */*
Pragma: no-cache
Expires: Sat, 01 Jan 2000 00:00:00 GMT
Cache-Control: no-cache
X-XSRF-TOKEN:... This report describes a Race_Condition issue affecting the target application surface. The disclosed finding is titled "Race condition on..." and indicates exploitable input handling weaknesses. Observed report context: ## Summary: Hi! I hope you all are pretty good =) We have discovered a race condition endpoint ## Steps To Reproduce:
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1087188](https://hackerone.com/reports/1087188)

## Polyglot Payloads

#### Payload 1

```javascript
if(stat(filename, &sb) == -1 || !S_ISREG(sb.st_mode)) {
    /* a non-regular file, fallback to direct fopen() */
    *fh = fopen(filename, FOPEN_WRITETEXT);
...
}
...
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1019457](https://hackerone.com/reports/1019457)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
if(stat(filename, &sb) == -1 || !S_ISREG(sb.st_mode)) {
    /* a non-regular file, fallback to direct fopen() */
    *fh = fopen(filename, FOPEN_WRITETEXT);
...
}
...
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1019457](https://hackerone.com/reports/1019457)

## Chained Payloads

#### Payload 4

```javascript
POST /cabinet/stripeapi/v1/projects/298427/emails/folders HTTP/1.1
Host: my.stripo.email
Connection: close
Content-Length: 23
Accept: application/json, text/plain, */*
Pragma: no-cache
Expires: Sat, 01 Jan 2000 00:00:00 GMT
Cache-Control: no-cache
X-XSRF-TOKEN:... This report describes a Race_Condition issue affecting the target application surface. The disclosed finding is titled "Race condition on..." and indicates exploitable input handling weaknesses. Observed report context: ## Summary: Hi! I hope you all are pretty good =) We have discovered a race condition endpoint ## Steps To Reproduce:
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1087188](https://hackerone.com/reports/1087188)

