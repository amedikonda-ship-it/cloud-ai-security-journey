import json

# Python dict -> JSON string (for saving/sending data)
architect_data = {
    "name": "AB",
    "phase": 1,
    "skills": ["Linux", "AWS", "Python"]
}

json_string = json.dumps(architect_data, indent=2)
print(json_string)

# JSON string -> Python dict (for reading data, e.g. from an API response)
raw_json = '{"instance_id": "i-123", "state": "running"}'
parsed = json.loads(raw_json)
print(parsed["state"])

# Save to an actual file
with open("data.json", "w") as f:
    json.dump(architect_data, f, indent=2)

print("Saved to data.json")
