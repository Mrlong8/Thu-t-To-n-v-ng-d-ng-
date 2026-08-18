n = int(input())
a = list(map(int, input().split()))

def scp(x):
    if x < 0:
        return False
    return x == int(x ** 0.5) ** 2 # trả về true nếu đúng

b = len([x for x in a if x % 3 != 0])
# viết như này có nghĩa là Lấy từng phần tử x trong a,
#  nếu x thỏa điều kiện thì đưa x vào một list mới."

c = len([x for x in a if scp(x)])

d = len([
    1 for x, y in zip(a, a[1:])
    # zip() ghép các phần tử cùng vị trí của hai dãy.
    # Mỗi lần lấy một cặp số liên tiếp, gán số thứ nhất vào x, số thứ hai vào y
    # nếu điều kiện thỏa mãn thêm 1 vào danh sách
    if x != 0 and y % x == 0
])

e = len([x for x in a if x % 2 == 0]) # số lượng số chắn
g = n - e # số lượng số lẻ

f = e * (e - 1) // 2 + g * (g - 1) // 2
# cặp số bất kỳ cùng chắn lẻ

h = len([
    1 for x, y, z in zip(a, a[1:], a[2:])
    if x < y < z
])

print(b)
print(c)
print(d)
print(f)
print(h)