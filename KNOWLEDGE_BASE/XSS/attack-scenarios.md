---
vuln_type: "XSS"
file_type: "scenarios"
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


# XSS — Attack Scenarios

### Scenario 1: Reflected XSS Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 477 reports used this pattern
**Average bounty for this scenario:** $66

#### Prerequisites
- The application processes untrusted input in the Reflected XSS context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to XSS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

#### Step-by-Step Attack

1. Identify the input vector within the application that maps to the vulnerable context.
2. Inject a benign canary value (e.g. `xyzztest`) to verify reflection or processing.
3. Observe how the context translates the canary value. Identify forbidden characters.
4. Craft an execution sequence escaping the context boundaries. Use variations if WAF intervenes.
5. Observe: The application structurally parses the execution sequence as active code/metadata rather than raw text.
6. Contrast: A patched response safely literalizes the input, rendering it completely inert.

> [!EXAMPLE]
> A classic example of this involves bypassing frontend sanitization to trigger backend processing.

#### Proof of Concept

```http
POST /api/v1/trigger/reflected_xss HTTP/1.1
Host: target.com
Content-Type: application/json

{"payload": "injection_sequence_here"}
```

Expected response contains:
```http
HTTP/1.1 200 OK

{"result": "execution_successful"}
```

#### Impact
This execution pattern critically undermines the integrity of the application, empowering the attacker to commandeer session identity, access underlying operating systems, or exfiltrate massive amounts of sensitive internal data depending on the deployment role.

