def anagram1(s1,s2):
    return sorted([s for s in s1])==sorted([s for s in s2])

def anagram2(s1,s2):
    lis=[i for i in s1]
    c=0
    for j in s2:
        if j in lis:
            c+=1   
    return c==len(lis)       

print(anagram1("eat","ate"))
print(anagram2("eat","ate"))