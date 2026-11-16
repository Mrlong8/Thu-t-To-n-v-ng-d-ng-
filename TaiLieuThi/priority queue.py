#Priorityqueue
"""
#sap xep co dieu kien
from queue import PriorityQueue
class item:
    def __init__ (self,e):self.elem=e
    def __gt__ (self,other):
        a = self.elem % 3
        b = other.elem % 3
        if self.elem % 3 != other.elem % 3:
            return self.elem % 3 > other.elem % 3
        return self.elem > other.elem
n = int(input())
a = list(map(int, input().split()))
q = PriorityQueue()
for x in a:q.put(item(x))
while q.qsize() > 0:print(q.get().elem, end=" ")
"""
"""
#vi tri sau khi sap xep
from queue import PriorityQueue
q = PriorityQueue()
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    q.put((a[i], i + 1))
while not q.empty():
    x = q.get()
    print(x[1], end=" ")
"""
"""
#noi thanh kim loai
from queue import PriorityQueue
q=PriorityQueue()
res=0
n=input()
for x in map(int,input().split()):q.put(x)
while q.qsize()>1:
    x=q.get()+q.get()
    res+=x
    q.put(x)
print(res)    
"""
"""
#thuat toan ma hoa Huffman
from queue import PriorityQueue
from collections import Counter
q=PriorityQueue()
res=0
D=Counter(input())
for x in D.values():q.put(x)
while q.qsize()>1:
    x=q.get()+q.get()
    res+=x
    q.put(x)
print(res)    
"""

#phan tu trung vi
from queue import PriorityQueue
l=PriorityQueue()
r=PriorityQueue()
n=int(input())
a=list(map(int,input().split()))
for i,x in enumerate(a,1):
    if i%2:l.put(-x)
    else:r.put(x)
    if i>1 and -l.queue[0]>r.queue[0]:
        x=-l.get()
        y=r.get()
        l.put(-y)
        r.put(x)
    print(-l.queue[0],end=" ")    
    