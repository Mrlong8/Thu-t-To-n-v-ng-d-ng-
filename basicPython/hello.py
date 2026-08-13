
# Lồng hàm input() bên trong int() để ép kiểu ngay khi người dùng nhập xong
# a,b = map(float,input().split())
a = int(input())
tong = 0;
# for i in range (1,a+1): tong += i
tong = a * (a + 1) // 2
print(tong)


