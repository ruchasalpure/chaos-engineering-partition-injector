# Duties and Responsibilities for Chaos Engineering Partition Injector Agent

## Dual-Control Architecture
Maker:
partition-generator

Checker:
recovery-sla-checker

## Operational Workflow
1. The Maker (partition-generator) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (recovery-sla-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
