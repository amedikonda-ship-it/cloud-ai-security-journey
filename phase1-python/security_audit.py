import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

def find_unused_security_groups():
    all_sgs = ec2.describe_security_groups()['SecurityGroups']
    
    # Get security groups actually attached to instances
    instances = ec2.describe_instances()
    used_sg_ids = set()
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            for sg in instance.get('SecurityGroups', []):
                used_sg_ids.add(sg['GroupId'])
    
    print("Security Group Audit")
    print("-" * 50)
    
    for sg in all_sgs:
        sg_id = sg['GroupId']
        sg_name = sg['GroupName']
        
        if sg_id in used_sg_ids:
            print(f"✓ {sg_id} ({sg_name}) - IN USE")
        else:
            print(f"⚠ {sg_id} ({sg_name}) - UNUSED, consider deleting")

find_unused_security_groups()
