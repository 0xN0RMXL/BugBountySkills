# SKILL: Workflow Orchestration
## Version: 1.0 | Domain: automation

---

## TOOLS BY COMPLEXITY
| Tool | Complexity | Use case |
|------|-----------|----------|
| bash + cron | Low | Solo, ≤10 targets |
| systemd timers | Low | Solo, better restart |
| make | Low | Ad-hoc pipelines |
| axiom | Med | Distributed across cheap VPSes |
| Prefect / Dagster | Med | Python-native DAGs |
| Apache Airflow | High | Team / large infra |
| Temporal / Argo | High | Cloud-native, k8s |

## AXIOM SETUP
```bash
# Install
bash <(curl -s https://raw.githubusercontent.com/pry0cc/axiom/master/interact/axiom-configure)
# Spin fleet
axiom-fleet hunt -i 10
# Run distributed
axiom-scan all_subs.txt -m httpx -p 80,443,8080,8443 -o probed.txt
axiom-scan probed.txt -m nuclei -t ~/nuclei-templates/ -severity high,critical
# Tear down
axiom-rm '*' -f
```

## DAG EXAMPLE (Prefect)
```python
from prefect import flow, task

@task
def subfinder(domain):
    return run(f"subfinder -d {domain} -all -silent")

@task
def probe(subs):
    return run(f"echo '{subs}' | httpx -silent")

@task
def nuclei_scan(alive):
    return run(f"echo '{alive}' | nuclei -severity high,critical")

@flow
def recon(domain):
    subs = subfinder(domain)
    alive = probe(subs)
    findings = nuclei_scan(alive)
    return findings

if __name__ == '__main__':
    recon.serve(name="recon")
```

## REFERENCES
axiom docs, Prefect docs, Apache Airflow
