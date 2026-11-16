# D = {
#     61 :'Brasilia',
#     71 : 'Salvador',
#     11 : 'Sao Paulo',
#     21 :'Rio de Janeiro',
#     32 :'Juiz de Fora',
#     19 :'Campinas',
#     27 :'Vitoria',
#     31 :'Belo Horizonte'
# }

# print(D.get(int(input()),'DDD nao cadastrado'))

# a = "hffhr98fyewc8rhfsjkfhs"
# D = {}

# đếm tần suất
input()
a = list(map(int,input().split()))
D={}
for x in a :
    D[x]=D.get(x,0)+1
# print(D.items())

for k in sorted(D.keys()): print(k,D[k])

# phần tử áp đảo
from collections import Counter

input()
a = list(map(int,input().split()))
D={}
for x in a :
    D[x]=D.get(x,0)+1
# print(D.items())

for k in sorted(D.keys()): print(k,D[k])

# đếm số cặp cột điện bằng nhau


# đếm giày
R,L = {},{}
 # dãy con liên tục khác biệt