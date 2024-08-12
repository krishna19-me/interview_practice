

def dic_schedule(l):
    maxPricedItem = max(l, key=lambda x:x['price'])
    minPricedItem = min(l, key=lambda x:x['price'])
    print(minPricedItem["name"])


lst = [{"name":"dinesh",'price': 99}, {"name":"dinesh",'price': 88}]
print(dic_schedule(lst))