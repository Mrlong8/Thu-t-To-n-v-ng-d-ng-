#Bit mat bat de
#from queue import Queue
#q=Queue()
#n,k =map(int,input().split())
#for i in range(1,n+1): q.put(i)
#while q.qsize()>1:
#    for i in range(k-1):q.put(q.get())
#    q.get()
#print(q.queue[0])
#cach 2 danh sach lien ket vong
#class Node:
#    def __init__ (self,e=0,N=None):
#        self.elem=e
#        self.next=N
#if __name__=="__main__":
#    n,k=map(int,input().split()) 
#    H=None
#    for i in range(1,n+1):
#        if i==1:
#            H=Node(1)
#            H.next=H
#        else:
#            H.next=Node(i,H.next)
#            H=H.next   
#    for i in range(n-1):
#        for j in range(k-1):
#            H=H.next
#        H.next=H.next.next
#    print(H.elem)         
"""
#canh cua than ky 
from queue import Queue
ten=["dangdungcntt", "tienquanutc", "quang123", "maianh", "nguyenminhduc2820"]
def sol():
    q=Queue()
    n=int(input())
    for x in ten:q.put([x,1])
    while n>q.queue[0][1]:
        n-=q.queue[0][1]
        q.put(q.get())
        q.queue[-1][1]*=2
    print(q.queue[0][0])  
if __name__=="__main__":
    for i in range(int(input())): sol()
"""    
#buon dưa le
from queue import Queue
q=Queue()
n,k,m=map(int,input().split())
a=list(map(int,input().split()))+[0]*(k-1)
s=0
for x in a:
    q.put(x)
    while q.qsize()>k:q.get()
    t=0
    while q.qsize()>0 and t+q.queue[0]<=m:t+=q.get()
    if q.qsize()>0 and t<m:
        q.queue[0]-=m-t
        t=m
    s+=t
print(s)        