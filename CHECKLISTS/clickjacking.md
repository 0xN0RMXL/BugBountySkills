# Checklist: Clickjacking
- [ ] Check for X-Frame-Options / Content-Security-Policy frame-ancestors
- [ ] If missing → test with iframe
- [ ] Check sensitive endpoints (account delete, transfer, OAuth approve)
- [ ] Build PoC with overlay button
- [ ] Show impact (state-changing action triggered without consent)
