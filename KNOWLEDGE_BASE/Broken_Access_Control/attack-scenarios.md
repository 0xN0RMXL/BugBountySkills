---
vuln_type: "Broken_Access_Control"
file_type: "scenarios"
total_reports: "470"
avg_bounty: "1128"
max_bounty: "10000"
severity_distribution: "critical:10% high:10% medium:10% low:70%"
owasp_categories: ["A01:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Broken_Access_Control", "web", "api", "A01", "hunter-kb"]
related_vulns: ["Information_Disclosure", "SSRF"]
---


# Broken Access Control — Attack Scenarios

 This step-by-step reconstruction faithfully dictates the precise procedural methodology implemented by top earners across the platform to accurately recreate the vulnerability sequence on production instances. 

---

### Scenario 1: General Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 217 reports used this pattern
**Average bounty for this scenario:** $999

#### Prerequisites
- The application processes untrusted input in the General context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Broken_Access_Control processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
- [Report #2967634](https://hackerone.com/reports/2967634) — "Exposed proxy allows to access..." — $7500 — Reddit
- [Report #2528293](https://hackerone.com/reports/2528293) — "IDOR Exposes All Machine Learning..." — $1160 — GitLab

---

### Scenario 2: Missing Function Level Access Control Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 182 reports used this pattern
**Average bounty for this scenario:** $1,283

#### Prerequisites
- The application processes untrusted input in the Missing Function Level Access Control context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Broken_Access_Control processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/missing_function_level_access_control HTTP/1.1
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
- [Report #3124517](https://hackerone.com/reports/3124517) — "Arbitrary Read of Another Users..." — $10000 — GitHub
- [Report #1920908](https://hackerone.com/reports/1920908) — "Access to the business..." — $500 — Rockstar Games

---

### Scenario 3: Vertical Privilege Escalation Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 69 reports used this pattern
**Average bounty for this scenario:** $1,390

#### Prerequisites
- The application processes untrusted input in the Vertical Privilege Escalation context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Broken_Access_Control processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/vertical_privilege_escalation HTTP/1.1
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
- [Report #2885269](https://hackerone.com/reports/2885269) — "Shopify Partners Invitation Process..." — $3500 — partners.shopify.com
- [Report #2855610](https://hackerone.com/reports/2855610) — "Staff with Restricted Permissions..." — $1600 — Unknown Program

---

### Scenario 4: Horizontal Privilege Escalation Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 65 reports used this pattern
**Average bounty for this scenario:** $10,000

#### Prerequisites
- The application processes untrusted input in the Horizontal Privilege Escalation context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Broken_Access_Control processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/horizontal_privilege_escalation HTTP/1.1
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
- [Report #3124517](https://hackerone.com/reports/3124517) — "Arbitrary Read of Another Users..." — $10000 — GitHub
- [Report #3103849](https://hackerone.com/reports/3103849) — "Privilege Escalation leads to..." — $0 — Unknown Program

---

### Scenario 5: API Authorization Bypass Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 13 reports used this pattern
**Average bounty for this scenario:** $626

#### Prerequisites
- The application processes untrusted input in the API Authorization Bypass context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Broken_Access_Control processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/api_authorization_bypass HTTP/1.1
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
- [Report #3027461](https://hackerone.com/reports/3027461) — "Bypass of..." — $1250 — Cloudflare Public Bug Bounty
- [Report #3231321](https://hackerone.com/reports/3231321) — "HTTP Proxy Bypass via..." — $2 — curl

---
