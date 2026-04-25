# SKILL: Monitoring Scope Changes
## Version: 1.0 | Domain: automation

---

## STRATEGY
Programs change scope. New asset = first-mover advantage. Diff scope page hourly.

## SCRIPT
```bash
#!/usr/bin/env bash
TARGET=$1
URL="https://hackerone.com/${TARGET}/policy_scopes/all_eligible/json"
DIR="$HOME/scope_watch/${TARGET}"
mkdir -p "$DIR"
curl -sk "$URL" -o "$DIR/now.json"
[ -f "$DIR/last.json" ] || cp "$DIR/now.json" "$DIR/last.json"
diff <(jq -S . "$DIR/last.json") <(jq -S . "$DIR/now.json") > "$DIR/diff.txt"
if [ -s "$DIR/diff.txt" ]; then
  cat "$DIR/diff.txt" | python3 ~/scripts/notify_discord.py "[$TARGET] scope changed"
  cp "$DIR/now.json" "$DIR/last.json"
fi
```

## CRON
```
*/15 * * * * /home/ubuntu/scripts/scope_watch.sh hackerone-target
```

## TOOLS
- bbscope (collect raw)
- chaos for project-discovery dumps

## REFERENCES
chaos.projectdiscovery.io
