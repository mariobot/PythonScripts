# reference document https://docs.python.org/3/tutorial/stdlib2.html

# pprint module provide extra functionality to print in console
# make more easy read text at the console. 

import pprint

message = "This message has more than 50 characteres but it si printed in a multiline text defined at 30 width line"

pprint.pprint(message, width=20)

# textwrap format text give a width

import textwrap

print(textwrap.fill(message, width=30))

# Template class permit replace text in a string. 

from string import Template

t1 = Template("${name} is a located in ${mun}")
t1 = t1.substitute(name="Manizales",mun="Caldas")
print(t1)

# use safe_substitute when do you no realy safe of replace values
t1 = Template("${name} is a located in ${mun}")
t1 = t1.safe_substitute(country="USA",mun="Caldas")
print(t1)

# logging permit get a loggin register of your code
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')