from collections import deque

n = int(input())
a = deque(range(1, n + 1))
ds = []

while len(a) > 1:
    x = a.popleft()
    ds.append(x)
    y = a.popleft()
    a.append(y)
for i in range(len(ds)):
    print(ds[i], end=" ")
print(a[0])
