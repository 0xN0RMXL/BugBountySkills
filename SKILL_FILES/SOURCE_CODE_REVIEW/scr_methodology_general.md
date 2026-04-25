# SKILL: Source Code Review — General Methodology
## Version: 1.0 | Domain: scr

---

## IDENTITY
SCR finds the bugs scanners miss. I read code language-by-language, framework-by-framework, looking for trust boundaries, dangerous sinks, and missing controls.

## METHODOLOGY
1. **Map architecture** — entry points (HTTP routes, CLI, queue consumers), trust boundaries, data flow.
2. **Identify trust sources** — request body, query, headers, files, env vars, DB, external API responses.
3. **Trace to sinks** — DB queries, command exec, file ops, deserialization, eval, template render, HTTP fetch.
4. **Check controls** — auth middleware, input validation, output encoding, rate limit, CSRF token.
5. **Flag anti-patterns** — eval, exec, raw SQL, unbounded recursion, unbounded loops, debug code.

## TOOLS
- semgrep — pattern-based static analysis
- CodeQL — query-based deep analysis
- bandit (Python), brakeman (Rails), gosec (Go), eslint-plugin-security (JS), spotbugs+findsecbugs (Java)
- gitleaks, trufflehog (secrets)
- snyk, dependabot (dependencies)

## SEMGREP RULESETS
```bash
# Auto rules (covers most languages)
semgrep --config=auto src/

# Specific
semgrep --config=p/security-audit src/
semgrep --config=p/owasp-top-ten src/
semgrep --config=p/secrets src/
semgrep --config=p/r2c-ci src/
```

## CODEQL
```bash
codeql database create db --language=javascript --source-root=.
codeql database analyze db codeql/javascript-security-and-quality.qls --format=sarif-latest -o results.sarif
```

## CHECKLIST PER PR REVIEW
- [ ] Any new authentication / authorization paths?
- [ ] Any new SQL queries / template renders?
- [ ] Any new file uploads / downloads?
- [ ] Any new dependencies?
- [ ] Any new env-var reads (esp. with default fallback)?
- [ ] Any TODO/FIXME/HACK comments?
- [ ] Any commented-out code that hides logic?

## REFERENCES
OWASP Code Review Guide • Secure Code Review (Tanya Janca)
