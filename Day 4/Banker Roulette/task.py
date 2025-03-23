import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
randint = random.randint(0,len(friends)-1)

print(friends[randint])

# Another option
print(random.choice(friends))

