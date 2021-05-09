class Product:
    def __init__(self,name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price*percent_change
        else:
            self.price -= self.proce*percent_change
    def print_info(self):
        print(f"product_name: {self.name}, price: {self.price}, category: {self.category}")

class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = []
    def add_product(self, new_product):
        self.product_list.append(new_product)
    def sell_product(self, id):
        if id in range(0, len(self.product_list)):
            product_sell = self.product_list.pop(id)
            product_sell.print_info()
    def inflation(self, percent_increase):
        for product_item in self.product_list:
            product_item.price += product_item.price*percent_increase
    def set_clearance(self, category, percent_discount):
        for product_item in self.product_list:
            if product_item.category == category:
                product_item.price -= product_item.price*percent_discount

prod1 = Product("soap", 2.51,"clean")
prod2 = Product("shampoo", 5.99,"clean")
prod3 = Product("bread", 3.25,"food")
prod4 = Product("apple", 0.99,"food")
prod5 = Product("orange", 1.99,"food")
prod6 = Product("milk", 3.99,"dairy")
prod7 = Product("cheese", 7.69,"dairy")

store1 = Store("Costco")
store1.add_product(prod1)
store1.add_product(prod2)
store1.add_product(prod3)
store1.add_product(prod4)
store1.add_product(prod5)
store1.add_product(prod6)
store1.add_product(prod7)

store1.sell_product(3)
store1.inflation(0.10)
store1.set_clearance("food", 0.20)
for item in store1.product_list:
    print(f"product_name: {item.name}, price: {item.price}, category: {item.category}")

