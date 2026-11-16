# hàng đợi ưu tiên


#  vị trí sau khi sắp sếp
from queue import PriorityQueue
q = PriorityQueue();
n - int(input())
a= list(map(int,input().split()))

for i,x in enumerate(a,1): q.put(x,1)
while q.qsize(): print(q.get()[1],end = " ")
#  nối thanh kim loại
