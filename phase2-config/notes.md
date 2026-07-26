# Phase 2: AWS Config - Continuous Compliance Monitoring

## What was built
- S3 bucket: phase2-config-logs-473649005897 (Config snapshot storage)
- IAM role: Phase2-Config-Role (trust: config.amazonaws.com, permissions: AWS_ConfigRole managed policy)
- Configuration Recorder: Phase2-Recorder (allSupported, includeGlobalResourceTypes)
- Delivery Channel: Phase2-DeliveryChannel
- Config Rule: s3-bucket-public-access-prohibited (AWS managed rule)

## Key concepts
- CloudTrail = what happened (events). Config = what things look like right now,
  and whether that's compliant (continuous state + rules).
- AWS_ConfigRole is read-only (Get/List/Describe across many services) - Config
  can inspect everything but modify nothing via this role.
- Config's ability to WRITE to S3 comes entirely from the bucket's resource-based
  policy, not from the role - two separate, independently-scoped grants.
- Identity-based policy (role/user) vs resource-based policy (bucket):
  - Identity-based: Principal is implied by what it's attached to; trust policy
    (one-time, defines who can assume) + permission policy (repeatable) are separate
  - Resource-based: Principal is explicit inside the document itself; one document,
    no separate assume step, used for AWS services acting on your behalf or
    cross-account access
- Config Rules continuously re-evaluate - not a one-time scan

## Verified hands-on
- Confirmed real buckets (CloudTrail/Config log buckets) as COMPLIANT
- Deliberately created a public S3 bucket, confirmed Config correctly flagged it
  NON_COMPLIANT with accurate annotation ("bucket policy allows public read access")
- Cleaned up the test bucket immediately after proving detection
