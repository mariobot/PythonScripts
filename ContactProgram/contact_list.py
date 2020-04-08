class Contact_list:

    list_contacts = []

    def __init__(self):
        pass

    def add_contact(self, person_info):
        self.list_contacts.append(person_info)

    def remove_contect(self, person_info):
        self.list_contacts.remove(person_info)
    
    def count(self):
        return self.list_contacts.count

    def search_contact(self, name):
        pass

    






