import sys


t = int(input())

for i in range (t):
    a = sys.stdin.readline()
    ds = a.split()

    arr = []
    for w in ds:
        arr.append(w.capitalize())

    print(" ".join(arr))