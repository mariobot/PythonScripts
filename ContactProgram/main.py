import contact_list as contacts
import person_info as person

p1 = person.Person_info("Mario","Botero",46521325)
p2 = person.Person_info("Carlos","Medina",4556652)

contactsLib = contacts.Contact_list()

contactsLib.add_contact(p1)
contactsLib.add_contact(p2)

#print("You have: contacts.")

for contact in contactsLib.list_contacts:
    print("Name: "+ contact.name + " Surname: " + contact.surname + " Phone: " + str(contact.phone))




