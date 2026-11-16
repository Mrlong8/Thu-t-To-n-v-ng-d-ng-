#dictionary va phuong phap đêm
#d={2:3,4:"abc","mua":"nghi hoc",(3,4):[80,87,67]}
#print(d)
#print(d.keys())
#print(d.values())
#print(d['mua'])
#print(d.get(0))
#print(d.get(0,"k co"))
#a="shifstjczxbjtdxvbn"
#d={}
#for x in a: d[x]=d.get(x,0)+1
#print(d.items())
#ma vung dien thoai 
#d={61:"Brasilia",71:"Salvador",11:"Sao Paulo",21:"Rio de Janeiro",32:"Juiz de Fora",19:"Campinas",27:"Vitoria",31:"Belo Horizonte"}
#print(d.get(int(input()), "DDD nao cadastrado"))
#tan suất
#input()
#a=list(map(int,input().split()))
#d={}
#for x in a: d[x]=d.get(x,0)+1
#for k in sorted(d.keys()):print(k,d[k])
#phan tu ap dao
#from collections import Counter
#n=int(input())
#a=list(map(int,input().split()))
#d={}
#for x in a: d[x]=d.get(x,0)+1
#d=Counter(a)
#res="khong co pt ap dao"
#for k,v in d.items():
#    if v>n/2:
#        res=k
#        break
#print(res)        
#Dem so cap cot dien cao = nhau
#n=int(input())
#a=list(map(int,input().split()))
#d={}
#for x in a: d[x]=d.get(x,0)+1
#kq = 0
#for k in d.values(): kq += k * (k - 1) // 2
#print(kq)
#dem giay
#r,l={},{}
#for i in range(int(input())):
#    x=input()
#    z=int(x[1:])
#    if x[0]=='L': l[z]=l.get(z,0)+1
#    else: r[z]=r.get(z,0)+1
#res=0
#for k,v in l.items():
#    res+=min(v,r.get(k,0))    
#print(res)    
#day so lien tuc khac biết
n = int(input())
a = list(map(int, input().split()))
d={}
res=0
L=0
for R,x in enumerate(a,1):
    L=max(L,d.get(x,-1))
    res=max(res,R-L)
    d[x]=R
print(res)    