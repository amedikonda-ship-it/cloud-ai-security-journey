# Phase 2: KMS - Key Management Service

## What was built
- Created customer-managed KMS key (870dc11f-1597-4970-b5c8-0bb4495a8b64)
  with alias alias/phase2-learning-key
- Applied a custom key policy separating key administration from key usage

## Key concepts
- Envelope encryption: KMS master key never directly encrypts large data.
  Instead, GenerateDataKey produces a Plaintext data key (used locally,
  immediately, then discarded) + a CiphertextBlob (that data key, encrypted
  by the master key, safe to store alongside the encrypted data)
- aws kms encrypt is a DIRECT encryption call, 4KB limit, no data key involved -
  different from envelope encryption, meant for small values only
- In real-world use, AWS services (S3, EBS, RDS, Secrets Manager) handle
  envelope encryption automatically and invisibly - you just point them at
  a KMS key ID, not call encrypt/decrypt/generateDataKey yourself
- KMS key policies are resource-based policies (like S3 bucket policies) -
  but UNIQUE among AWS resources: KMS defaults to deny-all, even for the
  account owner, unless the key policy explicitly grants access
- Principal "arn:aws:iam::<account>:root" does NOT mean "only root user" -
  it means "delegate to the account's IAM policies," the standard default
- Real pattern: separate key ADMINISTRATION (manage/delete/policy changes)
  from key USAGE (encrypt/decrypt/generateDataKey) via separate statements,
  typically for different principals (admins group vs application role)
- get-key-policy does not accept key aliases, only key ID/ARN (inconsistent
  with most other KMS commands, which do accept aliases)
