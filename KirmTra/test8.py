
n = int(input())
a = list(map(int, input().split()))

ds = []
for i in range(n):
    dem = 0
    for j in range(i + 1, n):
        if a[j] > a[i]:
            dem = j - i
            break
    ds.append(dem)
for i in range(len(ds)):
    print(ds[i], end=" ")