import boto3
import json
import secrets
import string
from datetime import datetime, timezone

def generate_secure_password(length=16):
    """Generate a cryptographically secure random password."""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def create_or_get_secret(client, secret_name):
    """Create a secret if it doesn't exist, otherwise return its ARN."""
    try:
        initial_value = {
            "username": "app_db_user",
            "password": generate_secure_password(),
            "last_rotated": datetime.now(timezone.utc).isoformat()
        }
        response = client.create_secret(
            Name=secret_name,
            SecretString=json.dumps(initial_value)
        )
        print(f"Created new secret: {secret_name}")
        return response['ARN']
    except client.exceptions.ResourceExistsException:
        print(f"Secret already exists: {secret_name}")
        response = client.describe_secret(SecretId=secret_name)
        return response['ARN']

def rotate_secret(client, secret_name):
    """Simulate rotating a secret's password."""
    current = client.get_secret_value(SecretId=secret_name)
    current_data = json.loads(current['SecretString'])

    print(f"Current password (first 4 chars): {current_data['password'][:4]}****")

    new_data = {
        "username": current_data["username"],
        "password": generate_secure_password(),
        "last_rotated": datetime.now(timezone.utc).isoformat()
    }

    client.put_secret_value(
        SecretId=secret_name,
        SecretString=json.dumps(new_data)
    )

    print(f"New password (first 4 chars): {new_data['password'][:4]}****")
    print(f"Rotated at: {new_data['last_rotated']}")

if __name__ == "__main__":
    secret_name = "phase1-demo-db-credentials"
    client = boto3.client('secretsmanager', region_name='us-east-1')

    create_or_get_secret(client, secret_name)
    print("\n--- Simulating rotation ---")
    rotate_secret(client, secret_name)
