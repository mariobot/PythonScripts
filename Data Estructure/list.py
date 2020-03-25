#to define a list use []

my_list = [2010,2011,2012,2013]

print(my_list)

#add item ot last order

my_list.append(2014)

# you can count similar items in the list
print(my_list.count(2012))

# get the index of the object
print(my_list.index(2013))

# reverse the items
print(my_list.reverse())

# las item to analize
print(my_list.pop())

vocals = ["a","e","i","o","u"]
print(vocals)

abc = "abcdefghijklmnñopqrstwxyz"

for letter in abc:
    print(str(letter).upper())

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for k, v in enumerate(knights):
    print("Key: {0} Value: {1}".format(k,v))

my_list2 = ["Mario",37,3.0,"Famous"]

print(my_list2*2)
