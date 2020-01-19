a ={}
print(type(a))

a=set()
print(type(a))

d1={'Name' : 'abc', 'Age' : 90}
s= d1['Name']
print(s)

d1['Name'] = 'xyz'
print(d1)


d3={'Name':'anvesh' , 'Age' : 22}
k1 = d3.get('Name','xyz')
print("Name value in dict is : ", k1)
print(d3)

e = dict([('Name','abc'),('Age',40)])
print(e)

e['Address']='Aundh'
print(e)

b= e.pop('Name')
print(b)
a=e.popitem()
print(a)

list1 = ['Name', 'Age', 'Profession']
d1=dict.fromkeys(list1)
print(d1['Name'])

d1['Name']='abc'
d1['Age']=50
d1['Profession']='Developer'

print(d1)

# help(dict)

list2 = ['Name', 'Age', 'Profession']
d2=dict.fromkeys(list2, 'abc')
print(d2,"\n")

print(d1.items())
print(d1.keys())
print(d1.values())
print("\n")

d2 = {'Name' : 'Connor', 'Age' : 44, 'Profession' : 'Mechanic'}
d1.update(d2)
print(d1.items(),"\n")

for key in d1.keys() :
    print(key,":",d1[key])

print("\n")

for value in d1.values() :
    print(value)


sec_large = {'key1' : 3, 'key2' : 4, 'key3' : 1, 'key5' : 6}
value = 0
key = None
for key in sec_large.keys() :
    if value<sec_large[key] :
        value=sec_large[key]

print(key,":",value)

value1 = 9999
key1 = None
for key1 in sec_large.keys() :
    if value1 > sec_large[key1] :
        value1=sec_large[key1]
    else :
        continue
print(key1,":",value1)

s ="Radical Technologies"
help(str)