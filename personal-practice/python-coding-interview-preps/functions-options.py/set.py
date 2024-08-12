# a=set()
a={1,2,3.4,"t","r"}
a.add('e')
a.remove(1)
# a[0]=12 #unordered so set can't changed
print(a)


normal_set = set(["a", "b","c"])
 
print("Normal Set")
print(normal_set)
# A frozen set
frozen_set = frozenset(["e", "f", "g"])
print("\nFrozen Set")
print(frozen_set)


# for i in enumerate()