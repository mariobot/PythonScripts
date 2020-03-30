# You can format text with f or F keyword previous of "" characters

year = 2020
month = 3
status = "EN CUARENTENA"

message = f"Es el año {year} con el mes numero {month} el estado actual es {status}"
message2 = f"El cuadrado de 2 es {2*2}"

print(message)
print(message2)

# You can use str.format() with pass the parameters

yes_votes = 45_4
no_votes = 34_4
percentage = yes_votes / (yes_votes + no_votes)
message3 = "{:-9} yes votes {:2.2%}".format(yes_votes,percentage)
print(message3)

table = {"Carlos":3000000,"Maria":1500000,"Fernando":2500000}
message5 = "Carlos = {0[Carlos]:d}, Maria = {0[Maria]:d}, Fernando = {0[Fernando]:d}".format(table) # print a table
print(message5)

# Using the word repr you can print al the context string writed

st1 = "Hi world"
print(st1)
print(repr(st1))

print("The sum values of 5 + 4 is: "+repr(5+4))

# Using str.rjust, str.ljust, and str.center you can justify te content with your prefer filter
st5 = "NAME"
print(st5.rjust(10,"-"))
print(st5.ljust(10,"-"))
print(st5.center(10,"-"))

# Using str.zfill the number values can fill with 0

value22 = "22"
print(value22.zfill(5))
value_menus = "-25.23"
print(value_menus.zfill(7))



