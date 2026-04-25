---
vuln_type: "OAuth_Misconfiguration"
file_type: "payloads"
total_reports: "35"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["OAuth_Misconfiguration", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# OAuth Misconfiguration — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
#include <curl/curl.h>

int main(void) {
  curl_global_init(CURL_GLOBAL_ALL);

  CURL* curl = curl_easy_init();

  curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_BEARER);
  curl_easy_setopt(curl,... This report describes a OAuth_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "Memory leak in CURLOPT_XOAUTH2_BEARER" and indicates exploitable input handling weaknesses. Observed report context: ## Summary: Once a bearer token is set with `CURLOPT_XOAUTH2_BEARER`, each HTTP request done with the same handler leaks the token itself. ## Steps To Reproduce: Given the following code:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1074047](https://hackerone.com/reports/1074047)

## Context-Specific Payloads

#### Payload 2

```javascript
<script>
  function listener(event) {
    alert(JSON.stringify(event.data));
  }

  var dest =... This report describes a OAuth_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "[oauth token leak] at..." and indicates exploitable input handling weaknesses. Observed report context: Domain, site, application --- oauth.semrush.com Steps to reproduce --- 1) Create following html at attacker.com/postmessage.html
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #110293](https://hackerone.com/reports/110293)

## Advanced Payloads

#### Payload 1

```javascript
#include <curl/curl.h>

int main(void) {
  curl_global_init(CURL_GLOBAL_ALL);

  CURL* curl = curl_easy_init();

  curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_BEARER);
  curl_easy_setopt(curl,... This report describes a OAuth_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "Memory leak in CURLOPT_XOAUTH2_BEARER" and indicates exploitable input handling weaknesses. Observed report context: ## Summary: Once a bearer token is set with `CURLOPT_XOAUTH2_BEARER`, each HTTP request done with the same handler leaks the token itself. ## Steps To Reproduce: Given the following code:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1074047](https://hackerone.com/reports/1074047)

## WAF Bypass Payloads

#### Payload 3

```javascript
/login/oauth/authorize?response_type=code&client_id=web-internal&redirect_uri=http://whatever
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #110467](https://hackerone.com/reports/110467)

## Encoding & Obfuscation

#### Payload 1

```javascript
#include <curl/curl.h>

int main(void) {
  curl_global_init(CURL_GLOBAL_ALL);

  CURL* curl = curl_easy_init();

  curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_BEARER);
  curl_easy_setopt(curl,... This report describes a OAuth_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "Memory leak in CURLOPT_XOAUTH2_BEARER" and indicates exploitable input handling weaknesses. Observed report context: ## Summary: Once a bearer token is set with `CURLOPT_XOAUTH2_BEARER`, each HTTP request done with the same handler leaks the token itself. ## Steps To Reproduce: Given the following code:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1074047](https://hackerone.com/reports/1074047)

## Polyglot Payloads

#### Payload 1

```javascript
#include <curl/curl.h>

int main(void) {
  curl_global_init(CURL_GLOBAL_ALL);

  CURL* curl = curl_easy_init();

  curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_BEARER);
  curl_easy_setopt(curl,... This report describes a OAuth_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "Memory leak in CURLOPT_XOAUTH2_BEARER" and indicates exploitable input handling weaknesses. Observed report context: ## Summary: Once a bearer token is set with `CURLOPT_XOAUTH2_BEARER`, each HTTP request done with the same handler leaks the token itself. ## Steps To Reproduce: Given the following code:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1074047](https://hackerone.com/reports/1074047)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
#include <curl/curl.h>

int main(void) {
  curl_global_init(CURL_GLOBAL_ALL);

  CURL* curl = curl_easy_init();

  curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_BEARER);
  curl_easy_setopt(curl,... This report describes a OAuth_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "Memory leak in CURLOPT_XOAUTH2_BEARER" and indicates exploitable input handling weaknesses. Observed report context: ## Summary: Once a bearer token is set with `CURLOPT_XOAUTH2_BEARER`, each HTTP request done with the same handler leaks the token itself. ## Steps To Reproduce: Given the following code:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1074047](https://hackerone.com/reports/1074047)

## Chained Payloads

#### Payload 3

```javascript
/login/oauth/authorize?response_type=code&client_id=web-internal&redirect_uri=http://whatever
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #110467](https://hackerone.com/reports/110467)

