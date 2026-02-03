class Shirt:
    def __init__(self, sid=None, sname="", type=None,price=0, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        
    def getData(self):
        return f"SID : {self.sid}\nSHIRT NAME : {self.sname}\nSHIRT TYPE: {self.type}\nPRICE : {self.price}\nSIZE : {self.size}"
    
    def __del__(self):
        print("Destructor is called.")
        
s1 = Shirt()
print(s1.getData())

print("\n##################\n")
s2 = Shirt(100, "Cotton King", "Casual", 1500, "Medium")
print(s2.getData())
