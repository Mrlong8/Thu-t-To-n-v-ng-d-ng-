a = 100
print(type(a)) #khai báo ra kiểu dữ liệu của a

# các cách in các chữ số thập phan sau dấu ,
b = 25.456457546
print("%.2f" %b)
print(round(b,2)) # hàm này có sự làm tròn
print("{:.2f}".format(b))

c =  True
print(type(c))

s = """python C++ 
C# """#in ra sâu ký tự trên cùng nhiều dòng
print(s)

# ép kiểu str(), int(), float()...
d = "14134535"
h = int(d)
print(type(h))