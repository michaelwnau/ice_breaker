import json

invalid_json = "{'key': 'value'}"  # All your original JSON here.
valid_json = invalid_json.replace("'", '"')

try:
    data = json.loads(valid_json)
    print("This is valid JSON.")
except json.JSONDecodeError:
    print("This is invalid JSON.")


# Note that this function is only replacing single quotes with double quotes at present.
