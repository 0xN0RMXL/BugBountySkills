# SKILL: Azure Cloud Misconfiguration
## Version: 1.0 | Domain: infra

---

## TOP FINDINGS
### Public blob storage
```bash
curl "https://ACCOUNT.blob.core.windows.net/CONTAINER?restype=container&comp=list"
```

### Azure AD tenant enumeration
```bash
curl https://login.microsoftonline.com/target.com/.well-known/openid-configuration
# Reveals tenant ID
```

### Exposed Azure Functions
```bash
curl https://FUNCAPP.azurewebsites.net/api/FUNCTION?code=
# If no auth → unauth function execution
```

### Storage SAS token miscconfig
```bash
# SAS token with too broad permissions / long expiry
curl "https://ACCOUNT.blob.core.windows.net/container/file?sv=2020-08-04&ss=bfqt&srt=sco&sp=rwdlacuptfx&se=2030-01-01&sig=AAAA"
```

## TOOLS
- MicroBurst (PS), ROADtools, scoutsuite, azurehound

## REFERENCES
Azure Security Benchmark
