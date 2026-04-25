---
vuln_type: "RCE"
file_type: "scenarios"
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


# RCE — Attack Scenarios

 This step-by-step reconstruction faithfully dictates the precise procedural methodology implemented by top earners across the platform to accurately recreate the vulnerability sequence on production instances.

---

### Scenario 1: General Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 237 reports used this pattern
**Average bounty for this scenario:** $173

#### Prerequisites
- The application processes untrusted input in the General context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to RCE processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
- [Report #2221404](https://hackerone.com/reports/2221404) — "RCE on worker host due to..." — $500 — Mozilla
- [Report #924493](https://hackerone.com/reports/924493) — "Acronis Sync Agent Service -..." — $250 — Acronis

---

### Scenario 2: File Upload RCE Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 150 reports used this pattern
**Average bounty for this scenario:** $648

#### Prerequisites
- The application processes untrusted input in the File Upload RCE context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to RCE processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/file_upload_rce HTTP/1.1
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
- [Report #3031518](https://hackerone.com/reports/3031518) — "CVE-2025-24813: Remote..." — $4323 — Internet Bug Bounty
- [Report #1004740](https://hackerone.com/reports/1004740) — "DLL Hijacking when performing..." — $250 — Acronis

---

### Scenario 3: Command Injection Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 93 reports used this pattern
**Average bounty for this scenario:** $64

#### Prerequisites
- The application processes untrusted input in the Command Injection context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to RCE processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/command_injection HTTP/1.1
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
- [Report #2705661](https://hackerone.com/reports/2705661) — "CVE-2024-45498: Apache..." — $126 — Internet Bug Bounty
- [Report #2778350](https://hackerone.com/reports/2778350) — "Cisco IOS XE instance at ████..." — $1 — MTN Group

---

### Scenario 4: Deserialization RCE Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 26 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the Deserialization RCE context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to RCE processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/deserialization_rce HTTP/1.1
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
- [Report #2611669](https://hackerone.com/reports/2611669) — "[Switch, PIA/MK8DX] Stack buffer..." — $0 — github.com
- [Report #2762119](https://hackerone.com/reports/2762119) — "CVE-2017-9822 DotNetNuke Cookie..." — $0 — MTN Group

---

### Scenario 5: Code Injection Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 13 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the Code Injection context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to RCE processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/code_injection HTTP/1.1
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
- [Report #1425563](https://hackerone.com/reports/1425563) — "Remote code injection in Log4j on..." — $0 — MTN Group
- [Report #1425565](https://hackerone.com/reports/1425565) — "Remote code injection in Log4j on..." — $0 — MTN Group

---

### Scenario 6: SSTI/Template Injection Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 5 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the SSTI/Template Injection context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to RCE processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/ssti/template_injection HTTP/1.1
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
- [Report #1423496](https://hackerone.com/reports/1423496) — "██████████ running a..." — $0 — U.S. Dept Of Defense
- [Report #1438393](https://hackerone.com/reports/1438393) — "███ ████████ running a..." — $0 — U.S. Dept Of Defense

---

### Scenario 7: Server-Side Prototype Pollution Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 5 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the Server-Side Prototype Pollution context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to RCE processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/server-side_prototype_pollution HTTP/1.1
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
- [Report #1631258](https://hackerone.com/reports/1631258) — "Rocket.Chat Server RCE" — $0 — Rocket.Chat
- [Report #719856](https://hackerone.com/reports/719856) — "Prototype..." — $0 — Node.js third-party modules

---
