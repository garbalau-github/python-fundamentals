import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "titles": ["engineer", "programmer"]
}

# Convert into JSON
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)
