# Phase 2: Security Hub - Centralized Security Findings

## What was built
- Enabled Security Hub in us-east-1
- Auto-enabled standards: CIS AWS Foundations Benchmark v1.2.0,
  AWS Foundational Security Best Practices v1.0.0
- Confirmed automatic integration with GuardDuty, Config, Access Analyzer,
  Inspector, Macie, Firewall Manager, and other AWS-native services -
  no manual connection required within the same account

## Key concepts
- Security Hub does not detect anything itself - it AGGREGATES findings from
  other services (GuardDuty = threats, Config = compliance rules, Inspector =
  vulnerability scanning, etc.) into one unified view
- Also runs its own standards-based checks (CIS, AWS Foundational Best Practices)
  independently, in addition to aggregating
- This is the direct mechanism for the capstone's "centralize security findings"
  requirement - single pane of glass across multiple detection/compliance sources
- Initial standards evaluation is NOT instant - can take 30+ minutes to a few
  hours for first full pass, unlike Config (~minutes) or GuardDuty sample
  findings (~seconds).

## Status at time of session
- Standards subscriptions created, status PENDING as of session end
- Findings API returned empty - expected given pending evaluation state
- To verify later: aws securityhub get-findings --max-results 10
