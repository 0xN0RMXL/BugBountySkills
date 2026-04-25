# SKILL: Monitoring New Assets (Subdomains, IPs, Tech)
## Version: 1.0 | Domain: automation

---

## CERTSTREAM (LIVE CERT FEED)
```python
import certstream, os, requests
TARGETS = open('targets.txt').read().split()
def cb(msg, ctx):
    if msg.get('message_type') != 'certificate_update': return
    for d in msg['data']['leaf_cert']['all_domains']:
        for t in TARGETS:
            if d.endswith('.'+t) or d == t:
                requests.post(os.environ['DISCORD_WH'], json={'content': f'NEW CERT: {d}'})
certstream.listen_for_events(cb, url='wss://certstream.calidog.io')
```

## SUBDOMAIN DIFFING (CRON)
```bash
TARGET=$1
DIR=$HOME/subwatch/$TARGET
mkdir -p $DIR
subfinder -d $TARGET -all -silent | sort -u > $DIR/now.txt
[ -f $DIR/last.txt ] || cp $DIR/now.txt $DIR/last.txt
NEW=$(comm -23 $DIR/now.txt $DIR/last.txt)
[ -n "$NEW" ] && echo "$NEW" | python3 ~/scripts/notify_discord.py "[$TARGET] new subs"
cp $DIR/now.txt $DIR/last.txt
```

## ASSET FINGERPRINT WATCH
```bash
httpx -l alive.txt -tech-detect -title -ip -json > now.jsonl
diff <(jq -S . last.jsonl) <(jq -S . now.jsonl) | python3 notify.py "tech changed"
```

## REFERENCES
ProjectDiscovery chaos, certstream
