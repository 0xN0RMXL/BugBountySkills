# SKILL: Recon Automation Pipeline
## Version: 1.0 | Domain: recon | Trigger: scaling — running recon across N programs continuously

---

## IDENTITY IN THIS SKILL
Stitch all recon stages into a single repeatable pipeline. Trigger on: program scope changes, new subdomain CT log entry, new GitHub commit. Notify via Telegram/Discord. Persist deltas in Git. Re-run every 6h.

---

## TOOLS
(see commands)

## COMMANDS & WORKFLOWS
### Skeleton recon_pipeline.sh
```bash
#!/usr/bin/env bash
set -euo pipefail
TARGET=$1
DATE=$(date +%Y%m%d-%H%M)
OUT=$HOME/hunting/$TARGET/$DATE
mkdir -p "$OUT" && cd "$OUT"

# 1. Passive subs
subfinder -d "$TARGET" -all -silent | tee subs_subfinder.txt
chaos-client -d "$TARGET" -silent | tee subs_chaos.txt
github-subdomains -d "$TARGET" -t "$GITHUB_TOKEN" -o subs_github.txt
cat subs_*.txt | sort -u > subs.txt

# 2. Permute + resolve
alterx -l subs.txt -enrich -silent > permutations.txt
puredns resolve permutations.txt -r ~/.config/resolvers.txt --wildcard-batch 1500000 -q > resolved.txt
cat subs.txt resolved.txt | sort -u > all_subs.txt

# 3. Probe
httpx -l all_subs.txt -threads 100 -timeout 7 -follow-redirects \
      -status-code -title -tech-detect -ip -cdn -tls-grab -web-server \
      -json -o httpx.jsonl
cat httpx.jsonl | jq -r .url > alive.txt

# 4. Crawl + URLs
katana -list alive.txt -d 3 -jc -kf all -silent -o crawl.txt
cat alive.txt | gau --threads 10 --subs > gau.txt
cat crawl.txt gau.txt | sort -u | uro > all_urls.txt

# 5. JS analysis
mkdir -p js
grep -E '\.js(\?|$)' all_urls.txt | sort -u > js_urls.txt
cat js_urls.txt | xargs -I{} -P 20 curl -sk --max-time 10 -o "js/$(echo {} | md5sum | cut -d' ' -f1).js" "{}"
trufflehog filesystem js --only-verified --json > js_secrets.json

# 6. Vuln scan
nuclei -l alive.txt -severity medium,high,critical -t ~/nuclei-templates/ -t ~/custom-templates/ -rl 100 -timeout 10 -silent -o nuclei.txt -json -store-resp -store-resp-dir nuclei_resp/

# 7. Diff vs last run
PREV=$(ls -1 ~/hunting/$TARGET/ | sort | grep -v "^$DATE" | tail -1)
if [ -n "$PREV" ]; then
    comm -23 <(sort all_subs.txt) <(sort ~/hunting/$TARGET/$PREV/all_subs.txt) > new_subs.txt
    comm -23 <(sort all_urls.txt) <(sort ~/hunting/$TARGET/$PREV/all_urls.txt) > new_urls.txt
fi

# 8. Notify
[ -s nuclei.txt ] && python3 ~/scripts/notify_tg.py --file nuclei.txt --title "[$TARGET] nuclei findings"
[ -s new_subs.txt ] && python3 ~/scripts/notify_tg.py --file new_subs.txt --title "[$TARGET] new subdomains"

```

### Cron entry
```bash
# Run every 6 hours at 5 minutes past
5 */6 * * * /home/ubuntu/scripts/recon_pipeline.sh example.com >> /var/log/recon-example.log 2>&1
```

### Telegram notifier (Python)
```bash
import os, sys, requests, argparse
TOKEN = os.environ['TG_BOT_TOKEN']
CHAT  = os.environ['TG_CHAT_ID']
ap = argparse.ArgumentParser()
ap.add_argument('--file', required=True)
ap.add_argument('--title', required=True)
a = ap.parse_args()
text = open(a.file).read()[:3500]
requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',
              data={'chat_id': CHAT, 'text': f'*{a.title}*\n```\n{text}\n```', 'parse_mode': 'Markdown'})

```

### Discord notifier
```bash
import os, sys, requests
WH = os.environ['DISCORD_WEBHOOK']
title = sys.argv[1]; body = open(sys.argv[2]).read()[:1900]
requests.post(WH, json={'content': f'**{title}**\n```\n{body}\n```'})

```

### certstream live-listener (new cert hit → trigger)
```bash
import certstream, re, requests, os, json
TARGETS = open('~/hunting/targets.txt').read().splitlines()
def cb(msg, ctx):
    if msg['message_type'] != 'certificate_update': return
    for d in msg['data']['leaf_cert']['all_domains']:
        for t in TARGETS:
            if d.endswith(t):
                requests.post(os.environ['DISCORD_WEBHOOK'],
                              json={'content': f'NEW CERT: {d} (issuer: {msg["data"]["chain"][0]["subject"]["CN"]})'})
                # trigger pipeline
                os.system(f'/home/ubuntu/scripts/recon_pipeline.sh {t} &')
certstream.listen_for_events(cb, url='wss://certstream.calidog.io')

```

### axiom — distributed across N VPSes
```bash
axiom-init mybox && axiom-fleet hunt -i 5
axiom-scan all_subs.txt -m httpx -p 80,443,8080,8443
axiom-scan alive.txt -m nuclei -t ~/nuclei-templates/
axiom-rm '*' -f
```



## STACK

## Reference architecture

```
                                       ┌──────────────────────────────┐
[CronJob 6h] ──► recon_pipeline.sh ──► │  artifacts/<target>/<date>/  │
       │                               │   subs.txt, alive.txt,        │
       │                               │   tech.json, urls.txt,        │
       │                               │   nuclei.json, secrets.json   │
       │                               └──────────────┬───────────────┘
       │                                              │
       │                                              ▼
       │                                       diff against last run
       │                                              │
       │                                              ▼
       └─► [scope-monitor] ──► program-scope.txt ──► diff_handler.py ──► Telegram bot
                                                                       └► Discord webhook
                                                                       └► commit deltas to Git
```

Use **[axiom](https://github.com/pry0cc/axiom)** for distributed scanning across cheap VPSes (DigitalOcean / Linode).


## EDGE CASES
- **Token rotation** — gitdorker / GitHub API gets you to ~5K req/h per token; rotate 5+ to keep up.
- **Resolver poisoning** — public resolvers occasionally return wildcards / poisoned A records. Use a curated resolver list (trickest/resolvers).
- **False-positive flood from nuclei** — keep a `~/.nuclei-ignore.yaml` to silence templates that always alert (e.g. CSP misconfig info-level on every host).
- **Notify spam** — diff before notifying. Only ping when the delta has lines.
- **State drift** — pipeline writes to a dated dir; diff against `last`. Symlink `last → <newest>` after each run.
- **Self-DoS** — running this against your own production targets at high concurrency may breach program rate-limit clauses. Throttle.

## OUTPUT FORMAT
```
RECON_AUTOMATION_PIPELINE({target}):
  <key>: <value>
  ...
NEXT: handoff to next stage
```

## SOURCES
- Bug Hunters Methodology Live Day One Recon (jhaddix)
- zseanos-methodology
- Elite_BugBounty_Methodology
- ProjectDiscovery / Assetnote / SecLists
- HackTricks recon section
- PortSwigger Research blog
