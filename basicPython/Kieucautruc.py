from collections import namedtuple

Diem = namedtuple("Diem","x y")
A = Diem(3,4)
print(A.x,A.y)