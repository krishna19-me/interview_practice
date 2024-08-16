from item import Item
#INHERITANCE

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        
        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater than or equal to zero"
        self.broken_phones = broken_phones
        
iphone = Phone("Iphone 14 pro", 110000.25, 4, 1)

print(iphone.calculate_total_price())

pixel = Phone("Google Pixel 6a", 30000, 5, 1)

print(pixel.calculate_total_price())
    
print(Phone.all_items)

