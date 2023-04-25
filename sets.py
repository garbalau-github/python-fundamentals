# Sets: unordered, mutable, no duplicates
set = {"a", "b", "c"}

# Modify elements
set.add("d")
set.add("e")
set.remove("a")

# Check
if ("b" in set):
    print("b is in set")

# Looping
for item in set:
    print(item)

# Union and Intersection
odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(even)
intersection = even.intersection(primes)

print(union)
print(intersection)

# Differences
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)
