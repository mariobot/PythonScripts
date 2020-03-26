# a dictionary its defined with {}
# have a key and value

my_dictionary = {"Mario":300664585,"Carlos":456655215,"Sandra":45566554,"Camila":45662215,"Maria":455566554}

print(my_dictionary)

# fro get a value node
print(my_dictionary["Mario"])

# to asign a new value
my_dictionary["Mario"] = 315464646
print(my_dictionary["Mario"])

# to remove a node
print(my_dictionary)
del my_dictionary["Sandra"]
print(my_dictionary)

m_v = {"d":2,"a":3,"f":4,"b":5}
print(sorted(m_v))

# Looping in Dictionaries

for f in my_dictionary.items():
    print(f)

for k,v in enumerate(my_dictionary):
    print(k,v)


