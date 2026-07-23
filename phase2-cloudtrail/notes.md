# Phase 2: CloudTrail - Centralized Organization Logging

## What was built
- S3 bucket: phase2-cloudtrail-logs-473649005897
- Organization trail: Phase2-Organization-Trail (multi-region, org-wide)
- Enabled CloudTrail as trusted Organizations service

## Key concepts
- CloudTrail logs EVERY API call by default (90-day Event History, free, always on)
- A Trail = persistent, S3-stored, configurable version of that log
- Organization trails require the AWS Organizations management account,
  explicit service-access trust (enable-aws-service-access), and
  a bucket policy covering BOTH the management account's own path
  AND the org-wide path (/AWSLogs/<account-id>/* AND /AWSLogs/<org-id>/*)
- Multi-region trail is essential - a single-region trail creates blind spots
  for activity in any other region

## Real troubleshooting encountered
- InsufficientS3BucketPolicyException: bucket policy needs 3 statements
  (GetBucketAcl, account-path PutObject, org-path PutObject), not 2 -
  discovered by checking official AWS docs rather than guessing
- CloudTrailAccessNotEnabledException: Organizations requires explicit
  trusted-service enablement per service before that service can act
  org-wide (enable-aws-service-access)
