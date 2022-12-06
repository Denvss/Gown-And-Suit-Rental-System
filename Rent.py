import datetime
class OutfitRent:
    
    def __init__(self, stock):
        self.stock = stock
        self.now = 0
        
    def displayStock(self):
        print("{} outfit(s) available to rent.".format(self.stock))
        return self.stock
    
    def rentDay(self, n):
        if n <= 0:
            print("Number should be positive!")
            return None
        elif n > self.stock:
            print("Sorry {} oufit(s) available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} outfit(s) for a Day ".format(n, self.now.hour))
            self.stock -= n
            return self.now

    def rentWeek(self, n):
        if n <= 0:
            print("Number should be positive!")
            return None
        elif n > self.stock:
            print("Sorry {} outfit(s) available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} outfit(s) for a Week.".format(n, self.now.hour))
            self.stock -= n
            return self.now
        
    def returnOutfit(self, request, outfit):
        gownDPrice = 800
        gownWPrice = gownDPrice * 6
        suitDPrice = 700
        suitWPrice = suitDPrice * 6