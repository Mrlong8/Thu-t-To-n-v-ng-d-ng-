import sys


arr = sys.stdin.read().strip();

if(len(arr) < 10):
     print(arr[:1],end = "")
elif(len(arr) <= 189):
    print(arr[:2],end = "")
elif(len(arr) <= 2889):
    print(arr[:3],end = "")
elif(len(arr) <= 38889):
    print(arr[:4],end = "")
elif(len(arr) <= 488889):
    print(arr[:5],end = "")
else:
    print(arr[:6],end = "")

