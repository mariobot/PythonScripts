# reference documentation https://docs.python.org/3/tutorial/classes.html
# To define a class use class !obius

class website:
    subdomain = "www"

    # this metod are the constructor of the class    
    def __init__(self):
        self.data = []

    def define_domain(self, name):
        return f"CONFIG DOMAIN {self.subdomain}.{name}.com"

web = website()
print(web.subdomain)
print(web.define_domain("pepsi"))

class page:

    # use this constructur to inizialice the clas with the parameterst that you wanth
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def show_parameter1(self):
        return self.param1

p = page("Fernando","Entrenador")
print(p.show_parameter1())
    
# class and instance variables

class vehicle:

    brand = "Mazda"

    def __init__(self, name):
        self.name = name

cls1 = vehicle("Miata")
print(cls1.brand)
print(cls1.name)
cls2 = vehicle("121")
print(cls2.brand)
print(cls2.name)

# its posible to define a methods in a class that wass writen outside of the class

def sum(x,y):
    return x+y

class Operation:
    sum_method = sum

result_sum = Operation.sum_method(200,199)
print(result_sum)

# the methods in a class can call another methods with the self refence 

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

# To use inheritance send at the deninition name the class that inheritance
#class Name(Address)
#class Name(Address,Location,Estate) # for multiple inheritance

# To define a private variavle use __ to the private variable

class Location:    

    def you_are(self):
        self.__location = "Colombia"
        text = "Your Country is: " + self.__location 
        return text

loc = Location()
print(loc.you_are())





