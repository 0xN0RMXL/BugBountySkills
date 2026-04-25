---
vuln_type: "SSTI"
file_type: "payloads"
total_reports: "10"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["SSTI", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# SSTI — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
module UJS
  class Server < Rails::Application
    routes.append do
      get "/rails-ujs.js" => Blade::Assets.environment
      get "/" => "tests#index"
      match "/echo" =>... This report describes a SSTI issue affecting the target application surface. The disclosed finding is titled "Server-side template..." and indicates exploitable input handling weaknesses. Observed report context: I have found in the server code for testing ujs in Rails that template injection is possible and that leads to rce. ### code https://github.com/rails/rails/blob/v6.0.3.2/actionview/test/ujs/server.rb
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1104349](https://hackerone.com/reports/1104349)

## Context-Specific Payloads

#### Payload 1

```javascript
module UJS
  class Server < Rails::Application
    routes.append do
      get "/rails-ujs.js" => Blade::Assets.environment
      get "/" => "tests#index"
      match "/echo" =>... This report describes a SSTI issue affecting the target application surface. The disclosed finding is titled "Server-side template..." and indicates exploitable input handling weaknesses. Observed report context: I have found in the server code for testing ujs in Rails that template injection is possible and that leads to rce. ### code https://github.com/rails/rails/blob/v6.0.3.2/actionview/test/ujs/server.rb
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1104349](https://hackerone.com/reports/1104349)

## Advanced Payloads

#### Payload 1

```javascript
module UJS
  class Server < Rails::Application
    routes.append do
      get "/rails-ujs.js" => Blade::Assets.environment
      get "/" => "tests#index"
      match "/echo" =>... This report describes a SSTI issue affecting the target application surface. The disclosed finding is titled "Server-side template..." and indicates exploitable input handling weaknesses. Observed report context: I have found in the server code for testing ujs in Rails that template injection is possible and that leads to rce. ### code https://github.com/rails/rails/blob/v6.0.3.2/actionview/test/ujs/server.rb
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1104349](https://hackerone.com/reports/1104349)

## WAF Bypass Payloads

#### Payload 1

```javascript
module UJS
  class Server < Rails::Application
    routes.append do
      get "/rails-ujs.js" => Blade::Assets.environment
      get "/" => "tests#index"
      match "/echo" =>... This report describes a SSTI issue affecting the target application surface. The disclosed finding is titled "Server-side template..." and indicates exploitable input handling weaknesses. Observed report context: I have found in the server code for testing ujs in Rails that template injection is possible and that leads to rce. ### code https://github.com/rails/rails/blob/v6.0.3.2/actionview/test/ujs/server.rb
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1104349](https://hackerone.com/reports/1104349)

## Encoding & Obfuscation

#### Payload 1

```javascript
module UJS
  class Server < Rails::Application
    routes.append do
      get "/rails-ujs.js" => Blade::Assets.environment
      get "/" => "tests#index"
      match "/echo" =>... This report describes a SSTI issue affecting the target application surface. The disclosed finding is titled "Server-side template..." and indicates exploitable input handling weaknesses. Observed report context: I have found in the server code for testing ujs in Rails that template injection is possible and that leads to rce. ### code https://github.com/rails/rails/blob/v6.0.3.2/actionview/test/ujs/server.rb
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1104349](https://hackerone.com/reports/1104349)

## Polyglot Payloads

#### Payload 1

```javascript
module UJS
  class Server < Rails::Application
    routes.append do
      get "/rails-ujs.js" => Blade::Assets.environment
      get "/" => "tests#index"
      match "/echo" =>... This report describes a SSTI issue affecting the target application surface. The disclosed finding is titled "Server-side template..." and indicates exploitable input handling weaknesses. Observed report context: I have found in the server code for testing ujs in Rails that template injection is possible and that leads to rce. ### code https://github.com/rails/rails/blob/v6.0.3.2/actionview/test/ujs/server.rb
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1104349](https://hackerone.com/reports/1104349)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
module UJS
  class Server < Rails::Application
    routes.append do
      get "/rails-ujs.js" => Blade::Assets.environment
      get "/" => "tests#index"
      match "/echo" =>... This report describes a SSTI issue affecting the target application surface. The disclosed finding is titled "Server-side template..." and indicates exploitable input handling weaknesses. Observed report context: I have found in the server code for testing ujs in Rails that template injection is possible and that leads to rce. ### code https://github.com/rails/rails/blob/v6.0.3.2/actionview/test/ujs/server.rb
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1104349](https://hackerone.com/reports/1104349)

## Chained Payloads

#### Payload 1

```javascript
module UJS
  class Server < Rails::Application
    routes.append do
      get "/rails-ujs.js" => Blade::Assets.environment
      get "/" => "tests#index"
      match "/echo" =>... This report describes a SSTI issue affecting the target application surface. The disclosed finding is titled "Server-side template..." and indicates exploitable input handling weaknesses. Observed report context: I have found in the server code for testing ujs in Rails that template injection is possible and that leads to rce. ### code https://github.com/rails/rails/blob/v6.0.3.2/actionview/test/ujs/server.rb
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1104349](https://hackerone.com/reports/1104349)

