from collections import namedtuple

SinhVien = namedtuple("SinhVien", ["hoten", "date", "famer"])
ds = []

def ngayThangNam(sv):
        ngay,thang,nam = sv.date.split('/')
        return (int(nam),int(thang),int(ngay))

while True:
    try:
        dong = input().split()
        if not dong: 
            continue  # Bỏ qua nếu là dòng trống
            
        hoten = " ".join(dong[:-2])
        date = dong[-2]
        famer = dong[-1]
        
        ds.append(SinhVien(hoten, date, famer))
        
    except EOFError:
        break

ds.sort(key=ngayThangNam)

for sv in ds:
        print(sv.hoten + " " + sv.date + " " + sv.famer)