---
vuln_type: "Cryptographic_Weakness"
file_type: "payloads"
total_reports: "172"
avg_bounty: "573"
max_bounty: "2162"
severity_distribution: "critical:7% high:10% medium:20% low:63%"
owasp_categories: ["A02:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Cryptographic_Weakness", "web", "api", "A02", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Cryptographic Weakness — Payloads

 This payload structure operates reliably against standard implementations lacking modern security boundaries or active request filtering components.
 
> [!TIP]
> Always iterate. Test a canary token to figure out parsing logic, then increment to full payload structures.

> [!WARNING]
> Execute payloads explicitly only against authorized systems in accordance with program SLA scopes.

## Basic Payloads

#### Payload 1

```javascript
//set private key to 2
dh.setPrivateKey(Buffer.from("02", 'hex'));        
//outputs 02 (as expected)
console.log(dh.getPrivateKey().toString('hex'));
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1048457](https://hackerone.com/reports/1048457)

#### Payload 2

```javascript
public function return_handler() {
		@ob_clean();
		header( 'HTTP/1.1 200 OK' );

		if ( isset( $_REQUEST['reference'] ) && isset( $_REQUEST['paymentId'] ) && isset( $_REQUEST['signature'] ) ) {
			$signature = strtoupper( md5(... This report describes a Cryptographic_Weakness issue affecting the target application surface. The disclosed finding is titled "Timing attack woocommerce,..." and indicates exploitable input handling weaknesses. Observed report context: file `class-wc-gateway-simplify-commerce.php` method `return_handler` e.g. where woocommerce marks the order regarding its payment / transaction.
```

**Context:** JSON body
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1056144](https://hackerone.com/reports/1056144)

## Context-Specific Payloads

#### Payload 3

```javascript
<?php
$to = "VICTIM@example.com";
$subject = "Password Change";
$txt = "Change your password by visiting here - [VIRUS LINK HERE]l";
$headers = "From: support@wakatime.com";
mail($to,$subject,$txt,$headers);
?>
```

**Context:** HTTP header
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1064087](https://hackerone.com/reports/1064087)

## Advanced Payloads

#### Payload 4

```javascript
if ( sha1( $attempted_password_plaintext ) === $valid_password_hash || wp_check_password( $attempted_password_plaintext, $valid_password_hash ) ) {
	$this->is_using_application_password = true;
	return... This report describes a Cryptographic_Weakness issue affecting the target application surface. The disclosed finding is titled "Timing Attack in Google..." and indicates exploitable input handling weaknesses. Observed report context: *Google Authenticator - Per User Prompt* contains a timing attack vulnerability in how it validates the application password for a user account.
```

**Context:** URL parameter
**Bypasses:** WAF / Input Validation Filter
**Framework:** Framework-agnostic
**Source:** [Report #1070533](https://hackerone.com/reports/1070533)

## WAF Bypass Payloads

#### Payload 1

```javascript
//set private key to 2
dh.setPrivateKey(Buffer.from("02", 'hex'));        
//outputs 02 (as expected)
console.log(dh.getPrivateKey().toString('hex'));
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1048457](https://hackerone.com/reports/1048457)

## Encoding & Obfuscation

#### Payload 5

```javascript
nli@nlistation:~$ dig mycrypto.com txt

; <<>> DiG 9.10.3-P4-Ubuntu <<>> mycrypto.com txt
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 43571
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;mycrypto.com.			IN	TXT

;; AUTHORITY... This report describes a Cryptographic_Weakness issue affecting the target application surface. The disclosed finding is titled "Missing SPF record for the in..." and indicates exploitable input handling weaknesses. Observed report context:
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1125143](https://hackerone.com/reports/1125143)

## Polyglot Payloads

#### Payload 1

```javascript
//set private key to 2
dh.setPrivateKey(Buffer.from("02", 'hex'));        
//outputs 02 (as expected)
console.log(dh.getPrivateKey().toString('hex'));
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1048457](https://hackerone.com/reports/1048457)

## Blind / Out-of-Band Payloads

#### Payload 1

```javascript
//set private key to 2
dh.setPrivateKey(Buffer.from("02", 'hex'));        
//outputs 02 (as expected)
console.log(dh.getPrivateKey().toString('hex'));
```

**Context:** URL parameter
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1048457](https://hackerone.com/reports/1048457)

## Chained Payloads

#### Payload 5

```javascript
nli@nlistation:~$ dig mycrypto.com txt

; <<>> DiG 9.10.3-P4-Ubuntu <<>> mycrypto.com txt
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 43571
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;mycrypto.com.			IN	TXT

;; AUTHORITY... This report describes a Cryptographic_Weakness issue affecting the target application surface. The disclosed finding is titled "Missing SPF record for the in..." and indicates exploitable input handling weaknesses. Observed report context:
```

**Context:** JSON body
**Bypasses:** No special bypass needed
**Framework:** Framework-agnostic
**Source:** [Report #1125143](https://hackerone.com/reports/1125143)


