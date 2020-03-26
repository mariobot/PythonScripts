#the conditionals in Python are be implemented for the next rules. 

# ------ IF STAMENT --------------

num = 15
state = False

if state == False:
    print(state)
else:
    print(state)

if num < 10:
    print("Less 10")
elif num > 10 and num < 20:
    print("Mayor than 10 and Menor than 20")

# -------- FORM STAMENT ----------------

my_list = ["Carlos","Andres","Rocio"]

for p in my_list:
    print(p)

# FOR WITH ENUMERATER
for k,v in enumerate(my_list):
    print(k,v)

# RANGE FUNCTION
for item in range(10):
    print(item)

for item in range(50,60):
    print(item)

for item in range(-100,200,50):
    print(item)

# break and continue

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# PASS Statement
# User pass when do you pass a function, for example when do you not implementing a functionality but wanth to have defined the name

def add_numbers(items):
    pass




    





