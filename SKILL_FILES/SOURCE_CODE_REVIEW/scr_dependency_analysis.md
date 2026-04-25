# SKILL: Dependency Analysis
## Version: 1.0 | Domain: scr

---

## TOOLS
- **snyk** — comprehensive vuln DB + advisor
- **npm audit / yarn audit / pnpm audit**
- **pip-audit**
- **bundler-audit**
- **cargo audit**
- **govulncheck**
- **OWASP dependency-check**
- **Trivy** — multi-ecosystem
- **dependabot** (GitHub native)

## COMMANDS
```bash
# Node
npm audit --json
yarn audit --json
snyk test

# Python
pip-audit
safety check
snyk test --file=requirements.txt

# Ruby
bundler-audit check
brakeman

# Go
govulncheck ./...

# Rust
cargo audit

# Java
dependency-check.sh --scan src/
mvn dependency-check:check

# Multi-ecosystem
trivy fs --security-checks vuln src/
```

## DEPENDENCY CONFUSION
See VULNERABILITIES/WEB/dependency_confusion.md.
```bash
confused -l npm package.json
confused -l pypi requirements.txt
confused -l mvn pom.xml
```

## TYPOSQUATTING
- Check for slight misspellings of popular packages.
- `npm view PACKAGE` to see metadata before install.

## REFERENCES
Snyk vuln DB, GitHub Advisory Database, OSV.dev
