def dem(x):
    if x<0 : return 0
    return 1 if x==0 else 2
if __name__ =='__main__':
    a,b,c=map(float,input().split())
    if a == 0 and b == 0 and c == 0:
        res = -1
    elif a == 0 and b == 0:
        res = 0
    elif a == 0:
        res = 1
    else:
        b /= 2
        d = b * b - a * c
        res = dem(d)
    print(res)