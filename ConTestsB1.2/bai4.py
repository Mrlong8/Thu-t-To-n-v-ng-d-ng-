import sys
DEF = 10**9 + 7

input_data = sys.stdin.read().split()
tong = sum(map(int, input_data))

kq = tong % DEF

print(kq)