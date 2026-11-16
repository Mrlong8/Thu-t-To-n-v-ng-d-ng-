n = int(input())



arr = [0,1]
for i in range(0,n-2):
    temp = arr[i] + arr[i+1]
    arr.append(temp)


for i in range(0,n):
    print(arr[i],end =" ")


