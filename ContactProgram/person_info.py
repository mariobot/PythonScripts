class Person_info:

    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def complete_name(self):
        return self.name + " " +self.surname

