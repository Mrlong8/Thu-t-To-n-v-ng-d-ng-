# tính số ngày
def nhuan(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


def songay(d, m, y):
    s = 0
    for i in range(1, y):
        s += 366 if nhuan(i) else 365

    thang = [31, 29 if nhuan(y) else 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
    for i in range(m - 1):
        s += thang[i]
    return s + d


def main():
    d1, m1, y1 = map(int, input("Nhap ngay thu nhat (ngay thang nam): ").split())
    d2, m2, y2 = map(int, input("Nhap ngay thu hai (ngay thang nam): ").split())
    print(abs(songay(d2, m2, y2) - songay(d1, m1, y1)))


if __name__ == "__main__":
    main()