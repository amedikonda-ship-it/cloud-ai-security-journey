# Phase 2: IAM Deep Dive

## Concepts covered
- Policy structure: Version, Statement, Effect, Action, Resource
- Implicit deny by default; explicit deny always wins
- Least privilege: scoping Action + Resource narrowly
- Users vs Roles: roles = temporary, auto-rotating credentials, no stored secrets
- Trust policy (who can assume a role) vs Permission policy (what the role can do)
- Trust policy = exactly one per role, built-in (AssumeRolePolicyDocument)
- Permission policies = zero-or-more, attached separately, reusable across users/roles
- Instance profiles: EC2-specific wrapper required to attach a role to an instance (other services attach roles directly)
- IMDSv2: token-based metadata access, mitigates SSRF credential theft

## Hands-on work
- Wrote custom least-privilege policy (Phase2-EC2-StartStop-Only)
- Created test user, proved explicit allow + implicit deny via real UnauthorizedOperation error
- Created IAM role + trust policy + instance profile, attached to EC2
- Proved role-based auth via `aws s3 ls` with zero stored credentials
- Inspected actual temporary credentials via IMDSv2 metadata endpoint
- Cleaned up all test resources (user, role, instance profile) after verification
