# Phase 2: VPC Design (In Progress)

## Resources created
- VPC: vpc-0c79de1eb8cc396fb (10.0.0.0/16), tag: Phase2-Custom-VPC
- Public subnet: subnet-0b3b038265e3a0db4 (10.0.1.0/24, us-east-1a)
- Private subnet: subnet-01a7cfcef1efad8cd (10.0.2.0/24, us-east-1a)
- Internet Gateway: igw-090d6a7c9914ce220 (attached to VPC)
- Public route table: rtb-0a00e9a42b41899d8 (0.0.0.0/0 -> IGW), associated
  with public subnet

## Status: INCOMPLETE
- Private subnet still using default/main route table (no NAT Gateway route yet)
- NAT Gateway creation was STARTED then stopped mid-session due to billing
  concerns (Free Plan credit found to be expired as of 2026-07-22)
- Elastic IP that was allocated for NAT Gateway has been RELEASED - no
  NAT Gateway currently exists

## Key concepts learned
- Route tables control routing per-subnet via explicit association, not
  automatically inherited from the VPC-level Internet Gateway attachment
- A VPC can have multiple route tables; only subnets explicitly associated
  with a table use its rules (default: main route table, local traffic only)
- Real-world multi-route-table scenarios: different outbound paths per tier
  (IGW vs NAT vs on-prem VPN), per-AZ NAT Gateway isolation, traffic
  inspection requirements for specific subnets
- NAT Gateway = outbound-only internet access for private subnets;
  never provides a path for internet-initiated inbound connections

## TODO next session
- Decide on NAT Gateway (real, small ongoing cost) vs conceptual-only
- Add private subnet route table + NAT Gateway route
- Consider adding a third (database) subnet with zero internet route,
  completing a realistic 3-tier design
