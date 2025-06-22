class fruit:
    items = None
    unit_price = None
    def set_values(self, items, unit_price):
        self.items = items
        self.unit_price = unit_price    

class apple(fruit):
    def price(self):
        print('Apple price is :', self.unit_price* self.items)

class banana(fruit):
    def price(self):
        print('Banana price is :', self.unit_price* self.items)         

class orange(fruit):
    def price(self):
        print('Orange price is :', self.unit_price* self.items) 

man1 = apple()
man2 = banana()
man3 = orange()

man1.set_values(10, 100)
man1.price()
man2.set_values(20, 50)
man2.price()
man3.set_values(30, 30)
man3.price()
print("Total price is :", man1.unit_price * man1.items + man2.unit_price)