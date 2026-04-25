# SKILL: Telegram / Discord Notifications
## Version: 1.0 | Domain: automation

---

## TELEGRAM BOT SETUP
1. Talk to `@BotFather` → `/newbot` → get TOKEN.
2. Get chat_id: send any message to bot, then `curl https://api.telegram.org/bot<TOKEN>/getUpdates`.

## SCRIPT (Python)
```python
import os, requests, sys
def tg(text, files=None):
    TOKEN=os.environ['TG_BOT_TOKEN']; CHAT=os.environ['TG_CHAT_ID']
    if files:
        for f in files:
            requests.post(f'https://api.telegram.org/bot{TOKEN}/sendDocument',
                          data={'chat_id':CHAT,'caption':text[:1024]},
                          files={'document':open(f,'rb')})
    else:
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',
                      data={'chat_id':CHAT,'text':text[:4000],'parse_mode':'Markdown'})

if __name__ == '__main__':
    tg(sys.stdin.read(), sys.argv[1:])
```

## DISCORD WEBHOOK
1. Server settings → Integrations → Webhooks → New → copy URL.

## SCRIPT
```python
import os, requests, sys
WH = os.environ['DISCORD_WH']
def discord(text, file=None):
    if file:
        requests.post(WH, data={'content': text[:1900]}, files={'file': open(file,'rb')})
    else:
        requests.post(WH, json={'content': text[:1900]})
discord(sys.stdin.read(), sys.argv[1] if len(sys.argv)>1 else None)
```

## SLACK INCOMING WEBHOOK
```bash
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"new finding"}' $SLACK_WH
```

## REFERENCES
Telegram Bot API, Discord webhook docs
