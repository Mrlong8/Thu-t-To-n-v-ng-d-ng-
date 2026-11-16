#groupby
#from itertools import groupby
#people = [
#    ("A", "An"),
#    ("A", "Bình"),
#    ("A", "Chi"),
#    ("B", "Dũng"),
#    ("B", "Hà"),
#    ("C", "Lan"),
#]
#for room, people_in_room in groupby(people, key=lambda x: x[0]):
#    print(room, [name for _, name in people_in_room])
#accumulate
#truy van tong 
from itertools import accumulate
n,q=map(int,input().split())
a=list(map(int,input().split()))
b=[0]+list(accumulate(a))
for _ in range(q):
    L,R=map(int,input().split())
    print(b[R]-b[L-1])
