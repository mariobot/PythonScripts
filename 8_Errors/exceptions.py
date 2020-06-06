# Document reference https://docs.python.org/3/tutorial/errors.html

#10 * (1/0)
#error ZeroDivisionError

#4 + spam*2
#error NameError 

#"2" + 2
#error TypeError

while True:
    try:
        x = int(input("Write a number: "))
        break
    except ValueError:
        print("That is not a valid number, Try again: ")

print(f"The value is {x}")

#a exception can handle a different types errors 

while True:
    try:
        x = int(input("Write a number: "))
        break
    except (ValueError,TypeError,NameError):
        print("That is not a valid number, Try a: ")

# to generate an exception use the keyword rise

try:
    raise TypeError("THIS IS AN TYPEERROR")
except:
    print("Error provider by the user")
    #raise # return the error traceback

#finally instruction

def zeroFunc(x,y):
    return x/y

try:
    x = zeroFunc(5,0)
except ZeroDivisionError:
    print(ZeroDivisionError)
else:
    print(f"result is: {x}")
finally:
    x = None
    print(f"Value of x is: {x}")

# a good practice to force the finally is usint the with keyboard
# this force that the statement was colsing after the excecution
# if present an error the execution was closing. 

#with open("myfile.txt") as f:
#    for line in f:
#        print(line, end="")

# use the rise keyword to execute and exception

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')    

# a good example of execution is

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")