#### Report Evidence
- [Report #2038943](https://hackerone.com/reports/2038943) — "[oem.acronis.com] Reflected Cross..." — $100 — Acronis
- [Report #1891926](https://hackerone.com/reports/1891926) — "Reflected XSS in..." — $100 — acronis.com

---

### Scenario 2: Stored XSS Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 442 reports used this pattern
**Average bounty for this scenario:** $280

#### Prerequisites
- The application processes untrusted input in the Stored XSS context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to XSS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

#### Step-by-Step Attack

1. Identify the input vector within the application that maps to the vulnerable context.
2. Inject a benign canary value (e.g. `xyzztest`) to verify reflection or processing.
3. Observe how the context translates the canary value. Identify forbidden characters.
4. Craft an execution sequence escaping the context boundaries. Use variations if WAF intervenes.
5. Observe: The application structurally parses the execution sequence as active code/metadata rather than raw text.
6. Contrast: A patched response safely literalizes the input, rendering it completely inert.

> [!EXAMPLE]
> A classic example of this involves bypassing frontend sanitization to trigger backend processing.

#### Proof of Concept

```http
POST /api/v1/trigger/stored_xss HTTP/1.1
Host: target.com
Content-Type: application/json

{"payload": "injection_sequence_here"}
```

Expected response contains:
```http
HTTP/1.1 200 OK

{"result": "execution_successful"}
```

#### Impact
This execution pattern critically undermines the integrity of the application, empowering the attacker to commandeer session identity, access underlying operating systems, or exfiltrate massive amounts of sensitive internal data depending on the deployment role.

#### Report Evidence
- [Report #2521419](https://hackerone.com/reports/2521419) — "Stored XSS on trix editor version..." — $1000 — Basecamp
- [Report #2677187](https://hackerone.com/reports/2677187) — "CVE-2024-41937: Apache..." — $497 — Internet Bug Bounty

---

### Scenario 3: XSS via File Upload Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 364 reports used this pattern
**Average bounty for this scenario:** $400

#### Prerequisites
- The application processes untrusted input in the XSS via File Upload context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to XSS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

#### Step-by-Step Attack

1. Identify the input vector within the application that maps to the vulnerable context.
2. Inject a benign canary value (e.g. `xyzztest`) to verify reflection or processing.
3. Observe how the context translates the canary value. Identify forbidden characters.
4. Craft an execution sequence escaping the context boundaries. Use variations if WAF intervenes.
5. Observe: The application structurally parses the execution sequence as active code/metadata rather than raw text.
6. Contrast: A patched response safely literalizes the input, rendering it completely inert.

> [!EXAMPLE]
> A classic example of this involves bypassing frontend sanitization to trigger backend processing.

#### Proof of Concept

```http
POST /api/v1/trigger/xss_via_file_upload HTTP/1.1
Host: target.com
Content-Type: application/json

{"payload": "injection_sequence_here"}
```

Expected response contains:
```http
HTTP/1.1 200 OK

{"result": "execution_successful"}
```

#### Impact
This execution pattern critically undermines the integrity of the application, empowering the attacker to commandeer session identity, access underlying operating systems, or exfiltrate massive amounts of sensitive internal data depending on the deployment role.

#### Report Evidence
- [Report #1935628](https://hackerone.com/reports/1935628) — "HTML injection possible with soft..." — $1060 — GitLab
- [Report #2931688](https://hackerone.com/reports/2931688) — "ActionView sanitize..." — $541 — Internet Bug Bounty

---

### Scenario 4: General Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 331 reports used this pattern
**Average bounty for this scenario:** $818

#### Prerequisites
- The application processes untrusted input in the General context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to XSS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

#### Step-by-Step Attack

1. Identify the input vector within the application that maps to the vulnerable context.
2. Inject a benign canary value (e.g. `xyzztest`) to verify reflection or processing.
3. Observe how the context translates the canary value. Identify forbidden characters.
4. Craft an execution sequence escaping the context boundaries. Use variations if WAF intervenes.
5. Observe: The application structurally parses the execution sequence as active code/metadata rather than raw text.
6. Contrast: A patched response safely literalizes the input, rendering it completely inert.

> [!EXAMPLE]
> A classic example of this involves bypassing frontend sanitization to trigger backend processing.

#### Proof of Concept

```http
POST /api/v1/trigger/general HTTP/1.1
Host: target.com
Content-Type: application/json

{"payload": "injection_sequence_here"}
```

Expected response contains:
```http
HTTP/1.1 200 OK

{"result": "execution_successful"}
```

#### Impact
This execution pattern critically undermines the integrity of the application, empowering the attacker to commandeer session identity, access underlying operating systems, or exfiltrate massive amounts of sensitive internal data depending on the deployment role.

#### Report Evidence
- [Report #1695604](https://hackerone.com/reports/1695604) — "DoS Vulnerability via Cache..." — $3800 — cdn.shopify.com
- [Report #2520694](https://hackerone.com/reports/2520694) — "Possible XSS..." — $568 — Internet Bug Bounty

---

### Scenario 5: DOM-based XSS Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 212 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the DOM-based XSS context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to XSS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

#### Step-by-Step Attack

1. Identify the input vector within the application that maps to the vulnerable context.
2. Inject a benign canary value (e.g. `xyzztest`) to verify reflection or processing.
3. Observe how the context translates the canary value. Identify forbidden characters.
4. Craft an execution sequence escaping the context boundaries. Use variations if WAF intervenes.
5. Observe: The application structurally parses the execution sequence as active code/metadata rather than raw text.
6. Contrast: A patched response safely literalizes the input, rendering it completely inert.

> [!EXAMPLE]
> A classic example of this involves bypassing frontend sanitization to trigger backend processing.

#### Proof of Concept

```http
POST /api/v1/trigger/dom-based_xss HTTP/1.1
Host: target.com
Content-Type: application/json

{"payload": "injection_sequence_here"}
```

Expected response contains:
```http
HTTP/1.1 200 OK

{"result": "execution_successful"}
```

#### Impact
This execution pattern critically undermines the integrity of the application, empowering the attacker to commandeer session identity, access underlying operating systems, or exfiltrate massive amounts of sensitive internal data depending on the deployment role.

#### Report Evidence
- [Report #2778412](https://hackerone.com/reports/2778412) — "[ CVE-2018-1000129 ]..." — $0 — xn--`-zqpaaaaaa
- [Report #2321874](https://hackerone.com/reports/2321874) — "DOM Based Reflected Cross Site..." — $0 — MTN Group

---

### Scenario 6: XSS in Email Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 67 reports used this pattern
**Average bounty for this scenario:** $452

#### Prerequisites
- The application processes untrusted input in the XSS in Email context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to XSS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

#### Step-by-Step Attack

1. Identify the input vector within the application that maps to the vulnerable context.
2. Inject a benign canary value (e.g. `xyzztest`) to verify reflection or processing.
3. Observe how the context translates the canary value. Identify forbidden characters.
4. Craft an execution sequence escaping the context boundaries. Use variations if WAF intervenes.
5. Observe: The application structurally parses the execution sequence as active code/metadata rather than raw text.
6. Contrast: A patched response safely literalizes the input, rendering it completely inert.

> [!EXAMPLE]
> A classic example of this involves bypassing frontend sanitization to trigger backend processing.

#### Proof of Concept

```http
POST /api/v1/trigger/xss_in_email HTTP/1.1
Host: target.com
Content-Type: application/json

{"payload": "injection_sequence_here"}
```

Expected response contains:
```http
HTTP/1.1 200 OK

{"result": "execution_successful"}
```

#### Impact
This execution pattern critically undermines the integrity of the application, empowering the attacker to commandeer session identity, access underlying operating systems, or exfiltrate massive amounts of sensitive internal data depending on the deployment role.

#### Report Evidence
- [Report #1935628](https://hackerone.com/reports/1935628) — "HTML injection possible with soft..." — $1060 — GitLab
- [Report #3357036](https://hackerone.com/reports/3357036) — "Mail stored HTML injection in..." — $350 — Nextcloud

---

### Scenario 7: XSS via Open Redirect Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 51 reports used this pattern
**Average bounty for this scenario:** $100

#### Prerequisites
- The application processes untrusted input in the XSS via Open Redirect context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to XSS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

#### Step-by-Step Attack

1. Identify the input vector within the application that maps to the vulnerable context.
2. Inject a benign canary value (e.g. `xyzztest`) to verify reflection or processing.
3. Observe how the context translates the canary value. Identify forbidden characters.
4. Craft an execution sequence escaping the context boundaries. Use variations if WAF intervenes.
5. Observe: The application structurally parses the execution sequence as active code/metadata rather than raw text.
6. Contrast: A patched response safely literalizes the input, rendering it completely inert.

> [!EXAMPLE]
> A classic example of this involves bypassing frontend sanitization to trigger backend processing.

#### Proof of Concept

```http
POST /api/v1/trigger/xss_via_open_redirect HTTP/1.1
Host: target.com
Content-Type: application/json

{"payload": "injection_sequence_here"}
```

Expected response contains:
```http
HTTP/1.1 200 OK

{"result": "execution_successful"}
```

#### Impact
This execution pattern critically undermines the integrity of the application, empowering the attacker to commandeer session identity, access underlying operating systems, or exfiltrate massive amounts of sensitive internal data depending on the deployment role.

#### Report Evidence
- [Report #2611305](https://hackerone.com/reports/2611305) — "Potential XSS Vulnerability in..." — $100 — Acronis
- [Report #2653342](https://hackerone.com/reports/2653342) — "Potential XSS in redirect_url..." — $0 — Acronis

---

### Scenario 8: Blind XSS Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 35 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the Blind XSS context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to XSS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

#### Step-by-Step Attack

1. Identify the input vector within the application that maps to the vulnerable context.
2. Inject a benign canary value (e.g. `xyzztest`) to verify reflection or processing.
3. Observe how the context translates the canary value. Identify forbidden characters.
4. Craft an execution sequence escaping the context boundaries. Use variations if WAF intervenes.
5. Observe: The application structurally parses the execution sequence as active code/metadata rather than raw text.
6. Contrast: A patched response safely literalizes the input, rendering it completely inert.

> [!EXAMPLE]
> A classic example of this involves bypassing frontend sanitization to trigger backend processing.

#### Proof of Concept

```http
POST /api/v1/trigger/blind_xss HTTP/1.1
Host: target.com
Content-Type: application/json

{"payload": "injection_sequence_here"}
```

Expected response contains:
```http
HTTP/1.1 200 OK

{"result": "execution_successful"}
```

#### Impact
This execution pattern critically undermines the integrity of the application, empowering the attacker to commandeer session identity, access underlying operating systems, or exfiltrate massive amounts of sensitive internal data depending on the deployment role.

#### Report Evidence
- [Report #666040](https://hackerone.com/reports/666040) — "Blind XSS on admin.acronis.com via..." — $0 — Acronis
- [Report #923912](https://hackerone.com/reports/923912) — "Blind Stored XSS on..." — $0 — U.S. Dept Of Defense

---

### Scenario 9: Self-XSS Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 35 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the Self-XSS context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to XSS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

#### Step-by-Step Attack

1. Identify the input vector within the application that maps to the vulnerable context.
2. Inject a benign canary value (e.g. `xyzztest`) to verify reflection or processing.
3. Observe how the context translates the canary value. Identify forbidden characters.
4. Craft an execution sequence escaping the context boundaries. Use variations if WAF intervenes.
5. Observe: The application structurally parses the execution sequence as active code/metadata rather than raw text.
6. Contrast: A patched response safely literalizes the input, rendering it completely inert.

> [!EXAMPLE]
> A classic example of this involves bypassing frontend sanitization to trigger backend processing.

#### Proof of Concept

```http
POST /api/v1/trigger/self-xss HTTP/1.1
Host: target.com
Content-Type: application/json

{"payload": "injection_sequence_here"}
```

Expected response contains:
```http
HTTP/1.1 200 OK

{"result": "execution_successful"}
```

#### Impact
This execution pattern critically undermines the integrity of the application, empowering the attacker to commandeer session identity, access underlying operating systems, or exfiltrate massive amounts of sensitive internal data depending on the deployment role.

#### Report Evidence
- [Report #1029668](https://hackerone.com/reports/1029668) — "Self xss in product reviews" — $0 — Shopify
- [Report #1397940](https://hackerone.com/reports/1397940) — "Self-XSS due to image URL can be..." — $0 — Judge.me

---

### Scenario 10: CSP Bypass XSS Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 30 reports used this pattern
**Average bounty for this scenario:** $463

#### Prerequisites
- The application processes untrusted input in the CSP Bypass XSS context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to XSS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

#### Step-by-Step Attack

1. Identify the input vector within the application that maps to the vulnerable context.
2. Inject a benign canary value (e.g. `xyzztest`) to verify reflection or processing.
3. Observe how the context translates the canary value. Identify forbidden characters.
4. Craft an execution sequence escaping the context boundaries. Use variations if WAF intervenes.
5. Observe: The application structurally parses the execution sequence as active code/metadata rather than raw text.
6. Contrast: A patched response safely literalizes the input, rendering it completely inert.

> [!EXAMPLE]
> A classic example of this involves bypassing frontend sanitization to trigger backend processing.

#### Proof of Concept

```http
POST /api/v1/trigger/csp_bypass_xss HTTP/1.1
Host: target.com
Content-Type: application/json

{"payload": "injection_sequence_here"}
```

Expected response contains:
```http
HTTP/1.1 200 OK

{"result": "execution_successful"}
```

#### Impact
This execution pattern critically undermines the integrity of the application, empowering the attacker to commandeer session identity, access underlying operating systems, or exfiltrate massive amounts of sensitive internal data depending on the deployment role.

#### Report Evidence
- [Report #1941767](https://hackerone.com/reports/1941767) — "MetaMask Browser (on Android) does..." — $800 — MetaMask
- [Report #2905532](https://hackerone.com/reports/2905532) — "[CVE-2024-54133]..." — $126 — Internet Bug Bounty

---

### Scenario 11: XSS via Markdown Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 19 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the XSS via Markdown context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to XSS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

#### Step-by-Step Attack

1. Identify the input vector within the application that maps to the vulnerable context.
2. Inject a benign canary value (e.g. `xyzztest`) to verify reflection or processing.
3. Observe how the context translates the canary value. Identify forbidden characters.
4. Craft an execution sequence escaping the context boundaries. Use variations if WAF intervenes.
5. Observe: The application structurally parses the execution sequence as active code/metadata rather than raw text.
6. Contrast: A patched response safely literalizes the input, rendering it completely inert.

> [!EXAMPLE]
> A classic example of this involves bypassing frontend sanitization to trigger backend processing.

#### Proof of Concept

```http
POST /api/v1/trigger/xss_via_markdown HTTP/1.1
Host: target.com
Content-Type: application/json

{"payload": "injection_sequence_here"}
```

Expected response contains:
```http
HTTP/1.1 200 OK

{"result": "execution_successful"}
```

#### Impact
This execution pattern critically undermines the integrity of the application, empowering the attacker to commandeer session identity, access underlying operating systems, or exfiltrate massive amounts of sensitive internal data depending on the deployment role.

#### Report Evidence
- [Report #1014459](https://hackerone.com/reports/1014459) — "Stored XSS in any message..." — $0 — Rocket.Chat
- [Report #1023787](https://hackerone.com/reports/1023787) — "Stored XSS in markdown file with..." — $0 — Nextcloud

---
