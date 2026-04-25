---
vuln_type: "ReDoS"
file_type: "scenarios"
total_reports: "29"
avg_bounty: "384"
max_bounty: "541"
severity_distribution: "critical:0% high:3% medium:8% low:89%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["ReDoS", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# ReDoS — Attack Scenarios

 This step-by-step reconstruction faithfully dictates the precise procedural methodology implemented by top earners across the platform to accurately recreate the vulnerability sequence on production instances.

---

### Scenario 1: General Attack Flow

**Difficulty:** Medium
**Frequency in corpus:** 29 reports used this pattern
**Average bounty for this scenario:** $385

#### Prerequisites
- The application processes untrusted input in the General context
- Parameter filtering allows structural escape characters

#### Target
This applies directly to ReDoS processing endpoints, specifically those handling API integrations, file structures, or parameter passing arrays.

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
- [Report #2807139](https://hackerone.com/reports/2807139) — "CVE-2024-49761: ReDoS..." — $541 — Internet Bug Bounty
- [Report #2792776](https://hackerone.com/reports/2792776) — "[CVE-2024-47888]..." — $505 — Internet Bug Bounty

---
