import json

filepath = "revit_sample_model.hbjson"

# Load the JSON file
with open(filepath, 'r') as f:
    hb_json = json.load(f)  # Changed loads() to load() for file reading

# Save the JSON file
with open(filepath, 'w') as f:
    json.dump(hb_json, f, indent=4) 