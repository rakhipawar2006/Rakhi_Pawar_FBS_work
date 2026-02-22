class Product:
    discount = 20
    
    def __init__(self, pid=None, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        
    def apply_discount(self):
        discount_amt = (self.price * Product.discount) / 100
        self.price = self.price - discount_amt
      
    def getData(self):
        return f"PID : {self.pid}\nPRODUCT NAME : {self.pname}\nPRICE AFTER DISCOUNT : {self.price}\nQUANTITY : {self.quantity}"
    
    def __del__(self):
        print("Destructor is called.")
        
p1 = Product()
p1.apply_discount()
print(p1.getData())

print("\n##################\n")
p2 = Product(501, "Laptop", 61000, 2)
p2.apply_discount()
print(p2.getData())