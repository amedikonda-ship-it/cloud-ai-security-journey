# Phase 2: VPC Design

## Resources created
- VPC: vpc-0c79de1eb8cc396fb (10.0.0.0/16), tag: Phase2-Custom-VPC
- Public subnet: subnet-0b3b038265e3a0db4 (10.0.1.0/24, us-east-1a)
- Private subnet: subnet-01a7cfcef1efad8cd (10.0.2.0/24, us-east-1a)
- Internet Gateway: igw-090d6a7c9914ce220 (attached to VPC)
- Public route table: rtb-0a00e9a42b41899d8 (0.0.0.0/0 -> IGW), associated
  with public subnet
- Private route table: rtb-0e5f13c9dc49a9ca2 (0.0.0.0/0 -> NAT Gateway),
  associated with private subnet
- NAT Gateway: created, tested via route configuration, then DELETED after
  verification to stop ongoing cost (~$0.045/hr). Associated Elastic IP
  released. Standing infrastructure (VPC/subnets/route tables/IGW) costs
  nothing while idle - only NAT Gateway/EIP/running instances cost money.

## Status: Core two-tier design COMPLETE
- Public subnet: bidirectional internet access via IGW
- Private subnet: outbound-only internet access via NAT Gateway (route
  configured and verified; NAT Gateway itself deleted post-verification
  to avoid ongoing charges - live traffic test skipped, config-level
  verification only)

## Key concepts learned
- Route tables control routing per-subnet via explicit association, not
  automatically inherited from VPC-level Internet Gateway attachment
- A VPC can have multiple route tables; only subnets explicitly associated
  with a table use its rules
- Public vs private subnet distinction = which route table it's associated
  with (IGW target vs NAT Gateway target vs no internet route at all),
  not any inherent subnet property
- NAT Gateway = outbound-only for private subnets; never provides inbound path
- Real-world multi-route-table scenarios: different outbound paths per tier
  (IGW vs NAT vs on-prem VPN), per-AZ NAT Gateway isolation, traffic
  inspection requirements for specific subnets

## Not yet covered
- Third (database) tier subnet with zero internet route
- Network ACLs (subnet-level stateless firewall)
- Multi-AZ redundancy (currently single-AZ: us-east-1a only)lling
ol routing per-subnet via explicit association, not
level Internet Gateway attachment
ateway (real, small ongoing cost) vs conceptual-only
way route
