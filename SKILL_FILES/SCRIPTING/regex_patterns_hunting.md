# SKILL: Regex Patterns for Hunting
## Version: 1.0 | Domain: scripting

---

## SECRETS
```regex
# AWS
AKIA[0-9A-Z]{16}
ASIA[0-9A-Z]{16}
aws_secret_access_key.{0,30}['"][A-Za-z0-9/+=]{40}['"]

# GitHub
gh[pousr]_[A-Za-z0-9]{36,}
github_pat_[a-zA-Z0-9_]{82}

# Google
AIza[0-9A-Za-z_-]{35}
ya29\.[0-9A-Za-z_-]+

# Slack
xox[baprs]-[0-9a-zA-Z-]+

# Stripe
sk_live_[0-9a-zA-Z]{24,}
rk_live_[0-9a-zA-Z]{24,}

# Twilio
SK[0-9a-fA-F]{32}
AC[0-9a-fA-F]{32}

# SendGrid
SG\.[A-Za-z0-9_-]{22}\.[A-Za-z0-9_-]{43}

# Mailgun
key-[0-9a-zA-Z]{32}

# Square
sq0atp-[0-9A-Za-z_-]{22}
sq0csp-[0-9A-Za-z_-]{43}

# JWT
eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+

# Private key
-----BEGIN ((RSA|DSA|EC|OPENSSH|PRIVATE) )?PRIVATE KEY-----
```

## ENDPOINTS IN JS
```regex
# URL paths
['"]\/[a-zA-Z0-9_/.-]{2,}['"]
# API patterns
['"]\/api\/v?\d+\/[a-zA-Z0-9_/.-]+['"]
# GraphQL
['"]\/graphql['"]
# Tokens in URLs
[?&](?:token|api_key|apikey|access_token|key)=([^&\s'"]+)
```

## EMAILS / DOMAINS
```regex
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}
```

## DANGEROUS SINKS (JS)
```regex
\b(eval|Function|setTimeout|setInterval)\s*\(
\.(innerHTML|outerHTML|insertAdjacentHTML)\s*=
document\.(write|writeln)\s*\(
location(\.href)?\s*=
```

## USAGE
```bash
# Apply via grep / rg
rg -nE 'AKIA[0-9A-Z]{16}' .
# Combine many at once
cat patterns.txt | xargs -I{} rg -nE '{}' .
# In curl pipeline
curl -sk $URL | grep -oE 'AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36}'
```

## REFERENCES
gitleaks rules, trufflehog detectors
