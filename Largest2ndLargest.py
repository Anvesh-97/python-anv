d1 = {'key1' : 2, 'key2': 3, 'key3' : 7, 'key4' : 5}
# Largest
value = 0
for key in d1.keys() :
    if value < d1[key] :
        value=d1[key]
        key1=key


print(key1,":",value)

# 2nd Largest
max2 = 0
max4 = max(d1.values())
print("Max using func.",max4)
for key2 in d1.keys() :
    if(d1[key2]<max4 and d1[key2]>max2) :
        max2=d1[key2]
        key3 = key2

print(key3,":",max2)


min = min(d1.values())
min1=9999
for keym in d1.keys() :
    if min1>d1[keym] :
        min1 = d1[keym]
        keymin = keym

print(keymin,":",min1)


# 2nd Minimum value
min2 = 9999
for key2 in d1.keys() :
    if(d1[key2]>min and d1[key2]<min2) :
        min2=d1[key2]
        key3 = key2
print(key3,":",min2)

diff1 = [1, 2, 3]
diff2 = [3, 4, 5]
res1=[]
res = diff1 + diff2
for i in range(0, len(res)):
    for j in range(i+1, len(res)):
        if res[i] != res[j]:
            res1.append(res[i])
            break
        # if diff2[j] != diff1[i] :
        #     res.append(diff2[j])
print(res1)

max1=[1,"abc",-3,"xyz", -33]
resmax = []
m=0
for x in range(0,len(max1)):
    if(type(max1[x])==int):
        resmax.append(max1[x])

print(resmax)
print(max(resmax))


list5 = [1,3,5,6,7,2,3,9,11]
for i in range(0,len(list5)):
    if list5[i]>5:
        print(list5[i])
        break


        # for y in range(0,len(resmax)):
        #     if m<resmax[y]:
        #         m=resmax[y]

for j in range(0,len(list5)):
    if (list5[j]/2)!=0 :
        print(list5[j])
        break

l5=[]
for i in range(0,len(list5)):
    if list5[i]>5:
        l5.append(list5[i])
print(l5)

diffl1 = [1,2,3]
diffl2 = [1,2,4]
finaldiff=[]
setdiff=set()
setdiff = (set(diffl1) ^ set(diffl2))
# Symmetric difference
print(setdiff)

# 2nd way of different elements :
for i in diffl1:
    if i in diffl2:
        continue
    else:
        finaldiff.append(i)

for j in diffl2:
    if j in diffl1:
        continue
    else:
        finaldiff.append(j)

print(finaldiff)