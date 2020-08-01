class person:
    name = ""
    surname = ""
    age = ""
    email = ""

    # this metod are the constructor of the class    
    def __init__(self,_name,_surname,_age,_email):
        self.data = []
        self.name = _name
        self.surname = _surname
        self.age = _age
        self.email = _email

    def print_age(self):
        return f"Name: {self.name} Email:{self.email} Age: {self.age}"

per = person("Carlos","Medina","40","mail")

print(per.print_age())