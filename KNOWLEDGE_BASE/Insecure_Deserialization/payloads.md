---
vuln_type: "Insecure_Deserialization"
file_type: "payloads"
total_reports: "16"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:6% medium:94% low:0%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Insecure_Deserialization", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---

# Insecure Deserialization — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
https://github.com/php/php-src/blob/master/ext/wddx/wddx.c#L896

                if (!strcmp((char *)name, EL_BINARY)) {
                        zend_string *new_str =... This report describes a Insecure_Deserialization issue affecting the target application surface. The disclosed finding is titled "wddx_deserialize null..." and indicates exploitable input handling weaknesses. Observed report context: Upstream Bug --- https://bugs.php.net/bug.php?id=72750 Summary -- When wddx deserialize tries to parse an invalid base64 binary value, php_base64_decode return NULL. The return value is not checked and used.
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1167773](https://hackerone.com/reports/1167773)

## Context-Specific Payloads

#### Payload 1

```javascript
https://github.com/php/php-src/blob/master/ext/wddx/wddx.c#L896

                if (!strcmp((char *)name, EL_BINARY)) {
                        zend_string *new_str =... This report describes a Insecure_Deserialization issue affecting the target application surface. The disclosed finding is titled "wddx_deserialize null..." and indicates exploitable input handling weaknesses. Observed report context: Upstream Bug --- https://bugs.php.net/bug.php?id=72750 Summary -- When wddx deserialize tries to parse an invalid base64 binary value, php_base64_decode return NULL. The return value is not checked and used.
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1167773](https://hackerone.com/reports/1167773)

## Advanced Payloads

#### Payload 2

```javascript
http://git.php.net/?p=php-src.git;a=commit;h=780daee62b55995a10f8e849159eff0a25bacb9d
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1415436](https://hackerone.com/reports/1415436)

## WAF Bypass Payloads

#### Payload 1

```javascript
https://github.com/php/php-src/blob/master/ext/wddx/wddx.c#L896

                if (!strcmp((char *)name, EL_BINARY)) {
                        zend_string *new_str =... This report describes a Insecure_Deserialization issue affecting the target application surface. The disclosed finding is titled "wddx_deserialize null..." and indicates exploitable input handling weaknesses. Observed report context: Upstream Bug --- https://bugs.php.net/bug.php?id=72750 Summary -- When wddx deserialize tries to parse an invalid base64 binary value, php_base64_decode return NULL. The return value is not checked and used.
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1167773](https://hackerone.com/reports/1167773)

## Encoding & Obfuscation

#### Payload 1

```javascript
https://github.com/php/php-src/blob/master/ext/wddx/wddx.c#L896

                if (!strcmp((char *)name, EL_BINARY)) {
                        zend_string *new_str =... This report describes a Insecure_Deserialization issue affecting the target application surface. The disclosed finding is titled "wddx_deserialize null..." and indicates exploitable input handling weaknesses. Observed report context: Upstream Bug --- https://bugs.php.net/bug.php?id=72750 Summary -- When wddx deserialize tries to parse an invalid base64 binary value, php_base64_decode return NULL. The return value is not checked and used.
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1167773](https://hackerone.com/reports/1167773)

## Polyglot Payloads

#### Payload 1

```javascript
https://github.com/php/php-src/blob/master/ext/wddx/wddx.c#L896

                if (!strcmp((char *)name, EL_BINARY)) {
                        zend_string *new_str =... This report describes a Insecure_Deserialization issue affecting the target application surface. The disclosed finding is titled "wddx_deserialize null..." and indicates exploitable input handling weaknesses. Observed report context: Upstream Bug --- https://bugs.php.net/bug.php?id=72750 Summary -- When wddx deserialize tries to parse an invalid base64 binary value, php_base64_decode return NULL. The return value is not checked and used.
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1167773](https://hackerone.com/reports/1167773)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
https://github.com/php/php-src/blob/master/ext/wddx/wddx.c#L896

                if (!strcmp((char *)name, EL_BINARY)) {
                        zend_string *new_str =... This report describes a Insecure_Deserialization issue affecting the target application surface. The disclosed finding is titled "wddx_deserialize null..." and indicates exploitable input handling weaknesses. Observed report context: Upstream Bug --- https://bugs.php.net/bug.php?id=72750 Summary -- When wddx deserialize tries to parse an invalid base64 binary value, php_base64_decode return NULL. The return value is not checked and used.
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1167773](https://hackerone.com/reports/1167773)

## Chained Payloads

#### Payload 2

```javascript
http://git.php.net/?p=php-src.git;a=commit;h=780daee62b55995a10f8e849159eff0a25bacb9d
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1415436](https://hackerone.com/reports/1415436)


