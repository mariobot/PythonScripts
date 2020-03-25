# the Tuples are defined with ()

my_tuple = (100,550,5468,99776,4546585)

# Tuples are INMUTABLE
# my_tuple[0] = 11556
# Error set is not valid

# But the object in the Tuples can be mutables

print(my_tuple)

# Looping tuples
for x in my_tuple:
    print(x)

# Lopping tuples enumerates
for k,v in enumerate(my_tuple):
    print("Key: {0} Value: {1}".format(k,v))


