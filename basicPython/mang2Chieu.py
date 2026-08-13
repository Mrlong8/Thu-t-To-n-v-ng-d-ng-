# các tạo ra ma trận bằng cach sử dụng các mảng 1 chiều làm các phần tử của mẩng 1 chiều khác
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

for row in matrix:
    # print(row)
    for col in row:
        print(col, end = ' ')
    print()
