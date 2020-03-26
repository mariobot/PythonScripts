# FUNCTIONS  is the core of Python. 

# To define a function use the keyword def

def sum_numbers(x,y):
    return x + y

print(sum_numbers(10,15))

# Default arguments in a function

def get_geo_location(name, country = "Colombia", age = 18):
    message = "{0} Location is: {1} with {2} years old".format(name,country,age)
    return message

print(get_geo_location("Carlos"))
print(get_geo_location("Maria","USA",21))

# Default parameters are mutable and acumulate the values

def calc(a, b = []):
    b.append(a)
    return b

print(calc(1))
print(calc(2))
print(calc(3))

# To prevent the acumulate values you can do it

def calc2(a, b = None):
    if b == None:
        b = []
    b.append(a)
    return b

print(calc2(1))
print(calc2(2))
print(calc2(3))

# Key word arguments
# You can pass the keyword atribute for specify the parameter sended

def vehicle(speed, tires = 4, color = "White"):
    message = "Vehicle speed: {0}, wiht {1}, and {2} color".format(speed,tires,color)
    return message
print(vehicle(180, color="Red"))
print(vehicle(120, tires=8))
print(vehicle(speed=200, color="Black",tires=6))

# Recibe a Dictionary
# **keywords recivie the dictionay
# *arguments 
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# use / to force that the method parameters are passed by position
#pos_only_arg(arg, /)
# use * to force that the method parameters are passed by kyeword
#kwd_only_arg(*, arg):

# Atribute Argument List
# You can pass an list of arguments to one fild
def concat(*args, delimiter="-"):
    message = str(delimiter).join(args)
    return message

print(concat("ROOT","USER","FOLDER","EXTENSION", delimiter="/"))
print(concat("COLOMBIA","CUNDINAMARCA","BOGOTA","CHAPINERO"))

# List can be delivered with *
h_fields = [5,55]
print(list(range(*h_fields)))

# Dictionaries can be delivered with the keyword **

my_info = {"age":18,"name":"Carlos","address":"ST 244"}

def showInfo(age,name,address):
    message = "{0} {1} {2}".format(name,age,address)
    return message

print(showInfo(**my_info))

# To decorete a function with description use

def calculate_area(base, width, hight):
    """ Use this method to calculete the area ^2 
    You need to gife the base, width and hight
    """
    return base * width * hight

print(calculate_area.__doc__)
print(calculate_area(10,20,50))

