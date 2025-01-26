

class Item:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

class Orders:
    def __init__(self, items_list, country):
        self.item_list = items_list
        self.country = country

    def calculate_total(self):
        print(f"Calculating Total Amount: ")
        total = 0
        for item in self.item_list:
            total += item.price * item.quantity
        total += TaxCalculator.calculate_tax(total=total, country=self.country)
        return total

class TaxCalculator:

    @staticmethod
    def calculate_tax(total, country):
        print("\nCalculating Total Amount after adding Tax : ")
        if country == "US":
            total += total * 0.07
        elif country == "EU":
            total += total * 0.04
        else:
            total += total * 0.01
        return total

if __name__ == "__main__":
    item1 = Item(10, 20)
    item2 = Item(200,5)
    item3 = Item(5,2000)

    order_us = Orders([item1,item2, item3], "US")
    print(f"\nTotal Amount is = {order_us.calculate_total()}")


