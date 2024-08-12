
def primecheck(num):
    c=0
    if num>1:
        for i in range(1,num+1):
            if(num%i==0):
                c+=1
    if c==2:
        # print(f"The given: {num} numer is Prime")
        return True
    else:    
        # print(f"The given: {num} numer is not a Prime")
        return False

print(primecheck(17))