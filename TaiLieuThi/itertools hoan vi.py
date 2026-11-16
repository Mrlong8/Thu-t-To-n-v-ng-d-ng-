#hoan vi
#from itertools import permutations
#a = [1, 2, 3]
#for x in permutations(a):
#    print(x)
#Hoan vi 4
#from itertools import permutations
#n=int(input())
#bd=0
#for x in permutations(range(1,n+1)):
#    if all((x[i]+x[i+1])%4!=0 for i in range(n-1)):
#        print(*x)
#        bd+=1
#print(bd)   
#cach quay lui
#n = int(input())
#a = []
#count = 0
#def backtrack():
#    global count
#    if len(a) == n:
#        print(*a)
#        count += 1
#        return
#    for x in range(1, n + 1):
#        try:
            # Nếu x đã có trong a thì bỏ qua
#            a.index(x)
#            continue
#        except ValueError:
#            # x chưa xuất hiện
#            pass
        # Kiểm tra điều kiện hai số cạnh nhau
#        if a and (a[-1] + x) % 4 == 0:
#            continue
#        a.append(x)
#        backtrack()
#        a.pop()
#backtrack()
#print(count)
#hai tam giác
#def tg(a): return sum(a)>2*max(a)
#def ktra(p): return tg(p[:3]) and tg(p[3:])
#def sol():
#    a=list(map(int,input().split()))
#    P=permutations(a)
#    for p in P:
#        if ktra(p): return "yes"
#    return "no"
#if __name__=='__main__':
#    for i in range(int(input())): print(sol())
#xau hình sin
#from itertools import permutations
#def dem(a): return sum(x > y < z for x, y, z in zip(a, a[1:], a[2:]))
#n, m, k = map(int, input().split())
#a = 'a' * n + 'b' * m + 'c' * k
#res = 0
#for p in permutations(a): res = max(res, dem(p))
#print(res)
