# SKILL: Recon Pipeline Automation
## Version: 1.0 | Domain: automation

---

(See SKILL_FILES/RECON/16_recon_automation_pipeline.md for the full pipeline shell script. This file documents pipeline patterns specifically.)

## PATTERNS
1. **Idempotent stages** — each stage produces a deterministic output file; re-running doesn't duplicate effort.
2. **Diff-driven** — compare to last run, only process delta.
3. **Throttled** — respect program rate limits.
4. **Parallel-safe** — multiple targets concurrently without race.
5. **Fail-fast** — `set -euo pipefail` + non-zero exit on any stage failure.
6. **Observability** — log to file + push notification on critical events.
7. **Stateful** — persist `last/` symlinks between runs.

## ORCHESTRATION
- **bash + cron** — simplest, sufficient for solo hunting.
- **systemd timers** — better restart behavior than cron.
- **Apache Airflow** — DAG with retries, dependencies (overkill for solo).
- **Prefect / Dagster** — modern Python DAG orchestrators.
- **Make** — for ad-hoc one-shot pipelines.
- **axiom + tmux + cron** — distributed across cheap VPSes.

## REFERENCES
RECON/16_recon_automation_pipeline.md
