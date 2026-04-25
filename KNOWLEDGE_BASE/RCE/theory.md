---
vuln_type: "RCE"
file_type: "theory"
total_reports: "495"
avg_bounty: "411"
max_bounty: "4323"
severity_distribution: "critical:9% high:85% medium:5% low:1%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-78", "CWE-94", "CWE-502"]
last_updated: "2026-04-09"
tags: ["RCE", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# RCE — Theory & Deep Technical Analysis

## All Variants and Sub-types
### General
Occurs within the context of general, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('General_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('General_context', escapeAndSanitize(user_input));
```

### File Upload RCE
Occurs within the context of file upload rce, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('File Upload RCE_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('File Upload RCE_context', escapeAndSanitize(user_input));
```

### Command Injection
Occurs within the context of command injection, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('Command Injection_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('Command Injection_context', escapeAndSanitize(user_input));
```

### Deserialization RCE
Occurs within the context of deserialization rce, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('Deserialization RCE_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('Deserialization RCE_context', escapeAndSanitize(user_input));
```

### Code Injection
Occurs within the context of code injection, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('Code Injection_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('Code Injection_context', escapeAndSanitize(user_input));
```

### SSTI/Template Injection
Occurs within the context of ssti/template injection, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('SSTI/Template Injection_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('SSTI/Template Injection_context', escapeAndSanitize(user_input));
```

### Server-Side Prototype Pollution
Occurs within the context of server-side prototype pollution, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('Server-Side Prototype Pollution_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('Server-Side Prototype Pollution_context', escapeAndSanitize(user_input));
```

### Dependency Confusion
Occurs within the context of dependency confusion, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('Dependency Confusion_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('Dependency Confusion_context', escapeAndSanitize(user_input));
```

## Root Cause Analysis

### 1. Context Confusion
Developers often sanitize for one context (e.g., HTML text) but safely render in another (e.g., JavaScript attribute or DOM sink). This failure to understand context switching is the leading root cause. Over 346 reports in this corpus involve some form of context confusion.

### 2. Trusting Client-Side Validations
Applications enforce restrictions in the frontend UI but fail to replicate them server-side. Attackers bypass the UI directly via interception proxies like Burp Suite.

### 3. Vulnerable Third-Party Dependencies
Integrating legacy libraries or unpatched external packages introduces known vulnerable sinks into an otherwise secure application.

## The Attacker Mental Model

When you're hunting for this vulnerability, you must think like an adversary parsing state transitions. Do not blindly throw payloads. First, map the entire surface area. Observe the application's natural behavior. 
1. Where does your input go? 
2. Does it bounce back immediately? 
3. Does it settle into a database and surface in a secondary administrator portal?
4. Are you hitting a Web Application Firewall (WAF)?

Identify the actual parsing technology used in the backend. If you know the backend runs Node.js vs PHP, your payload structure changes dramatically. Common false positives happen when the input is reflected safely as a string — a successful hunt confirms that the string is actually interpreted as code or structural metadata by the underlying environment.

 The theoretical underpinnings of this vulnerability stem from the fundamental concept of context switching in modern web application design. When untrusted user data crosses a trust boundary, the receiving context must understand how to safely interpret that data.

## Common Misconceptions

> [!WARNING]
> These misconceptions regularly invalidate bug reports.

**Misconception:** "Any reflection implies vulnerability."
**Reality:** Reflection must escape its current data context. If the input is safely cast or contextually encoded, there is no vulnerability. Many beginners submit invalid reports based on raw reflections.

**Misconception:** "WAF blocks mean the target is secure."
**Reality:** WAFs are easily bypassed with specific canonicalization tricks or logic parsing errors. A WAF block simply means you're using a public payload. 

**Misconception:** "It only affects public pages."
**Reality:** Blind vulnerabilities execute in administrative backends or logging systems. Some of the highest value reports ($10,000+) are triggered blindly by administrators reviewing logs.

**Misconception:** "It requires user interaction."
**Reality:** Depending on the variant, payloads execute zero-click during default application state changes or image loading.

**Misconception:** "Modern frameworks eliminate this vulnerability."
**Reality:** React, Angular, and Vue have "dangerouslySet" equivalents, and server-side rendering introduces completely new vector classes.
