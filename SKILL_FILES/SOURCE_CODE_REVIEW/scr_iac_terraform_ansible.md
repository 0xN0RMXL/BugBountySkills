# SKILL: Infrastructure-as-Code Review (Terraform / Ansible / CloudFormation)
## Version: 1.0 | Domain: scr (iac)

---

## TERRAFORM
```bash
# Static analysis
tfsec .
checkov -d .
terrascan scan -i terraform
trivy config .

# Common findings
- S3 bucket with public ACL
- Security group 0.0.0.0/0 on SSH/RDP
- IAM policies with "*" actions or resources
- Unencrypted RDS / EBS / S3
- Missing CloudTrail / VPC Flow Logs
- Public RDS endpoint
- Lambda with VPC, but no encryption
```

## ANSIBLE
```bash
ansible-lint playbook.yml
- become: yes without explicit reason
- shell vs command (shell allows injection)
- no_log: false on tasks with secrets
- module: shell with j2 template containing user input
```

## CLOUDFORMATION
```bash
cfn-lint template.yaml
cfn-nag scan -i template.yaml
- Resources with PublicAccess
- IAM Policies with wildcards
- Missing encryption
```

## SEMGREP
```bash
semgrep --config=p/terraform .
semgrep --config=p/cloudformation .
```

## REFERENCES
tfsec, checkov, OPA/Conftest
