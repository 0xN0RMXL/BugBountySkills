# SKILL: Monitoring New Bug Bounty Programs
## Version: 1.0 | Domain: automation

---

## SOURCES
- HackerOne hacktivity → /hacktivity
- HackerOne directory → /directory/programs
- Bugcrowd programs → /programs/list
- Intigriti → /programs
- YesWeHack → /program
- Immunefi → /explore
- HackenProof → /programs
- Bug bounty roundups (Twitter @disclosedh1, @bugbounty)

## SCRIPT — H1 new program watcher
```python
import requests, json, time, os
SEEN=set(open('seen.txt').read().split()) if os.path.exists('seen.txt') else set()
while True:
    r = requests.get('https://hackerone.com/programs/search?query=&sort_type=published_at&page=1', headers={'Accept':'application/json'})
    for p in r.json()['programs']:
        if p['handle'] not in SEEN:
            requests.post(os.environ['DISCORD_WH'], json={'content': f"NEW: {p['name']} https://hackerone.com/{p['handle']}"})
            SEEN.add(p['handle']); open('seen.txt','a').write(p['handle']+'\\n')
    time.sleep(3600)
```

## CRON
```
*/30 * * * * /home/ubuntu/scripts/watch_h1.py >> /var/log/h1watch.log 2>&1
```

## TOOLS
- chaos.projectdiscovery.io — daily program-scope dumps
- bbscope — pull program scopes from H1/BC/IGT
- bbradar (community feed)

## REFERENCES
disclosed-h1.com, hackerone.com/hacktivity
