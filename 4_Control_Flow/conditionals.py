#to define the diferents conditionals you can use

#IF STATEMENT

age = 30

if age < 18:
    print("you are so young")
elif age >= 18 and age < 40:
    print("you are a productive person")
elif age >= 40 and age < 60:
    print("you are a good worker")
else:
    print("you are a third age person")

#FOR STATEMEN

ages = [18,40,60]

for age in ages:
    print(age)

#FOR USING A RANGE

for number in range(10):
    print(number)

#RANGE can be used
range(5, 10)
#   5, 6, 7, 8, 9

range(0, 10, 3)
#   0, 3, 6, 9

range(-10, -100, -30)
#   -10,-40-70


