def factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    return fact


print(factorial(5))


# RECURSION

def fact_recursion(n):
    if n < 1:
        return 1
    else:
        return n * fact_recursion(n-1)


print(fact_recursion(5))
