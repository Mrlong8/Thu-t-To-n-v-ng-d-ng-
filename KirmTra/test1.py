import math
n = int(input())
tong = 0
for i in range(1,math.sqrt(n) + 1):
    if n % i == 0:
        tong += i
        if  i* i != n:
            tong += n//i

print(tong)