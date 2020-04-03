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
    



