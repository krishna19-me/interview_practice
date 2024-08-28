def fib(n):
    if n == 0:
        return "Enter Valid number"
    elif n == 1 or n ==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(10))

def fib1(n):
    num1= 0
    num2 = 1
    nextnum = num2
    count =1
    while count<=n:
        print(nextnum)
        count+=1
        num1, num2 = num2, nextnum
        nextnum = num1+num2
    print()
print(fib1(10))