def add(a,b):
    return(a+b)

print(add(3,4))
print(type(add))

ad = add
print("Function without argument",ad(5,6))

del add
# print(add(5,6))

print(ad(5,6))

def add1(x=8,y=3,z=4) :
    return(x+y+z)

print(add1())
print(add1(8,2,z=5))

def square(x):
    return x*x

def applier(Fn,x):
    return Fn(x)

print(applier(square,3))

# Lambda Functions

f = lambda x,y : x+y
print(f(3,4))

# OR
f1 = (lambda x,y : x+y)(3,4)
print(f1)

def outerfn(x):
    def innerfn():
        return x
    return innerfn

print(outerfn(8))

myfunc = outerfn(7)
print(myfunc())

# decorator

def decor(func):
    def wrap():
        print('**********')
        func()
        print('**********')
    return wrap

def sayhello():
    return print('hello')

newfunc = decor(sayhello)
print(newfunc())

# Parameterized wrap decorator

def decor1(func):
    def wrap(a,b):
        if b==0:
            print('Cannot divide by zero')
            return
        else :
            return func(a,b)
    return wrap

@decor1
def divide(a,b):
    return a/b

# newfunc1 = decor1(divide)
# print(newfunc1(4,2))

print(divide(4,0))