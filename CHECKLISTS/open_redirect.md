# Checklist: Open Redirect
- [ ] Find redirect parameters (url, redirect, next, return, callback, dest, link, ref)
- [ ] Test //attacker.tld
- [ ] Test http://allowed.tld@attacker.tld
- [ ] Test backslash variants \\\\attacker.tld, \\/attacker.tld
- [ ] Test data:, javascript: schemes (if response renders as link)
- [ ] Test CRLF injection in redirect
- [ ] Chain with OAuth flow → token leak → ATO
- [ ] Test SAML RelayState
- [ ] Test password reset URL → leak token via referer
