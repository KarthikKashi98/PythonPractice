def sum1(arr):
    s=sum(arr)
    a=s/len(arr)
    return s,a


n=int(input("enter the no of integers in the list"))
print("enter the ",n ," elements")
arr=[]
for i in range(n):
    arr.append(int(input()))

s,a=sum1(arr)
print("sum of elements in the array is",s)
print("average of n elements in the array is",a)
