# a small function can be writed by lambda espression.

# original function
def sum(x,y):
    return x + y

print(sum(4,5))

# with lamnda

sumlambda = lambda x,y: x + y

print(sumlambda(4,5))

g = (lambda x,y: x + y)(1,2)

# LIST LAMBDA
# To make a lambda funcion for a list its necesary use the method map

list_tl = [4565,4568,45532,45567,4562155,1,225]

menor_values = list(map(lambda list: list * 2, list_tl))

print(menor_values)




