class Shirt:
    price_increment = 0.10 # 10%
    def __init__(self, sid=None, sname="", type=None,price=0, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        
    def calculatePrice(self):
        if self.size == "small":
            self.price = self.price
        elif self.size == "medium":
            self.price += self.price * Shirt.price_increment
        elif self.size == "large":
            self.price += self.price * (Shirt.price_increment * 2)
        elif self.size == "xlarge":
            self.price += self.price * (Shirt.price_increment * 3)
            
    def getData(self):
        return f"SID : {self.sid}\nSHIRT NAME : {self.sname}\nSHIRT TYPE: {self.type}\nPRICE : {self.price}\nSIZE : {self.size}"
    
    def __del__(self):
        print("Destructor is called.")
        
s1 = Shirt()
s1.calculatePrice()
print(s1.getData())

print("\n##################\n")
s2 = Shirt(100, "Cotton King", "Casual", 1500, "medium")
s2.calculatePrice()
print(s2.getData())
