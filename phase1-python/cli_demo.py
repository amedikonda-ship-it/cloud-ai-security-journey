import argparse

parser = argparse.ArgumentParser(description="Demo script showing argparse")
parser.add_argument("--region", default="us-east-1", help="AWS region to check")
parser.add_argument("--verbose", action="store_true", help="Show detailed output")

args = parser.parse_args()

print(f"Checking region: {args.region}")
if args.verbose:
    print("Verbose mode is ON - would show extra details here")
else:
    print("Verbose mode is OFF")
