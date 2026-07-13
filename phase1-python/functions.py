def check_compliance(instance_name, has_encryption, has_backup, is_tagged):
    """Returns a list of compliance issues for an EC2 instance."""
    issues = []
    
    if not has_encryption:
        issues.append("Missing encryption")
    if not has_backup:
        issues.append("No backup configured")
    if not is_tagged:
        issues.append("Missing required tags")
    
    if len(issues) == 0:
        return f"{instance_name}: COMPLIANT"
    else:
        return f"{instance_name}: NON-COMPLIANT - {', '.join(issues)}"

# Test with different scenarios
print(check_compliance("web-server-1", True, True, True))
print(check_compliance("web-server-2", False, True, True))
print(check_compliance("db-server-1", False, False, False))

# Loop through a list of instances
instances = ["web-server-1", "web-server-2", "db-server-1"]
for instance in instances:
    print(f"Checking {instance}...")
