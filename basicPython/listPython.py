# list có thể chứa bất kỳ phần tử nào
# list tương tự như mảng 1 chiều của các ngôn ngữ khác

a = [1,2,3,4,5,"python"]
print(a)

# list contructor
s = "python c++"
b = list(s)
# c = list(range(20))
# print(b,c)

# hàm len() cho biết sl phần tử
# có thể truy cập thông qua chỉ số vd a[1], a[-1]

for i in range(0, len(a)):
    print(a[i], end = " ")

a[2] = "C++"

for item in a:
    print(item, end = " ")

# thêm 1 phần tử vào cuối
a.append(100)
print(a)

# thêm vào vị trí bất kỳ
a.insert(2,1000)
print(a)

# xóa phần tử dùng pop() ( hoặc del() ) nếu không chuyền chỉ só thì xóa pt cuối
# hàm remove() xóa gia trị ( nhưng chỉ xóa đi giá trị đầu tiên có trong list )
# xóa mọi phần tử clear()

# sao chép list
c = a * 2 
print(c) # [1,2,3] -> [1,2,3,1,2,3]

# kiểm tra 1 pt có nằm trong list hay không dùng in 
# nối hai list a.extend(b) hoặc là a += b

# các phương thức của list
# copy() dùng để sao chép c = a.copy()
# count() trả về phàn tử nào đó trong list a.count(1)
# reverse() lật ngược 1 list a. reverse() O(n)
# sort() sắp sếp OnLog(n) theo thứ tự tăng dần
# sorted() trả về mảng mới được sắp sếp
# min(). max(), sum() ...
