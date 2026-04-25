---
vuln_type: "Rate_Limit_Bypass"
file_type: "methodology"
total_reports: "184"
avg_bounty: "200"
max_bounty: "200"
severity_distribution: "critical:1% high:1% medium:3% low:95%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Rate_Limit_Bypass", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Rate Limit Bypass — Hunting Methodology

 The methodical execution of this phase guarantees definitive coverage over the targeted attack surface, enabling comprehensive discovery without alerting defensive mechanisms.

### Phase 1: Reconnaissance
**Step 1.1 — Map all input vectors**
Use Burp Suite's passive scanner while browsing the application normally. Every parameter that appears in the response source is a reflection candidate.

**Step 1.2 — JavaScript source analysis**
Download all frontend Javascript bundles. Look for routing paths and state manipulators.

> [!TIP]
> Always diff authenticated versus unauthenticated routes. The delta mapping usually exposes hidden parameters.

### Phase 2: Attack Surface Mapping
**Step 2.1 — Enumerate hidden parameters**
Utilize tools like Arjun to brute-force undocumented parameters on existing API paths.

**Step 2.2 — Identify integrations**
Scan for webhook inputs, file upload portals, and third-party integrations like OAuth flows.

### Phase 3: Discovery & Detection
**Step 3.1 — Inject benign tokens**
Submit `canary123` to all mapped parameters and search the HTTP responses for exact positioning.

**Step 3.2 — Test structural bounds**
Submit `<"';{` and monitor error logs or reflection encoding mechanisms.

> [!TIP]
> Use Burp Intruder to spray boundary checks across the entire request schema sequentially.

### Phase 4: Verification & Proof of Concept
**Step 4.1 — Confirm execution context**
Trigger an out-of-band callback (e.g. Collaborator) or a visual alert demonstrating absolute state subversion.

**Step 4.2 — Confirm bypasses**
If WAF blocks occur, test encoding matrices natively until a payload bypass variant achieves identical execution.

### Phase 5: Impact Escalation
**Step 5.1 — Access sensitive functionality**
Attempt to chain the execution to read internal configuration endpoints or steal the administrative session cookie.

**Step 5.2 — Confirm broader context**
Demonstrate if the execution can affect all active tenants or strictly the isolated user.

> [!TIP]
> Bounties scale proportionally with demonstrated business risk. Don't stop at `alert(1)`.

### Phase 6: Report Writing for Maximum Payout
**Step 6.1 — Document precise reproduction steps**
Specify the exact HTTP request required with step-by-step UI actions.

**Step 6.2 — Detail business impact**
Explicitly state how this bypasses the security boundary and affects user confidentiality or integrity.

## Decision Tree

IF you find a parameter reflected in HTML response body
  → Try basic injection: `<b>test</b>`
  → If bold text renders: proceed to basic section
  → If plain text output: check if encoding is happening → try encoding bypasses

IF you find a parameter interacting with the backend interpreter directly
  → You are in a dynamic code context
  → Try breaking out of structural encapsulation: `'; print("test"); //`

## Grep Patterns for Code Review

```bash
# Find dangerous reflections and internal references
grep -rn "\.html\(.*\$\|\.append\(.*\$\|\.prepend\(.*\$" --include="*.js" .

# Find structural processing functions
grep -rn "document\.write" --include="*.js" .
```
