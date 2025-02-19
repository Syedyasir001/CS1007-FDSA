def fib(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fib(a-1)+fib(a-2)


for i in range(0,7):
    x=fib(i)
    print(x,end=" ")
    
print()
    
n=int(input("enter a number : "))
