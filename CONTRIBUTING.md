# Contributing to BugBountySkills

## What to contribute

- **New techniques** — add to the relevant `KNOWLEDGE_BASE/<topic>.md`
- **New payloads** — append to `SKILL_FILES/PAYLOADS/<class>_payloads*.md`
- **New tool integrations** — add to `SKILL_FILES/AUTOMATION/` or `SKILL_FILES/SCRIPTING/`
- **New exploit chains** — append to `SKILL_FILES/EXPLOIT_DEVELOPMENT/exploit_chain_building.md`
- **New disclosed bug reports as case studies** — add to `KNOWLEDGE_BASE/`

## Format rules

Every addition must follow the standard template from the existing files:

```
What It Is → How to Find → How to Test → How to Exploit → Bypass Techniques →
Tools → Payloads → Real-World Examples → Common Mistakes → Severity → References → One-Liners
```

## Quality bar

- **No generic content** — specific, technical, actionable
- **Source-backed** — cite the writeup, CVE, or tool doc
- **Tool-complete** — exact command and flags, not pseudocode
- **Payload-ready** — real payloads, not `[INSERT PAYLOAD HERE]`
- **Copy-paste ready** — commands work as-is or with one obvious variable substitution

## Process

1. Fork → branch → edit → PR
2. PR title format: `[CATEGORY] Brief description`
   - Examples:
     - `[PAYLOAD] Add Unicode normalization XSS bypasses`
     - `[RECON] Add Censys query for Kubernetes API servers`
     - `[KB] Add prototype pollution → server RCE chain (Express)`
     - `[FIX] Correct ffuf flags in 15_content_discovery_fuzzing.md`
3. **One topic per PR** — keeps reviews fast.
4. All PRs reviewed within 7 days.

## Style

- Use fenced code blocks with the language tag (` ```bash `, ` ```python `, ` ```http `).
- Inline payloads should be in fenced blocks, not backticks, when they exceed one line.
- For tools, always include the **exact** command + flags + a one-line "what it does" comment.
- For payloads, group by **context** (HTML body / attribute / JS string / URL / etc.).
- For chains, use a numbered list: `1. Get X → 2. Pivot via Y → 3. Land Z`.

## What NOT to contribute

- Anything sourced from undisclosed reports without permission.
- Tools or techniques whose only use is unauthorized intrusion.
- AI-generated filler (e.g. "this vulnerability is critical because…" without specifics).
- Payloads / commands you haven't actually run.

## Need help?

Open an issue with the **`question`** label or use the [New Technique Submission](.github/ISSUE_TEMPLATE/new_technique.md) template if you want to discuss before writing.
