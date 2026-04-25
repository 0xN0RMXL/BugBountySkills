# Checklist: Cache Poisoning
- [ ] Identify cached endpoints (Cache-Control: public, X-Cache: HIT, CF-Cache-Status: HIT)
- [ ] Use Param Miner to find unkeyed inputs
- [ ] Test X-Forwarded-Host, X-Forwarded-Scheme, X-Original-URL, X-Host, Forwarded
- [ ] Inject XSS / redirect via unkeyed header
- [ ] Confirm next clean request gets poisoned response
- [ ] Use cache-buster (`?cb=<random>`) during testing — don't poison real users
