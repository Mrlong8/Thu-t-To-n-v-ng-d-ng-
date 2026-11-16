x = int(input())

tong = 0

if(x < 50 ):
    tong = x * 100
if(x >= 50 and x < 1000 ):
    tong = x * 500
if(x >= 1000 and x < 10000 ):
    tong = x * 1000
if(x >= 10000):
    tong = x * 1200

print(tong)