import pandas as pd
import csv
class Item:
    pay_rate = 0.8 #20% discount default on all products modify during instance creation
    all_items = []
    def __init__(self, name : str, price : float, quantity=0):
        assert price>=0, f"Price {price} is not greater than or equal to 0"
        assert quantity>=0, f"Quantity {quantity} is not greater than or equal to 0"
        
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        Item.all_items.append(self)
    
    @classmethod    
    def instantiate_from_csv(cls):
        with open(r'C:\Users\Admin\Desktop\Work\Interview-Preps\interview_practice\personal-practice\python-programs\OOPS\Items.csv', 'r') as f:
            reader = csv.DictReader(f)
            for item in list(reader):
                Item(name= item["name"],price= float(item['price']),quantity= int(item["quantity"]))   
                
                     
    def calculate_total_price(self):
        return f"Total price of {self.quantity} {self.__name} {self.price * self.quantity}"
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"
    
    @property
    def name(self):
        print("Trying to access the variable!!..")
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
# item1= Item("Mobile", 15000, 1)
# item2 = Item("Laptop", 50000, 1)
# item3 = Item("Chair", 2200, 4)
# item4 = Item("Table", 4200, 2)
# item5 = Item("Cable", 100, 4)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(item3.calculate_total_price())

# itemdf = pd.DataFrame([vars(item) for item in Item.all_items])
# itemdf.to_csv("C:\Users\Admin\Desktop\Work\Interview-Preps\interview_practice\personal-practice\python-programs\OOPS\Items.csv", index=False)
# print(itemdf)

#INSTANTIATING USING CLASS METHOD
Item.instantiate_from_csv()
print(Item.all_items)

print("All Items: " + " ".join([item.name for item in Item.all_items]))
