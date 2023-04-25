# Lists: ordered, mutable, allows duplicate elements
list = ["banana", "cherry", "apple", "apple", 42, True]

# Accessing elements
list[0] = "pear"
print(list[0])
print(list[-1])
print(len(list))

# Check
if "banana" in list:
    print("Yes, 'banana' is in the list")
else:
    print("No, 'banana' is not in the list")

# Looping
for i in list:
    print(i)

# Methods
list.append("lemon")
list.insert(1, "blueberry")
removed_item = list.pop()
list.remove("apple")

print(list)
