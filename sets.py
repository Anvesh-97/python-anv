a ={1,2,3,4,"anvesh"}
print(a)

b={1,2,3,3,3,3}
print(b)

l=[1,2,3,3,3,4]
s=set(l)
print(s)

f={1,2,3,4,5}
for i in f :
    print(i)

help(f)

g={1,2,3,4,5}
print(g)
g.add(0)
print(g)
g.update([5,6,7])
print(g)

g.remove(7)
print(g)
g.discard(6)
print(g)

# g.remove(7)
# print(g)
g.discard(6)
print(g,"\n")

j={1,2,3,4,5}
print(j)
x=j.pop()
print(x ,"Set is : ",  j)
j.clear()
print(j)

#Set Operations

a={1,2,3,4,5}
b={4,5,6,7}

print("Union : ",a|b)             # Using operators
#OR
print("Union : ", a.union(b))     # Using Function Call
print("Intersection : ", a&b)
print("Intersection : ", a.intersection(b))
print("Difference : ", a-b)
print("Difference : ", a.difference(b))
print("Symmetric Difference (aUb - aUb) : ", a^b)