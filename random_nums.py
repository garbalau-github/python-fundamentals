import random
import secrets

# Psuedo-random numbers (bad for security)
a = random.random()
print(a)  # 0.5723292133191319

# Random choice from a list (bad for security)
list = ["A", "B", "C", "D", "E", "F", "G"]
choice = random.choice(list)
print(choice)

# Random with 'secrets' (tokens, auth, passwords)
token_one = secrets.randbelow(10)
# 4 random binary values, 1111 is max (15)
token_two = secrets.randbits(4)
print(token_one)
print(token_two)
