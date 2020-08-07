# https://docs.python.org/3/tutorial/introduction.html

# this is the first comment
spam = 1  # and this is the second comment # ... and now a third!
text = "# This is not a comment because it's inside quotes."

# Numbers
2 + 2 # Execute a sum
50 - 5*6 # Execute first the multiplication and later the rest
(50 - 5*6) / 4 # Execute first the multiplication 5*6 later the rest 50-30 later divisor to 4
8 / 5  # division always returns a floating point number
17 / 3  # classic division returns a float

# MOD and foalt
17 // 3  # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 * 3 + 2  # result * divisor + remainder

# price tax example
tax = 12.5 / 100
price = 100.50
price_total = price * tax
print(price_total)

# STRINGS

'spam eggs'  # single quotes
'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

# Use r when you need to print \n value in the text
print(r'C:\some\name')  # note the r before the quote

# Use """ text multiline """ or ''' multiline text ''' whent try to print multiline text
print("""\
Totorial: by [Mario Botero]
     -m                        Recomend this tuto to learn
     -ar                       For most info check the README FILE in the core of the project
     -i                        Tutoriales y mas para el conocimiento basico de PYTHON
     -o                        RECUERDE QUE LA MEJOR MANERA DE APRENDER ES LEER Y HACER
""")

# Concatenation strings
# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'

# if do you need concetenate so long string you can use
text = ('Put several strings within parentheses '
        'to have them joined together.')
text

word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)
word[:2] + word[2:]
word[:4] + word[4:]
word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end

