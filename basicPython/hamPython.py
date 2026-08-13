#function
def tong(a,b):
    res = a + b
    return res

def gt(n):
    res = 1
    for i in range(1, n + 1, 1):
        res *= i 
    return res

if __name__ == '__main__':
    #code run
    print("hello")
    x, y = map(int, input().split())
    print(tong(x, y))
    print(" giai thừa của x : ",gt(x))

