def listsquare(x):
    return x*x

l =  lambda x : x*x

m = map(l,[2,4,6,8])
print(list(m))

def add(x,y):
    return x+y

addlambda = lambda x,y : x+y
list1 = [1,2,3]
list2 = [2,4,6]
iterable = map(addlambda,list1,list2)
print(list(iterable))

scores = [60, 70, 80, 55, 43, 90]

def pass_scores(score):
    return score>65

lambda_65 = lambda x : x>65
# filter
over_65 = list(filter(pass_scores,scores))
print(over_65)

map_65 = list(map(lambda x : x>65,[60, 70, 80, 55, 43, 90]))
print(map_65)

# Reduce
from functools import reduce
def do_sum(x,y):
    return x+y

list_red = [1,2,3,4]
r = reduce(do_sum,list_red,10)
print(r)