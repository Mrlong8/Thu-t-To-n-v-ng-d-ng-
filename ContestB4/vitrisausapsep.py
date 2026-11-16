n = int(input())


a = list(map(int,input().split()))

arr = []


for i in range(n):
    arr.append((a[i],i+1))


arr.sort(key=lambda x : x[0])

for x in arr:
    print(x[1],end=" ")







