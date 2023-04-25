# Dictionaries: key-value pairs, unordered, mutable, no duplicates
dict = {
    "name": "Nick",
    "age": 25,
    "country": "Moldova"
}

# Accessing elements
print(dict)
print(dict["age"])
print(dict.keys())
print(dict.get("age"))

# Loop
for key, value in dict.items():
    print(key, value)

# Merge
dict_two = {
    "email": "nick@gmail.com"
}
dict.update(dict_two)
print(dict)
