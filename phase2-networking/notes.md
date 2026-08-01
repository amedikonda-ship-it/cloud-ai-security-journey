# Phase 2: PrivateLink & Transit Gateway

## PrivateLink
- Created Interface VPC Endpoint for Secrets Manager (com.amazonaws.us-east-1.secretsmanager)
- Required enabling enableDnsSupport + enableDnsHostnames on the VPC first
  (not on by default for custom VPCs, unlike the default VPC)
- PrivateDnsEnabled: true means the NORMAL AWS service DNS name
  (secretsmanager.us-east-1.amazonaws.com) transparently resolves to the
  private endpoint - zero application code changes needed
- Verified available, then deleted (cost: ~$0.01/hr, small per-GB charge)

## Key concept: PrivateLink scope
- THREE use cases: VPC -> AWS service, VPC -> your own service in a
  different VPC (via Endpoint Service), VPC -> third-party SaaS vendor
- Narrow, service-specific connectivity - NOT general VPC-to-VPC networking

## Transit Gateway (real cross-account setup)
- Created TGW (tgw-0fa2991b8893fae53) in management account
- Attached management VPC (vpc-0c79de1eb8cc396fb)
- Shared TGW with Sandbox account (510473518243) via AWS RAM
  (create-resource-share, principals = target account ID)
- Sandbox account accepted RAM invitation, created own VPC
  (vpc-0476a974f013515d7, CIDR 10.1.0.0/16 - deliberately non-overlapping
  with management VPC's 10.0.0.0/16)
- Sandbox account created attachment (pendingAcceptance since
  AutoAcceptSharedAttachments was disabled)
- Management account explicitly accepted the attachment (dual-approval:
  RAM share acceptance + individual attachment acceptance are separate steps)

## Key concept: TGW = broad VPC-to-VPC connectivity (contrast to PrivateLink's
narrow, service-specific scope)

## Two-layer routing model (important, initially got this wrong)
- VPC route table: "for traffic leaving THIS subnet, where does it go" -
  routes to TGW added HERE, in whichever specific subnet's route table
  actually needs the connectivity (NOT a fixed
