# num = 13

# print(bin(num)[2:])

def decimal_to_binary(num):
    if num>=1:
        decimal_to_binary(num//2)
    print(num %2, end="")
num =13 
decimal_to_binary(num)