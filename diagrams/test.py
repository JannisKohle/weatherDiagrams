import json

with open("../data/example.json", "r+") as f:
    content = json.load(f)

print(content)
