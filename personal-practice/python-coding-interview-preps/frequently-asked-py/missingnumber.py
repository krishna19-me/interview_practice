
def missingnum(l):
    misnum=(set(i for i in range(min(l),max(l)+1))-set(l))
    return misnum

print(missingnum([11,12,13,14,16,17,18,19]))