
n = int(input())
a = input().split()
ds = {}

for i in range(n):
    tu = a[i]

    if tu in ds:
        ds[tu] += 1
    else:
        ds[tu] = 1

dem = max(ds.values())
kq = []
for tu in ds:
    if ds[tu] == dem:  kq.append(tu)
kq.sort()
print(kq[0], dem)
