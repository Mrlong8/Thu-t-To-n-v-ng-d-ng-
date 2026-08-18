a, b, c = map(int, input().split())

dental = b * b - 4 * a * c

if a == 0:
    if b == 0:
        if c == 0:
            print("vo so nghiem")
        else:
            print("vo nghiem")
    else:
        x = -c / b
        print(f"{x:.3f}")

elif dental < 0:
    print("vo nghiem")

elif dental == 0:
    x = -b / (2 * a)
    print(f"{x:.3f}")

else:
    d = dental ** 0.5

    x1 = (-b - d) / (2 * a)
    x2 = (-b + d) / (2 * a)

    if x1 > x2:
        x1, x2 = x2, x1

    print(f"{x1:.3f}")
    print(f"{x2:.3f}")