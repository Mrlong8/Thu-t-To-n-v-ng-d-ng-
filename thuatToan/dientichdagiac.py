# Chu vi diện tích đa giác

from collections import namedtuple

Diem = namedtuple("Diem", ["x", "y"])

n = int(input())

A = []

for i in range(n):
    x, y = map(float, input().split())
    A.append(Diem(x, y))


def kc(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


def dt(a, b):
    return a.x * b.y - a.y * b.x


def tong(A, f):
    s = 0

    for u, v in zip(A, A[1:] + A[0:1]):
        s += f(u, v)

    return s


if __name__ == '__main__':
    chuvi = tong(A, kc)
    dientich = abs(tong(A, dt)) / 2

    print(f"{chuvi:.3f}")
    print(f"{dientich:.3f}")