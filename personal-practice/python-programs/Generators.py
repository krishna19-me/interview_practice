#fibonnaci series using generators

def fib(limit):
    a, b = 0,1 
    while b < limit:
        yield b
        a, b = b, b+a
nums  =fib(50)
for n in nums:
    print(n)