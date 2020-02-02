import math

s = "Radical Technologies"
dict_dup={}
l = list(s)
l1 = str(l)
print(l1)
print(l)
count = 0
for i in l :
    count1=l.count(i)
    d = dict.fromkeys(l,count1)


print(d)

# From internet

from collections import Counter
print(Counter(s))

# Duplicates from String DOUBT IN THIS (One e not coming)
def dupl(str,n) :
    index = 0
    for i in range(0,n) :

        for j in range(0,i+1) :
            if(str[i]==str[j]):
                break
        if(j==i):
            str[index]=str[i]
            index+=1
    return "".join(str[:index])

print(dupl(list(s),len(s)))

num1 = 134.55678
print(round(num1))

print(math.floor(num1))


# Correct code for alphabets as key and their count as value

for i in s:
    if i in dict_dup:
        dict_dup[i]=dict_dup[i]+1
    else :
        dict_dup[i]=1
print(dict_dup)

str1 = 'RARAR'
# print(str1.count('RAR'))
cnt=0
for i in range(len(str1)-2):
    if(str1[i]+str1[i+1]+str1[i+2]=='RAR'):
        cnt = cnt + 1
print(cnt)
# For RAR combinations that are not adjacent and can be anywhere.
cnt1 = 0
for i in range(len(str1)):
    for j in range(i+1,len(str1)):
        for k in range(j+1, len(str1)):
            if(str1[i]+str1[j]+str1[k]=='RAR'):
                cnt1 = cnt1 + 1
print(cnt1)
# count1 = 0
# for i in str1 :
#     if i =='RAR':
#         count1 +=1
#
# print(count1)

