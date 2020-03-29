import fibo, sys

#dir() function return the types used in the module or file

# list the types used in fibo
print(dir(fibo))

# list the types used by sys
print(dir(sys))

# list al the types used by file
print("--------\n")
print(dir())


# to import submodule you can referer the module of the package. 
# this import a subpackage of a package

# from sound.efect.echo import echofilter
# echofilter("param","1","2","3")




