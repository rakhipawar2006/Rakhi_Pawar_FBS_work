class Product:
    def __init__(self, pid=None, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        
    def getData(self):
        return f"PID : {self.pid}\nPRODUCT NAME : {self.pname}\nPRICE : {self.price}\nQUANTITY : {self.quantity}"
    
    def __del__(self):
        print("Destructor is called.")
        
p1 = Product()
print(p1.getData())

print("\n##################\n")
p2 = Product(501, "Laptop", 61000, 2)
print(p2.getData())