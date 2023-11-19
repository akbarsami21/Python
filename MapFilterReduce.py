

l1=[2,4,6,8]
def cube(x):
    return x**3

c=list(map(cube,l1))
print(c)

l2=[2,4,6,8]
def big(x):
    return x>5
c=list(filter(big,l1))
print(c)

import functools as f
l3=[2,4,6,8]
l4=[1,3,5,7]
def sum(x,y):
    return x+y
c=f.reduce(sum,l3)
print(c)



