---
vuln_type: "Auth_Bypass"
file_type: "payloads"
total_reports: "153"
avg_bounty: "2510"
max_bounty: "3500"
severity_distribution: "critical:3% high:92% medium:5% low:0%"
owasp_categories: ["A07:2021"]
common_cwe: ["CWE-287", "CWE-288"]
last_updated: "2026-04-09"
tags: ["Auth_Bypass", "web", "api", "A07", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Auth Bypass — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components. 

> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
45.			$uname = $myts->stripSlashesGPC($autologinName);
46.			$pass = $myts->stripSlashesGPC($autologinPass);
47.			if (empty($uname) || is_numeric($pass)) {
48.				$user = false ;
49.			} else {
50.				// V3
51.				$uname4sql = addslashes($uname);
52.				$criteria = new icms_db_criteria_Compo(new... This report describes a Auth_Bypass issue affecting the target application surface. The disclosed finding is titled "Potential Authentication Bypass..." and indicates exploitable input handling weaknesses. Observed report context: ## Summary: The vulnerability is located in the `/plugins/preloads/autologin.php` script:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1040047](https://hackerone.com/reports/1040047)

## Context-Specific Payloads

#### Payload 1

```javascript
45.			$uname = $myts->stripSlashesGPC($autologinName);
46.			$pass = $myts->stripSlashesGPC($autologinPass);
47.			if (empty($uname) || is_numeric($pass)) {
48.				$user = false ;
49.			} else {
50.				// V3
51.				$uname4sql = addslashes($uname);
52.				$criteria = new icms_db_criteria_Compo(new... This report describes a Auth_Bypass issue affecting the target application surface. The disclosed finding is titled "Potential Authentication Bypass..." and indicates exploitable input handling weaknesses. Observed report context: ## Summary: The vulnerability is located in the `/plugins/preloads/autologin.php` script:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1040047](https://hackerone.com/reports/1040047)

## Advanced Payloads

#### Payload 2

```javascript
def authenticate_bot(bot_key)
  bot_id, bot_token = bot_key.split("-")
  active.find_by(id: bot_id, bot_token: bot_token)
end
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1043480](https://hackerone.com/reports/1043480)

## WAF Bypass Payloads

#### Payload 1

```javascript
45.			$uname = $myts->stripSlashesGPC($autologinName);
46.			$pass = $myts->stripSlashesGPC($autologinPass);
47.			if (empty($uname) || is_numeric($pass)) {
48.				$user = false ;
49.			} else {
50.				// V3
51.				$uname4sql = addslashes($uname);
52.				$criteria = new icms_db_criteria_Compo(new... This report describes a Auth_Bypass issue affecting the target application surface. The disclosed finding is titled "Potential Authentication Bypass..." and indicates exploitable input handling weaknesses. Observed report context: ## Summary: The vulnerability is located in the `/plugins/preloads/autologin.php` script:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1040047](https://hackerone.com/reports/1040047)

## Encoding & Obfuscation

#### Payload 1

```javascript
45.			$uname = $myts->stripSlashesGPC($autologinName);
46.			$pass = $myts->stripSlashesGPC($autologinPass);
47.			if (empty($uname) || is_numeric($pass)) {
48.				$user = false ;
49.			} else {
50.				// V3
51.				$uname4sql = addslashes($uname);
52.				$criteria = new icms_db_criteria_Compo(new... This report describes a Auth_Bypass issue affecting the target application surface. The disclosed finding is titled "Potential Authentication Bypass..." and indicates exploitable input handling weaknesses. Observed report context: ## Summary: The vulnerability is located in the `/plugins/preloads/autologin.php` script:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1040047](https://hackerone.com/reports/1040047)

## Polyglot Payloads

#### Payload 1

```javascript
45.			$uname = $myts->stripSlashesGPC($autologinName);
46.			$pass = $myts->stripSlashesGPC($autologinPass);
47.			if (empty($uname) || is_numeric($pass)) {
48.				$user = false ;
49.			} else {
50.				// V3
51.				$uname4sql = addslashes($uname);
52.				$criteria = new icms_db_criteria_Compo(new... This report describes a Auth_Bypass issue affecting the target application surface. The disclosed finding is titled "Potential Authentication Bypass..." and indicates exploitable input handling weaknesses. Observed report context: ## Summary: The vulnerability is located in the `/plugins/preloads/autologin.php` script:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1040047](https://hackerone.com/reports/1040047)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
45.			$uname = $myts->stripSlashesGPC($autologinName);
46.			$pass = $myts->stripSlashesGPC($autologinPass);
47.			if (empty($uname) || is_numeric($pass)) {
48.				$user = false ;
49.			} else {
50.				// V3
51.				$uname4sql = addslashes($uname);
52.				$criteria = new icms_db_criteria_Compo(new... This report describes a Auth_Bypass issue affecting the target application surface. The disclosed finding is titled "Potential Authentication Bypass..." and indicates exploitable input handling weaknesses. Observed report context: ## Summary: The vulnerability is located in the `/plugins/preloads/autologin.php` script:
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1040047](https://hackerone.com/reports/1040047)

## Chained Payloads

#### Payload 2

```javascript
def authenticate_bot(bot_key)
  bot_id, bot_token = bot_key.split("-")
  active.find_by(id: bot_id, bot_token: bot_token)
end
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1043480](https://hackerone.com/reports/1043480)

