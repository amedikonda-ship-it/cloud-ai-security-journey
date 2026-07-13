import boto3

# boto3 automatically uses CloudShell's credentials - no keys needed in code
ec2 = boto3.client('ec2', region_name='us-east-1')

def list_all_instances():
    response = ec2.describe_instances()
    
    print(f"{'Instance ID':<22} {'State':<12} {'Type':<12} {'Name'}")
    print("-" * 60)
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            instance_type = instance['InstanceType']
            
            # Tags are a list of dicts - need to find the 'Name' tag specifically
            name = "No Name"
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    name = tag['Value']
            
            print(f"{instance_id:<22} {state:<12} {instance_type:<12} {name}")

list_all_instances()
