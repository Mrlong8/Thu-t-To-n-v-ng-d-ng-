import math

n = int(input())

a = list(map(int,input().split()))

tu = a[-1]
mau = 1

for i in range(n - 2, -1,-1):
    tu_moi = a[i] * tu + mau
    mau_moi = tu

    tu  = tu_moi
    mau = mau_moi

ucln = math.gcd(tu,mau)
tu //= ucln
mau //= ucln

print(f"{tu}/{mau}")