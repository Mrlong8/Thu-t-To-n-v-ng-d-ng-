# bài toán trinh thám
from collections import deque
Q=deque()
n,k=map(int,input().split())
a=list(map(int,input().split()))
for i,x in enumerate(a):
    while len(Q)>0 and Q[-1][1]<=x: Q.pop()
    Q.append((i,x))
    if i>=k-1:
        while i-Q[0][0]>=k: Q.popleft()
        print(Q[0][1], end=" ")


#  những con đường về 0