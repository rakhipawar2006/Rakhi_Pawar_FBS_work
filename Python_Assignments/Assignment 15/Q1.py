class Book:
    def __init__(self, bid=None, bname="", price=0, author=""):
        self.bid = bid
        self.bn = bname
        self.pr = price
        self.au = author
        
    def getData(self):
        return f"BID : {self.bid}\nBOOK NAME : {self.bn}\nPRICE : {self.pr}\nAUTHOR : {self.au}"
    
    def __del__(self):
        print("Destructor is called.")
        
b1 = Book()
print(b1.getData())

print("\n##################\n")
b2 = Book(101, "Mrutyunjay", 800, "Sivaji Sawant")
print(b2.getData())