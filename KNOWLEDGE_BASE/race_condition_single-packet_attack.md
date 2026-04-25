# Race Condition — single-packet attack

## 📌 What It Is
Server processes concurrent requests in parallel; state-checks not atomic. Multiple requests succeed where one should.

## 🔍 How to Find It
Find state-changing endpoint with check (e.g., redeem coupon, withdraw funds, accept invitation). Try sending N concurrent.

## 🧪 How to Test It
1. Use Burp Turbo Intruder `race-single-packet-attack.py`.\n2. Or Python httpx HTTP/2 with `asyncio.gather`.\n3. 20-30 concurrent requests via single TCP.\n4. If multiple 200s where logically only one expected → race confirmed.

## 💣 How to Exploit It
Redeem $50 gift card 30 times → $1500 credit. Accept invitation → invite + admin role twice.

## 🔄 Bypass Techniques
If JS framework rate-limits client-side → use direct API. If IP-based → use multiple X-Forwarded-For (if accepted).

## 🛠️ Tools
- Burp Turbo Intruder\n- httpx async (Python)\n- racepwn

## 🎯 Payloads
Single-packet attack via HTTP/2: 20-30 requests in 1 TCP packet → ~1ms apart.

## 📝 Real-World Examples
James Kettle's research at PortSwigger, HackerOne race reports (Shopify, Slack).

## 🚩 Common Mistakes / Traps
Don't run thousands of races on production — drains program treasury. Stop at smallest reliable PoC.

## 📊 Severity & Impact
Critical for monetary impact; High for privilege escalation.

## 🔗 References
PortSwigger Race Conditions Labs (James Kettle 2023).

## ⚡ One-Liners
```python\nasyncio.gather(*[client.post(url, json={'code':'X'}) for _ in range(30)])\n```
