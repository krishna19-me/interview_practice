l=[1,4,3,8,5,9,20]

for i in range (len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l[-2])           

''' second large'''

number=[10,5,8,20,3]
# large=0
# selarge=0
# for num in number:
#     if num > large:
#         selarge=large
#         large=num
#         print(selarge)
#         print(large)
#     elif num > selarge and num!= large:
#         selarge=num
# print(selarge)        


large=0
second_large=0
for num in number:
    if num> large:
        second_large=large
        large=num
    elif num > second_large and num!=large:
        second_large=num
print(second_large)        
