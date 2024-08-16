from item import Item

item1 = Item("privateItem", 100)

# __ - private variable , need to have getter and setter
# _ - protected variable, need to have property for reading it

print(item1.name)