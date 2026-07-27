# Phase 2: GuardDuty - Threat Detection

## What was built
- Enabled GuardDuty detector (cecfd0cfe6409371c64f79b43ba332b7)
- Generated and reviewed sample findings to learn finding structure

## Key concepts
- Config = "is my configuration correct" (static, rules-based, compliance)
- GuardDuty = "is something malicious happening right now" (ML/threat-intel based,
  continuously analyzes CloudTrail, VPC flow logs, DNS logs)
- Severity scoring: Low (1-3.9), Medium (4-6.9), High (7-8.9) - drives triage priority
- GuardDuty + CloudTrail + Config work together: GuardDuty flags something worth
  investigating, CloudTrail gives the forensic trail, Config shows what changed
- Archiving a finding = internal status flag (reviewed/resolved), not deletion or
  external storage - findings remain retrievable by ID, just excluded from default
  list-findings results

## Verified hands-on
- Reviewed a sample UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B finding
  (severity 5.0 / Medium) - simulated "impossible travel" login pattern
- Checked finding severity via CLI query
- Archived findings after review
