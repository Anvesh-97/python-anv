l1 = [1,2,3,4]
l2=[]
'''for i in range(len(l1)):
    l2[i]=l1[i]+1

print(l2)
'''
# Internet solution

k=1
res =[x+k for x in l1]
print(res)

k1=-1

res1=[y+k1 for y in l1]
print(res1)

print(sorted(l1,reverse=True))

list3 = [1,2,3,4,5,6,7,8,9]
l3=[]
for i in range(0,2) and range(-3 , -1):
    l3.append(list3[i])

print(l3)

list4=[]
list4.append(list3[0:3] + list3[-3:-1])
print(res)