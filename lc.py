l = [1,2,3,4,5]

x=[i for i in l]
print(x)

# To add 1 to all elements in list

y = [i+1 for i in l]
print(y)

l1 = ['a','b','c','d']
z=[("the"+j) for j in l1]
print(z)

def add(x):

    return (x+3)

ad = [add(i) for i in l]
print(ad)

str1 = "This is Radical Technologies"
# x1 = str1.split()
# print(x1)
# l2=[]
# for i in x1:
#     l2.append(len(i))
# print(l2)

l3=[len(i) for i in str1.split()]
print(l3)

res = [i[::-1] for i in str1.split()]
print(res)

resstr = " ".join(i[::-1] for i in str1.split())
print(resstr)

l2 = [1,2,3,4,5,6]
res_even = [i for i in l2 if(i%2==0)]
print(res_even)

str2 = "This is Radeical Technologies"
res_ae = [i for i in str2.split() if((i.__contains__('a') and i.__contains__('e'))==False)]
print(res_ae)

res_ae2 = [i for i in str2.split() if ('a' in i and 'e' in i)==False]
print(res_ae2)

str3 = "This is Radical Technologies hghf"

def vow_count(str):
    count1=0
    str_res=[]
    for word in str:
        for j in word:
            if('a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word):
                count1 = count1 + 1

            else:
                continue

    return count1
res_vow = [vow_count(i) for i in str3.split()]
print(res_vow)

l4=[1,2,3,4,5]
oddeven = ['Even' if (i%2==0) else 'Odd' for i in l4]
print(oddeven)

sq_oddeve = [i*i if (i%2!=0) else i*2 for i in l4]
print(sq_oddeve)
#
# l5 = [[1],[2],[3]]
# res_list = [j for i in l5 for j in i]
# print(res_list)

l_1 = [1,2,3]
l_2 = [5,6,7]

res_add = [(l_1[i]+l_2[i]) for i in range(0,len(l_1))]
print(res_add)

d1 = {'1':1, '2':2, '3':3}
[d1.update({i:d1[i]+1}) for i in d1.keys()]

print(d1)
#List of dictionaries
# x =[{str(i):d1[i]+1} for i in d1]
# print(x)


str1 = 'aabbccdefff'
lp=[]
dict1={}
for i in range(len(str1)-1):
    if(str1[i]==str1[i+1]):
        if str1[i] in dict1:
            dict1[str1[i]] = dict1[str1[i]] + str1[i]
        else :
            dict1[str1[i]] = str1[i] + str1[i]

# [print(value) for value in dict1.values()]
print(dict1)

