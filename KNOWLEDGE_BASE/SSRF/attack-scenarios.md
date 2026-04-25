---
vuln_type: "SSRF"
file_type: "scenarios"
total_reports: "214"
avg_bounty: "2954"
max_bounty: "4263"
severity_distribution: "critical:4% high:91% medium:5% low:0%"
owasp_categories: ["A10:2021"]
common_cwe: ["CWE-918"]
last_updated: "2026-04-09"
tags: ["SSRF", "web", "api", "A10", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control"]
---


# SSRF — Attack Scenarios

 This step-by-step reconstruction faithfully dictates the precise procedural methodology implemented by top earners across the platform to accurately recreate the vulnerability sequence on production instances.

---

### Scenario 1: Internal Service SSRF Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 77 reports used this pattern
**Average bounty for this scenario:** $2,000

#### Prerequisites
- The application processes untrusted input in the Internal Service SSRF context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to SSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/internal_service_ssrf HTTP/1.1
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
- [Report #3176157](https://hackerone.com/reports/3176157) — "DNS Rebinding SSRF..." — $2000 — github.com
- [Report #2932960](https://hackerone.com/reports/2932960) — "[my.stripo.email] Blind SSRF..." — $0 — Stripo Inc

---

### Scenario 2: General Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 68 reports used this pattern
**Average bounty for this scenario:** $3,432

#### Prerequisites
- The application processes untrusted input in the General context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to SSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
- [Report #2612028](https://hackerone.com/reports/2612028) — "important: Apache HTTP..." — $4263 — Internet Bug Bounty
- [Report #2585374](https://hackerone.com/reports/2585374) — "moderate: Apache HTTP..." — $2600 — Internet Bug Bounty

---

### Scenario 3: Blind SSRF Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 47 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the Blind SSRF context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to SSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/blind_ssrf HTTP/1.1
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
- [Report #2932960](https://hackerone.com/reports/2932960) — "[my.stripo.email] Blind SSRF..." — $0 — Stripo Inc
- [Report #1006599](https://hackerone.com/reports/1006599) — "Blind SSRF in ads.tiktok.com" — $0 — TikTok

---

### Scenario 4: File Read SSRF Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 41 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the File Read SSRF context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to SSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/file_read_ssrf HTTP/1.1
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
- [Report #3418646](https://hackerone.com/reports/3418646) — "Arbitrary Configuration File..." — $0 — curl
- [Report #3465156](https://hackerone.com/reports/3465156) — "Node.js permission model bypass via..." — $0 — Node.js

---

### Scenario 5: SSRF via Image/PDF Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 23 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the SSRF via Image/PDF context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to SSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/ssrf_via_image/pdf HTTP/1.1
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
- [Report #3024673](https://hackerone.com/reports/3024673) — "SSRF in Autodesk Rendering leading..." — $0 — Autodesk
- [Report #1049624](https://hackerone.com/reports/1049624) — "Abusing URL Parsers by long schema name" — $0 — curl

---

### Scenario 6: Cloud Metadata SSRF Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 21 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the Cloud Metadata SSRF context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to SSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/cloud_metadata_ssrf HTTP/1.1
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
- [Report #1055823](https://hackerone.com/reports/1055823) — "SSRF By adding a custom integration..." — $0 — Helium
- [Report #1108418](https://hackerone.com/reports/1108418) — "SSRF allows reading AWS EC2..." — $0 — Logitech

---

### Scenario 7: Webhook SSRF Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 6 reports used this pattern
**Average bounty for this scenario:** $0

#### Prerequisites
- The application processes untrusted input in the Webhook SSRF context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to SSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/webhook_ssrf HTTP/1.1
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
- [Report #1886954](https://hackerone.com/reports/1886954) — "Unauthenticated full-read SSRF..." — $0 — Rocket.Chat
- [Report #243277](https://hackerone.com/reports/243277) — "SSRF via webhook" — $0 — Mixmax

---

### Scenario 8: DNS Rebinding Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 5 reports used this pattern
**Average bounty for this scenario:** $2,000

#### Prerequisites
- The application processes untrusted input in the DNS Rebinding context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to SSRF processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
POST /api/v1/trigger/dns_rebinding HTTP/1.1
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
- [Report #3176157](https://hackerone.com/reports/3176157) — "DNS Rebinding SSRF..." — $2000 — github.com
- [Report #3383095](https://hackerone.com/reports/3383095) — "DNS Rebinding Attack" — $0 — arkadiyt-projects

---
