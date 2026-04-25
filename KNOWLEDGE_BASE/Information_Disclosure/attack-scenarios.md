---
vuln_type: "Information_Disclosure"
file_type: "scenarios"
total_reports: "556"
avg_bounty: "2257"
max_bounty: "25000"
severity_distribution: "critical:7% high:6% medium:13% low:74%"
owasp_categories: ["A02:2021"]
common_cwe: ["CWE-200"]
last_updated: "2026-04-09"
tags: ["Information_Disclosure", "web", "api", "A02", "hunter-kb"]
related_vulns: ["Broken_Access_Control", "SSRF"]
---
# Information Disclosure — Attack Scenarios

 This step-by-step reconstruction faithfully dictates the precise procedural methodology implemented by top earners across the platform to accurately recreate the vulnerability sequence on production instances. This step-by-step reconstruction faithfully dictates the precise procedural methodology implemented by top earners across the platform to accurately recreate the vulnerability sequence on production instances.

---
### Scenario 1: General Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 226 reports used this pattern
**Average bounty for this scenario:** $1,628

#### Prerequisites
- The application processes untrusted input in the General context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Information_Disclosure processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
- [Report #2505761](https://hackerone.com/reports/2505761) — "Information Leakage via Clicked Link..." — $4000 — GitHub
- [Report #3082917](https://hackerone.com/reports/3082917) — "Possible Sensitive..." — $2162 — Internet Bug Bounty

---

### Scenario 2: Internal IP/Infrastructure Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 147 reports used this pattern
**Average bounty for this scenario:** $1,588

#### Prerequisites
- The application processes untrusted input in the Internal IP/Infrastructure context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Information_Disclosure processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/internal_ip/infrastructure HTTP/1.1
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
- [Report #1707287](https://hackerone.com/reports/1707287) — "CVE-2022-40604: Apache..." — $8000 — Internet Bug Bounty
- [Report #2798380](https://hackerone.com/reports/2798380) — "Hackerone supports accounts..." — $2500 — HackerOne

---

### Scenario 3: API Key/Secret Exposure Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 100 reports used this pattern
**Average bounty for this scenario:** $807

#### Prerequisites
- The application processes untrusted input in the API Key/Secret Exposure context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Information_Disclosure processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/api_key/secret_exposure HTTP/1.1
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
- [Report #2915647](https://hackerone.com/reports/2915647) — "Netlify Authentication Token..." — $6000 — Mozilla
- [Report #2828271](https://hackerone.com/reports/2828271) — "Apache Airflow:..." — $541 — Internet Bug Bounty

---

### Scenario 4: PII Exposure Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 89 reports used this pattern
**Average bounty for this scenario:** $6,950

#### Prerequisites
- The application processes untrusted input in the PII Exposure context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Information_Disclosure processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/pii_exposure HTTP/1.1
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
- [Report #1618347](https://hackerone.com/reports/1618347) — "Disclosing  PolicyPageAssetGroup..." — $25000 — HackerOne
- [Report #2798380](https://hackerone.com/reports/2798380) — "Hackerone supports accounts..." — $2500 — HackerOne

---

### Scenario 5: Debug/Stack Trace Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 38 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the Debug/Stack Trace context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Information_Disclosure processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/debug/stack_trace HTTP/1.1
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
- [Report #2765259](https://hackerone.com/reports/2765259) — "Information disclosure due to..." — $0 — MTN Group
- [Report #3019290](https://hackerone.com/reports/3019290) — "Exposure of Sensitive..." — $0 — U.S. Dept Of Defense

---

### Scenario 6: Directory Listing Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 30 reports used this pattern
**Average bounty for this scenario:** $100

#### Prerequisites
- The application processes untrusted input in the Directory Listing context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Information_Disclosure processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/directory_listing HTTP/1.1
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
- [Report #2376909](https://hackerone.com/reports/2376909) — "Possible to enumerate valid files..." — $100 — Nextcloud
- [Report #2311179](https://hackerone.com/reports/2311179) — "Directory Listing of publicly..." — $0 — Nextcloud

---

### Scenario 7: Source Code Disclosure Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 29 reports used this pattern
**Average bounty for this scenario:** $250

#### Prerequisites
- The application processes untrusted input in the Source Code Disclosure context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to Information_Disclosure processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/source_code_disclosure HTTP/1.1
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
- [Report #1008364](https://hackerone.com/reports/1008364) — "Large Amounts of Back-End Acronis..." — $250 — Acronis
- [Report #2784712](https://hackerone.com/reports/2784712) — "Information Disclosure Due To..." — $0 — AWS VDP

---
