# Phase 2: AWS Organizations + SCPs

## Structure built
- Organization ID: o-o5k1w4qki4 (management account: 473649005897)
- Root: r-tgw9
- OUs created: Security, Sandbox, Workloads
- Member account created: Phase2-Sandbox-Account (510473518243), moved into Sandbox OU

## Concepts learned
- SCPs are guardrails at the Organization/OU level - restrict maximum possible permissions, never grant them
- SCPs combine: explicit Deny always wins, regardless of source policy
- Every OU/account has a default FullAWSAccess allow SCP; custom SCPs layer Deny on top
- Trust/access to member accounts: OrganizationAccountAccessRole (auto-created), assumed via sts assume-role
- Environment variables (AWS_ACCESS_KEY_ID etc.) control which identity the CLI acts as
- Management account is exempt from SCPs by design

## Verified hands-on
- Wrote SCP denying ec2:RunInstances except for specific small instance types (Condition + StringNotEquals)
- Attached to Sandbox OU, enabled SERVICE_CONTROL_POLICY at Root level (separate toggle from Org-level enablement)
- Proved denial: m5.large blocked with explicit SCP ARN cited in error
- Proved allow: t3.micro passed dry-run successfully
