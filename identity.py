a=301
b=301
print(a is b)

a = [1, 2, 3]
x = [1, 2, 3]

print(a is x)
print(a[0] is x[0])

print(id(a), id(x), id(a[0]), id(x[0]))
