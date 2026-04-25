# SKILL: Impact Statement Writing
## Version: 1.0 | Domain: reporting

---

## FORMULA
> [Attacker pre-state] can [verb] [resource] [optionally: at scale] without [precondition], leading to [business impact: data leak / ATO / fraud / availability loss / compliance].

## EXAMPLES — by class

### XSS (stored, admin-visible)
> Any unauthenticated visitor can persist a JavaScript payload in the support ticket body that executes when staff opens the ticket in the admin dashboard. This grants the attacker the staff member's session and full admin access to the SaaS tenant, allowing them to read/modify all customer data, billing records, and configuration.

### IDOR
> Any logged-in user (free tier sufficient) can read invoices belonging to any other customer by changing a single integer in the URL. This exposes PII for all 1.2M customers including full name, billing address, line items, and total spend, violating GDPR Art. 32 and PCI-DSS Req. 7.

### SSRF → cloud
> An unauthenticated attacker can coerce the server to make HTTP requests to arbitrary URLs, including `http://169.254.169.254`, returning the EC2 instance's IAM credentials. With those credentials they can [enumerate / read / modify / delete] any S3 bucket, RDS instance, and EC2 resource owned by the AWS account.

### Auth bypass
> An attacker can authenticate as any user (including admin) without knowing the password by sending a single crafted request. There is no rate limiting and the request leaves no anomalous log entry that the customer's monitoring would detect.

### Subdomain takeover (cookie scope)
> The wildcard cookie `Domain=.target.tld` is sent to any subdomain. The dangling DNS record for `forgotten.target.tld` allows an attacker to register the corresponding service (e.g., NXDOMAIN'd S3 bucket) and capture the session cookies of any user who visits an attacker-controlled link to that subdomain, leading to ATO.

### Race condition (gift card / coupon)
> A logged-in user can redeem a single $50 gift card N times concurrently, receiving N×$50 of credit. PoC redeems the same gift card 30 times in <1s with a single HTTP/2 connection.

## DON'T
- "Could potentially..."
- "An attacker may be able to..."
- "Theoretically..."

## DO
- "An attacker [does X] [to achieve Y]"
- Quantify (number of users, dollar value, regulatory citation)
- Cite specific endpoint, role, request body

## REFERENCES
HackerOne disclosed reports, OWASP Risk Rating
