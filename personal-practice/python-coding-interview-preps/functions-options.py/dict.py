dict={"a":1,"b":2,"c":3}

print([min([dict[k] for k,v in dict.items()])])
print(dict.get("d")) #this will give None
# print(dict["d"]) #this will throw the Keyerror
# dict.pop("a")
print(dict)


def add2dict(d1,d2):
    return {**d1,**d2}
def add2dict_m2(d1,d2):
    merge_dict=d1
    merge_dict.update(d2)
    return merge_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(add2dict(dict1,dict2))
print(add2dict_m2(dict1,dict2))