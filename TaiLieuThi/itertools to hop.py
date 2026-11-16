#to hop
#from itertools import combinations
#arr = [1, 2, 3, 4]
#for c in combinations(arr, 2): print(c)
#dem cap co tong gioi han 
from itertools import combinations
n,M=map(int,input().split())
a=list(map(int,input().split()))
C=combinations(a,2)
s=0
for c in C:
    if sum(c)<=M: s+=1
print(s)