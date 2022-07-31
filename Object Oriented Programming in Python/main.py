from item import Item
from phone import Phone
from keyboard import Keyboard

# Item.instantiate_from_csv()
        
# phone1 = Phone("samsung", 500, 5, 0)
# phone2 = Phone("apple", 1000, 1)

# print(phone1.calculate_total_price())
# print(Item.all)
# print(Phone.all)

item1 = Keyboard("Logitech", 750)
item1.apply_discount()
print(item1.price)