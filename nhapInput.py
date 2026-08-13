# cú phap input(prompt)
s = input("xin nhập xâu bất kì : ")
print("xâu vừa nhập là : ",s)

so =  int(input("Nhập vào 1 số : "))
print("Số vừa nhập là : ", so)

# các cách nhập nhiều só trên 1 hàng

baso = input("Nhập 3 số : ")
a = baso.split() # dùng để phân tách
x,y,z = map(int, a) # dùng để ép các phần tử trong list => sang kiểu mmong muốn
print(x + y + z)

# nhập 4 só
m, n, p ,q = map(int, input().split())
print(m,n,p,q)