# Checklist: Race Conditions
- [ ] Find state-checked endpoints (redeem, withdraw, accept, claim, vote, reset)
- [ ] Use Burp Turbo Intruder race-single-packet-attack
- [ ] Send 20-30 concurrent requests via HTTP/2
- [ ] Verify multi-success (multiple 200s where logically single)
- [ ] Quantify financial / privilege impact
- [ ] Don't run thousands of races in production
