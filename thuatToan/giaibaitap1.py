a, b, c, d = map(int ,input().split())
# c, d = map(int, input().split())

result = min(b,d) - max(a,c)

if result < 0 :
    print(0)
else:
    print(result)


# print("YES" if a == c == b + d else "NO")