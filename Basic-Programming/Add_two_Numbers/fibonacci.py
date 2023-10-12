def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-2)+fib(n-1)

x=int(input())
if(x<=0):
    print("enter positive number")
else:
    for i in range(x):
        print(fib(i),end=" ")
