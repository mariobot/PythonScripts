import contact_list as contacts
import person_info as person
import location as loc
import office as offi

p1 = person.Person_info("Mario","Botero",46521325)
p2 = person.Person_info("Carlos","Medina",4556652)

contactsLib = contacts.Contact_list()

contactsLib.add_contact(p1)
contactsLib.add_contact(p2)

location_p1 = loc.location("60","50","av 23 34 22",18006)
location_p2 = loc.location("55","52","st 54 55 2",13006)

for contact in contactsLib.list_contacts:
    print("Name: "+ contact.name + " Surname: " + contact.surname + " Phone: " + str(contact.phone))

office1 = offi.Office("501","2","5087","789987")
#print(office1.floor)