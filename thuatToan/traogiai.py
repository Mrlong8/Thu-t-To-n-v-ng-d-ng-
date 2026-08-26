from collections import namedtuple

SinhVien = namedtuple("SinhVien", ["hoten", "d", "k"])
ds = []
n = int(input())
for i in range(n):
    a = input().split()

    hoten = " ".join(a[:-2])
    d = int(a[-2])
    k = a[-1]

    ds.append(SinhVien(hoten, d, k))
ddt = []
khac = []

for i in ds:
    if i.k == "DDT":
        ddt.append(i)
    else:
        khac.append(i)

ddt.sort(key=lambda sv: sv.d, reverse=True)
khac.sort(key=lambda sv: sv.d, reverse=True)
top_ddt = ddt[:3]
top_khac = khac[:1]

print( "Giai nhat :"+top_ddt[0].hoten)
print( "Giai nhi :"+top_ddt[1].hoten)
print( "Giai ba :"+top_ddt[2].hoten)

print( "Giai giao luu :"+top_khac[0].hoten)
