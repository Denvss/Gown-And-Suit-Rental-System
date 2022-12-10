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
        
        rentalTime, rentalBasis, numOfOutfit = request
        bill = 0
        
        if outfit == "suit":
            if rentalTime and rentalBasis and numOfOutfit:
                self.stock += numOfOutfit
                now = datetime.datetime.now()
                
                if rentalBasis == 1: # daily
                    bill = suitDPrice * numOfOutfit
                elif rentalBasis == 2: #♠ weekly
                    bill = suitWPrice * numOfOutfit
                
                if numOfOutfit >= 3:
                    print("You have an extra 20% discount!")
                    bill *= 0.8
                    
                print("Thank you for returning your suit!")
                print("Price: ₱{}".format(bill))
                
        elif outfit == "gown":
            if rentalTime and rentalBasis and numOfOutfit:
                self.stock += numOfOutfit
                now = datetime.datetime.now()
                
                if rentalBasis == 1: # daily
                    bill = gownDPrice * numOfOutfit
                elif rentalBasis == 2: #♠ weekly
                    bill = gownWPrice * numOfOutfit
                
                if numOfOutfit >= 3:
                    print("You have an extra 20% discount!")
                    bill *= 0.8
                    
                print("Thank you for returning your gown!")
                print("Price: ₱{}".format(bill))
                
        else:
            print("You do not rent an Outfit!")
            return None

class Suit_Rent(OutfitRent):
    
    global discountRate
    discountRate = 15  
    
    def __init__(self, stock):
        super().__init__(stock)
    
    def discount(self, b):
        bill = b - (b * discountRate) / 100
        return bill

class Gown_Rent(OutfitRent):
    
    def __init__(self, stock):
        super().__init__(stock)

class Customer:
    
    def __init__(self):
        self.gowns = 0
        self.rentalBasisG = 0
        self.rentalTimeG = 0
        self.suits = 0
        self.rentalBasisS = 0
        self.rentalTimeS = 0
        
    def rentOutfit(self, outfit):
        if outfit == "gown":
            gowns = input("How many gown(s) would you rent: ")
            
            try:
                gowns = int(gowns)
            except ValueError:
                print("Input must be a number!")
                return -1
            
            if gowns < 1:
                print("Number of gown should be greater than zero!")
                return -1
            else:
                self.gowns = gowns
            return self.gowns
            
        elif outfit == "suit":
            suits = input("How many suit(s) would you rent: ")
            
            try:
                suits = int(suits)
            except ValueError:
                print("Input must be a number!")
                return -1
            
            if suits < 1:
                print("Number of suit should be greater than zero!")
                return -1
            else:
                self.suits = suits
            return self.suits
        else:
            print("Request Outfit error!")
    
    def returnOutfit(self, outfit):
        if outfit == "gown":
            if self.rentalTimeG and self.rentalBasisG and self.gowns:
                return self.rentalTimeG, self.rentalBasisG, self.gowns
            else:
                return 0,0,0
        elif outfit == "suit":
            if self.rentalTimeS and self.rentalBasisS and self.suits:
                return self.rentalTimeS, self.rentalBasisS, self.suits
        else:
            print("Return Outfit error!")