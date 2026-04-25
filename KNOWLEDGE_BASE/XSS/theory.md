---
vuln_type: "XSS"
file_type: "theory"
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


# XSS — Theory & Deep Technical Analysis

## All Variants and Sub-types
### Reflected XSS
Occurs within the context of reflected xss, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('Reflected XSS_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('Reflected XSS_context', escapeAndSanitize(user_input));
```

### Stored XSS
Occurs within the context of stored xss, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('Stored XSS_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('Stored XSS_context', escapeAndSanitize(user_input));
```

### XSS via File Upload
Occurs within the context of xss via file upload, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('XSS via File Upload_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('XSS via File Upload_context', escapeAndSanitize(user_input));
```

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

### DOM-based XSS
Occurs within the context of dom-based xss, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('DOM-based XSS_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('DOM-based XSS_context', escapeAndSanitize(user_input));
```

### XSS in Email
Occurs within the context of xss in email, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('XSS in Email_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('XSS in Email_context', escapeAndSanitize(user_input));
```

### XSS via Open Redirect
Occurs within the context of xss via open redirect, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('XSS via Open Redirect_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('XSS via Open Redirect_context', escapeAndSanitize(user_input));
```

### Blind XSS
Occurs within the context of blind xss, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('Blind XSS_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('Blind XSS_context', escapeAndSanitize(user_input));
```

### Self-XSS
Occurs within the context of self-xss, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('Self-XSS_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('Self-XSS_context', escapeAndSanitize(user_input));
```

### CSP Bypass XSS
Occurs within the context of csp bypass xss, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('CSP Bypass XSS_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('CSP Bypass XSS_context', escapeAndSanitize(user_input));
```

### XSS via Markdown
Occurs within the context of xss via markdown, historically bypassing generic validation defenses due to its unique rendering or execution environment.

**Vulnerable code:**
```javascript
// Input saved directly, rendered without encoding or parameterization
processInput('XSS via Markdown_context', user_input);
```

**Fixed code:**
```javascript
// Safely parameterized or sanitized using contextual filters
processInput('XSS via Markdown_context', escapeAndSanitize(user_input));
```

## Root Cause Analysis

### 1. Context Confusion
Developers often sanitize for one context (e.g., HTML text) but safely render in another (e.g., JavaScript attribute or DOM sink). This failure to understand context switching is the leading root cause. Over 1094 reports in this corpus involve some form of context confusion.

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
