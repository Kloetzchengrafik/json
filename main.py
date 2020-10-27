import json

with open("test.json", "r") as file:
    db = json.load(file)

template = {
    "name": "Lisa",
    "geldstand": 10
}

db["test"].append(template)
with open("test.json", "w") as file:
    json.dump(db, file, indent=4)


found = None
i = 0
for var in db["test"]:
    if var["name"] == "Tom":
        found = i
    i += 1
if found or found == 0:
    db["test"].pop(found)
with open("test.json", "w") as file:
    json.dump(db, file, indent=4)