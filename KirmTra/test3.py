t = int(input())
n = 1000000
s = [True] * (n + 1)
s[0] = False
s[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if s[i]:
        for j in range(i * i, n + 1, i):
            s[j] = False
dem = [0] * (n + 1)

for i in range(1, n + 1):
    dem[i] = dem[i - 1]
    if s[i]:
        dem[i] += 1
for i in range(t):
    a, b = map(int, input().split())
    print(dem[b] - dem[a - 1])
