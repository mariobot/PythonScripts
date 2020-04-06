# Reference documentation https://docs.python.org/3/tutorial/stdlib.html

# the Standard Libraries provide a extra functionalities in python
# for example libraries to interact with the Operative System 
# for example libraries to math operations
# for example libraries to acces to internet. 

import os 

print(os.getcwdb()) # return the current working directory

print(os.system("dir")) # execute a comand in the system

print(dir(os)) # provide list of modules in os library
# provide help 
# print(help(os))

# this library provide a util functions to manipule easy mode files
import shutil
try:
    shutil.copy("file1","file2")
    shutil.move("file1","file2")
except:
    pass

# glob library improve the search fuctionalitiy in a folder. 
# for example to find .py files in a folder
import glob

print(glob.glob("*.py"))

# re library provide a regex functionalities

import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print("hi firend, hi girldfrien".replace("hi","bye"))

# math library provide mathematics functionalities

import math

print(math.pi)
print(math.log(1024,2))

# statistics library provide a basic stadistics functions like mean, median, variance
import statistics

my_data = [5.0,60.5,411]
print(statistics.median(my_data))
print(statistics.variance(my_data))

# urllib.request provide access to Internet libraries
# smtplib  provide accesss to email functionalities

import smtplib

try:
    server = smtplib.SMTP("smp.server.com")
    server.sendmail("pythoncourse@mail.com","student@mail.com","Welcome to python libraries")
    server.quit()
except:
    pass

# datetime improve Date functionalities
from datetime import date

now = date.today()

b_date = date(2020,5,4)

birthday = b_date - now

print(now)
print(birthday)



