n= int(input())

dsDdt = []
dsNgoai = []

for i in range (n):
    dong = input()
    cactu = dong.split()
    khoa = cactu[-1]
    diem = int(cactu[-2])
    ten = " ".join(cactu[:-2])

    sinhvien = (diem,ten)

    if(khoa == "DDT"):
        dsDdt.append(sinhvien)
    else:
        dsNgoai.append(sinhvien)


dsNgoai.sort(reverse=True)
dsDdt.sort(reverse=True)

print(f"Giai nhat :{dsDdt[0][1]}")
print(f"Giai nhi :{dsDdt[1][1]}")
print(f"Giai ba :{dsDdt[2][1]}")
print(f"Giai giao luu :{dsNgoai[0][1]}")