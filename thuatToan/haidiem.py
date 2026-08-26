from collections import namedtuple

Diem = namedtuple("Diem",["x","y"]);
n = int(input())

A = set();

ok = "YES"

for i in range(n):
    x,y = map(int,input().split())

    A.add(Diem(x,y))

    if len(A) < i:
        ok = "NO"
        break
print(ok)