# Strings: ordered, immutable, text representation
string = "I'm learning Python"

# Accesing
char = string[0]
length = len(string)
word = string[13:]
print(word)

# Format strings (%s, %d, %f)
person = "Tom"
string_one = "The variable is %s" % person
string_two = "The variable is " + person
string_three = f"The variable is {person}"

# The variable is Tom x3
print(string_one)
print(string_two)
print(string_three)
