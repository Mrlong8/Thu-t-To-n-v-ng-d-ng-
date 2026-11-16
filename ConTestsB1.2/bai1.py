a = int(input())
b = int(input())

if(b < a):
    c = a
    a = b
    b = c
sum = 0
for i in range(a,b+1):
    if i % 13 != 0 :
        sum += i

print(sum)
