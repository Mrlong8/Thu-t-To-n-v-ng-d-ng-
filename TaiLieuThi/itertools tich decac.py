#tich decac
#from itertools import product
#A = [1,2,3,4,5,6]
#B = ['a', 'b', 'c']
#print(list(product(A, B)))
#sm tap the 
from itertools import product
n,M=map(int, input().split())
A=[]
for i in range(n):
    k,*a=map(int, input().split())
    A.append(list(a))
P=product(*A)
res=0
for p in P:
    s=sum(x*x for x in p)%M
    res=max(res,s)
print(res)    