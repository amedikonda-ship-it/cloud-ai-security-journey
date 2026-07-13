import boto3
import json
import argparse
from datetime import datetime, timezone

def generate_iam_report(region):
    iam = boto3.client('iam')
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "users": []
    }

    try:
        users = iam.list_users()['Users']
    except Exception as e:
        print(f"Error fetching users: {e}")
        return

    for user in users:
        username = user['UserName']
        user_info = {
            "username": username,
            "created": user['CreateDate'].isoformat(),
            "has_console_password": False,
            "mfa_enabled": False,
            "attached_policies": []
        }

        # Check for console password (login profile)
        try:
            iam.get_login_profile(UserName=username)
            user_info["has_console_password"] = True
        except iam.exceptions.NoSuchEntityException:
            user_info["has_console_password"] = False

        # Check MFA devices
        mfa_devices = iam.list_mfa_devices(UserName=username)['MFADevices']
        user_info["mfa_enabled"] = len(mfa_devices) > 0

        # Check attached policies
        policies = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
        user_info["attached_policies"] = [p['PolicyName'] for p in policies]

        report["users"].append(user_info)

    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an IAM security report")
    parser.add_argument("--region", default="us-east-1")
    parser.add_argument("--output", default="iam_report.json", help="Output file name")
    args = parser.parse_args()

    report = generate_iam_report(args.region)

    if report:
        with open(args.output, "w") as f:
            json.dump(report, f, indent=2)
        print(f"Report saved to {args.output}")

        # Quick security summary printed to screen
        print("\n--- Security Summary ---")
        for user in report["users"]:
            flags = []
            if not user["mfa_enabled"]:
                flags.append("NO MFA")
            if user["has_console_password"] and not user["mfa_enabled"]:
                flags.append("CONSOLE ACCESS WITHOUT MFA - HIGH RISK")
            status = ", ".join(flags) if flags else "OK"
            print(f"{user['username']}: {status}")
