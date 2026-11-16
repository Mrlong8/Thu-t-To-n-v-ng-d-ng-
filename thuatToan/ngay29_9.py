#  bài toán "lượng nước"   https://laptrinhonline.club/problem/tichpxluongnuoc

from itertools import accumulate

n = int(input())
a = list(map(int,input().split()))
L = list(accumulate(a,lambda x, y :max(x,y)))
R = list(accumulate(a[::-1],lambda x,y:max(x,y)))[::-1]

s= 0
for x, y,z in zip(L,a[1:],R[2:]) : s+= max(min(x,z)-y,0)
print(s)


# thư viện queue
import queue

s = queue.LifoQueue() #stack
for x in range(s.queue[-1])
while not s.empty(): print(s.get())

# bài toán khối lượng hóa chất   https://laptrinhonline.club/problem/tichpxweighthoachat
from queue import LifoQueue

KL = {'c':12, 'H':1,'O':16,'(':0}

def sol():
    S=LifoQueue()
    for c in input():
        if c in KL.keys(): S.put(KL[c])
        elif c == '(:':
            t= 0 
            while S.queue[-1] != 0 : t+= S.get()
            S.queue[-1] = t
        else: S.queue[-1] *= int(c)
    print()

    print(s)


if __name__ == '__main__':
    for i in range(int(input()):sol())



# kiểm tra ngoặc đúng https://laptrinhonline.club/problem/kiemtrangoacdung


# xếp hàng 
# chào tân sinh viên K59
# bịt mwaawrt bắt dê

from queue import Queue
q = Queue()
n,k = map(iny,input().split())
for i in range (1,n+1): q.put(q.get())
q.get()
print(q.queue[0])

# buân dưa lê
# bịt mắt bắt dê
#tìm kiếm theo chiều rộng và tìm kiếm theo chiều xâu
