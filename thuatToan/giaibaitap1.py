a, b, c = map(int, input().split())

d = b * b - 4 * a * c

if d < 0:
    print(0)
elif d == 0:
    t = -b/(2*a)
    if t < 0:
        print(0)
    elif t == 0:
        print(1)
    else:
        print(2)
else:
    d = d ** 0.5

    t1 = (-b - d) / (2 * a)
    t2 = (-b + d) / (2 * a)
    count = 0

    if(t1 > 0):count += 2
    elif t1 == 0: count += 1

    if(t2 > 0):count += 2
    elif t2 == 0: count += 1

    print(count)