import random
import my_module

print(my_module.my_favorite_number)

#random_int = random.randint(1,10)
#print(random_int)

#random_number = random.random() * 10 # 0 to 1; can multiply by 10^x
#print(random_number)

#random_float = random.uniform(1,10)
#print(random_float)

num = random.randint(0,1)

if num == 1:
    print("Heads")
else:
    print("Tails")