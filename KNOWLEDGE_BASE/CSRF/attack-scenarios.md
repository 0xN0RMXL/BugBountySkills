---
vuln_type: "CSRF"
file_type: "scenarios"
total_reports: "289"
avg_bounty: "350"
max_bounty: "500"
severity_distribution: "critical:1% high:2% medium:4% low:93%"
owasp_categories: ["A04:2021"]
common_cwe: ["CWE-352"]
last_updated: "2026-04-09"
tags: ["CSRF", "web", "api", "A04", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# CSRF — Attack Scenarios

 This step-by-step reconstruction faithfully dictates the precise procedural methodology implemented by top earners across the platform to accurately recreate the vulnerability sequence on production instances.

---

### Scenario 1: General Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 166 reports used this pattern
**Average bounty for this scenario:** $350

#### Prerequisites
- The application processes untrusted input in the General context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to CSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
- [Report #3253725](https://hackerone.com/reports/3253725) — "SameSite restrictions are..." — $500 — Brave Software
- [Report #2513333](https://hackerone.com/reports/2513333) — "csrftoken not unique to session or..." — $500 — Mozilla

---

### Scenario 2: State-Changing CSRF Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 58 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the State-Changing CSRF context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to CSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/state-changing_csrf HTTP/1.1
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
- [Report #2652603](https://hackerone.com/reports/2652603) — "CSRF Attack on..." — $0 — U.S. Dept Of Defense
- [Report #2697588](https://hackerone.com/reports/2697588) — "CSRF Attack leads to..." — $0 — U.S. Dept Of Defense

---

### Scenario 3: Login CSRF Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 43 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the Login CSRF context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to CSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/login_csrf HTTP/1.1
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
- [Report #2999394](https://hackerone.com/reports/2999394) — "Pivilege escalation of any new..." — $0 — WordPress
- [Report #3269777](https://hackerone.com/reports/3269777) — "Replayable Password Change..." — $0 — Malwarebytes

---

### Scenario 4: JSON CSRF Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 32 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the JSON CSRF context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to CSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/json_csrf HTTP/1.1
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
- [Report #1049360](https://hackerone.com/reports/1049360) — "CSRF in changing users..." — $0 — Logitech
- [Report #1122408](https://hackerone.com/reports/1122408) — "CSRF on /api/graphql allows..." — $0 — GitLab

---

### Scenario 5: CSRF Token Bypass Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 29 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the CSRF Token Bypass context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to CSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/csrf_token_bypass HTTP/1.1
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
- [Report #3400761](https://hackerone.com/reports/3400761) — "curl’s persistence files inherit..." — $0 — curl
- [Report #1091403](https://hackerone.com/reports/1091403) — "CSRF Bypassed on Logout Endpoint" — $0 — Enjin

---
