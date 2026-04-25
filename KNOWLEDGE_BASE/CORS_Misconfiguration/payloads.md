---
vuln_type: "CORS_Misconfiguration"
file_type: "payloads"
total_reports: "18"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["CORS_Misconfiguration", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# CORS Misconfiguration — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">
	<cross-domain-policy>    
	<site-control permitted-cross-domain-policies="all"/>    
	<allow-access-from domain="*"  secure="false" to-ports="*"/>
	<allow-http-request-headers-from domain="*"... This report describes a CORS_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "Insecure crossdomain.xml on..." and indicates exploitable input handling weaknesses. Observed report context: Hi, https://vdc.mtnonline.com/crossdomain.xml contains the following xml file:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1092125](https://hackerone.com/reports/1092125)

## Context-Specific Payloads

#### Payload 2

```javascript
GET /wp-json HTTP/1.1
Host: █████████
Connection: close
Origin: http://evil.com
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97... This report describes a CORS_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "(CORS) Cross-origin..." and indicates exploitable input handling weaknesses. Observed report context: **Description:** Affected website: **https://██████████/wp-json** ## Impact ## Step-by-step Reproduction : 1. **Send this request:**
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1183601](https://hackerone.com/reports/1183601)

## Advanced Payloads

#### Payload 3

```javascript
GET /██████████ HTTP/1.1
Host: █████
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
█████████
Origin: http://attacker.com
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1188471](https://hackerone.com/reports/1188471)

## WAF Bypass Payloads

#### Payload 1

```javascript
<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">
	<cross-domain-policy>    
	<site-control permitted-cross-domain-policies="all"/>    
	<allow-access-from domain="*"  secure="false" to-ports="*"/>
	<allow-http-request-headers-from domain="*"... This report describes a CORS_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "Insecure crossdomain.xml on..." and indicates exploitable input handling weaknesses. Observed report context: Hi, https://vdc.mtnonline.com/crossdomain.xml contains the following xml file:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1092125](https://hackerone.com/reports/1092125)

## Encoding & Obfuscation

#### Payload 4

```javascript
HTTP/1.1 200 OK
Cache-Control: max-age=0,must-revalidate
Expires: Wed, 31 Dec 1969 16:00:00 PST
Vary:... This report describes a CORS_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "(CORS) Cross-origin..." and indicates exploitable input handling weaknesses. Observed report context: Step-by-step Reproduction : Send this request:
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1189363](https://hackerone.com/reports/1189363)

## Polyglot Payloads

#### Payload 1

```javascript
<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">
	<cross-domain-policy>    
	<site-control permitted-cross-domain-policies="all"/>    
	<allow-access-from domain="*"  secure="false" to-ports="*"/>
	<allow-http-request-headers-from domain="*"... This report describes a CORS_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "Insecure crossdomain.xml on..." and indicates exploitable input handling weaknesses. Observed report context: Hi, https://vdc.mtnonline.com/crossdomain.xml contains the following xml file:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1092125](https://hackerone.com/reports/1092125)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM "http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">
	<cross-domain-policy>    
	<site-control permitted-cross-domain-policies="all"/>    
	<allow-access-from domain="*"  secure="false" to-ports="*"/>
	<allow-http-request-headers-from domain="*"... This report describes a CORS_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "Insecure crossdomain.xml on..." and indicates exploitable input handling weaknesses. Observed report context: Hi, https://vdc.mtnonline.com/crossdomain.xml contains the following xml file:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1092125](https://hackerone.com/reports/1092125)

## Chained Payloads

#### Payload 4

```javascript
HTTP/1.1 200 OK
Cache-Control: max-age=0,must-revalidate
Expires: Wed, 31 Dec 1969 16:00:00 PST
Vary:... This report describes a CORS_Misconfiguration issue affecting the target application surface. The disclosed finding is titled "(CORS) Cross-origin..." and indicates exploitable input handling weaknesses. Observed report context: Step-by-step Reproduction : Send this request:
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1189363](https://hackerone.com/reports/1189363)

