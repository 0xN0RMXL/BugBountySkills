# GraphQL — Introspection Enabled

## 📌 What It Is
Production GraphQL endpoint allows introspection query, leaking entire schema (types, queries, mutations, args).

## 🔍 How to Find It
POST `{__schema{types{name,fields{name,type{name}}}}}` to `/graphql`.

## 🧪 How to Test It
Run full introspection query → dump schema → discover hidden mutations / queries.

## 💣 How to Exploit It
Hidden admin mutations, deletion ops, batched queries → access control bugs.

## 🔄 Bypass Techniques
If introspection disabled → clairvoyance to recover via error messages.

## 🛠️ Tools
- graphql-voyager (visual)\n- inql (Burp)\n- clairvoyance\n- graphql-cop\n- altair, GraphQL Playground

## 🎯 Payloads
See SKILL_FILES/VULNERABILITIES/API/graphql_introspection_attacks.md

## 📝 Real-World Examples
HackerOne, Shopify, GitHub all had GraphQL bugs.

## 🚩 Common Mistakes / Traps
Introspection enabled isn't the bug — it's a starting point. Find auth/authz issues in revealed mutations.

## 📊 Severity & Impact
Low alone; Critical when chained with revealed admin mutations.

## 🔗 References
GraphQL spec, PortSwigger GraphQL labs.

## ⚡ One-Liners
```bash\ncurl -X POST 'https://target/graphql' -H 'Content-Type: application/json' -d '{"query":"{__schema{types{name}}}"}'\n```
