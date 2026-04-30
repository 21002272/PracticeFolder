class Shopping:
    def __init__(self):
        self.info = {}

    def create(self, p,r,s):
        self.info[p] = {
            "product":p,
            "price":r,
            "instock":s
        }
        print(f"Shopping '{p}' is created")

    def read(self,p):
        try:
            print(self.info[p])
        except KeyError:
            print("Product not found!")

    def update_price(self,p,new_value):
        try:
            if isinstance(new_value,int):
                self.info[p]["price"] =new_value
                print("Price updated successfully")
            else:
                print("Provide integer data for the price")
        except KeyError:
            print("Product not found")
    def bought(self,p,num):
        try:
            if isinstance(num,int):
                if self.info[p]["instock"]>=num:
                    self.info[p]["instock"] -=num
                    print(f"{num} items purchased successfully")
                else:
                    print(f"Only {self.info[p]['instock']} items available.")
            else:
                print("Please enter only numbers")
        except KeyError:
            print("Product not found!")
    def stock_added(self,p,num):
        try:
            if isinstance(num,int):
                self.info[p]["instock"] += num
                print(f"{num} items of {p} added to the stock successfully")
            else:
                print("Please enter only numbers.")
        except KeyError:
            print("Product not found!")
    def delete(self, p):
        try:
            del self.info[p]
            print(f"{p} deleted successfully")
        except KeyError:
            print("Product not found")
shop = Shopping()
shop.create("shirt", 1000, 12)
shop.create("pant",1200,8)
shop.read("shirt")
shop.update_price("shirt",900)
shop.bought("shirt",3)
shop.stock_added("pant",10)
shop.delete("shirt")