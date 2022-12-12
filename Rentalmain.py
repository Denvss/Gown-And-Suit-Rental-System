from Packages import Rent
from Packages import CustomerManage
from Packages.Rent import Customer

customer = Customer()

class RentalClass:
    def __init__(self, rentID, customerID, quantity, price):
        self.rentID = rentID
        self.customerID = customerID
        self.quantity = quantity
        self.price = price

    def data(self):
        return ("{:<30} {:<30} {:<30} {:<30}".format(self.rentID, self.customerID, self.quantity, self.price))


def welcome():
    print("||||| Welcome to JRRK Wardrove Rental Shop System |||||")

def menu():
    print("\n--- MANAGEMENT ---")
    print("A. Manage Customer")
    print("B. Rental")
    print("E. Exit")

def customerOperation():
    print("\n-- OPERATIONS --")
    print("A. Create Account.")
    print("B. Delete Account.")
    print("E. Go to Management.")

def rental():
    while True:
        print("\n-- RENTAL MENU --")
        print("A. Gown Menu")
        print("B. Suit Menu")
        print("E. Exit")

        choice = input("Choose Yours :) : ")

        try:
            
            if choice == "A" or choice == "a":
                rentIdExist = False
                rentID = int(input("Enter Rent ID: "))
                with open("RentRecords.txt", "r") as prs:
                    lines = prs.readlines()
                    for n in range(len(lines)):
                        if str(rentID) in lines[n].split():
                            rentIdExist = True
                            break
                        else:
                            rentIdExist = False
                
                if rentIdExist:
                    print("\nRent ID already Exists")
                    rental()

                found = False
                customerID = input("Enter Customer ID: ")
                with open("CustomerAccount.txt", "r") as prs:
                    lines = prs.readlines()
                    for n in range(len(lines)):
                        if customerID == lines[n].split()[0]:
                            found = True
                            break
                        else:
                            found = False
                
                if not found:
                    print("\nCustomer does'nt Exist!")
                    rental()

                print("""
                    ||||| Gown Menu |||||
                    1. Display Available Gowns
                    2. Rent a Gown for a Day (₱800)
                    3. Rent a Gown for a Week (₱4800)
                    4. Return a Gown
                    5. Main Menu
                    6. Exit
                    """)

                gSelect = int(input("Choose Yours :) : "))

                if gSelect == 1:
                    Rent.Gown_Rent(100).displayStock()
                elif gSelect == 2:
                    customer.rentalTimeG = Rent.Gown_Rent(100).rentDay(customer.rentOutfit("gown"))
                    customer.rentalBasisG = 1
                    quantity = int(input("Enter Again the Quantity to Confirm: "))
                    price = 800 
                    price = quantity * price
                    rent = RentalClass(rentID, customerID, quantity, price)
                    with open("RentRecords.txt", "a") as val:
                        val.write("\n")
                        val.write(rent.data())

                    print("\nRent Recorded Successfully!")
                    print("------------------------------------")
                elif gSelect == 3:
                    customer.rentalTimeG = Rent.Gown_Rent(100).rentWeek(customer.rentOutfit("gown"))
                    customer.rentalBasisG = 2
                    quantity = int(input("Enter Again the Quantity to Confirm: "))
                    price = 4800 
                    price = quantity * price
                    rent = RentalClass(rentID, customerID, quantity, price)
                    with open("RentRecords.txt", "a") as val:
                        val.write("\n")
                        val.write(rent.data())

                    print("\nRent Recorded Successfully!")
                    print("------------------------------------")
                elif gSelect == 4:
                    customer.bill = Rent.Gown_Rent(100).returnOutfit(customer.returnOutfit("gown"), "gown")
                    customer.rentalBasisG, customer.rentalTimeG, customer.gowns = 0, 0, 0
                    print("------------------------------------")
                elif gSelect == 5:
                    welcome()
                elif gSelect == 6:
                    print("Thank you for trusting JRRK Wardrove Rental Shop! Have a nice day!")
                    exit()

                else:
                     print("Invalid Input! Please enter a number between 1 - 6")
             
            elif choice == "B" or choice == "b":
                rentIdExist = False
                rentID = int(input("Enter Rent ID: ")) 
                with open("RentRecords.txt", "r") as prs:
                    lines = prs.readlines()
                    for n in range(len(lines)):
                        if str(rentID) in lines[n].split():
                            rentIdExist = True
                            break
                        else:
                            rentIdExist = False
                
                if rentIdExist:
                    print("\nRent ID already Exists")
                    rental()

                found = False
                customerID = input("Enter Customer ID: ")
                with open("CustomerAccount.txt", "r") as prs:
                    lines = prs.readlines()
                    for n in range(len(lines)):
                        if customerID == lines[n].split()[0]:
                            found = True
                            break
                        else:
                            found = False
                
                if not found:
                    print("\nCustomer does'nt Exist!")
                    rental()

                print("""
                    ||||| Suit Menu |||||
                    1. Display Available Suits
                    2. Rent a Suit for a Day (₱700)
                    3. Rent a Suit for a Week (₱4200)
                    4. Return a Suit
                    5. Main Menu
                    6. Exit
                    """)
                sSelect = int(input("Choose Yours 🙂 : "))
                
                if sSelect == 1:
                    Rent.Suit_Rent(100).displayStock()
                elif sSelect == 2:
                    customer.rentalTimeS = Rent.Suit_Rent(100).rentDay(customer.rentOutfit("suit"))
                    customer.rentalBasisS = 1
                    quantity = int(input("Enter Again the Quantity to Confirm: "))
                    price = 800 
                    price = quantity * price
                    rent = RentalClass(rentID, customerID, quantity, price)
                    with open("RentRecords.txt", "a") as val:
                        val.write("\n")
                        val.write(rent.data())

                    print("\nRent Recorded Successfully!")
                    print("------------------------------------")
                elif sSelect == 3:
                    customer.rentalTimeS = Rent.Suit_Rent(100).rentWeek(customer.rentOutfit("suit"))
                    customer.rentalBasisS = 2
                    quantity = int(input("Enter Again the Quantity to Confirm: "))
                    price = 4800 
                    price = quantity * price
                    rent = RentalClass(rentID, customerID, quantity, price)
                    with open("RentRecords.txt", "a") as val:
                        val.write("\n")
                        val.write(rent.data())

                    print("\nRent Recorded Successfully!")
                    print("------------------------------------")
                elif sSelect == 4:
                    customer.bill = Rent.Suit_Rent(100).returnOutfit(customer.returnOutfit("suit"), "suit")
                    customer.rentalBasisS, customer.rentalTimeS, customer.suits = 0, 0, 0
                    print("------------------------------------")
                elif sSelect == 5:
                    welcome()
                elif sSelect == 6:
                    print("Thank you for trusting JRRK Wardrove Rental Shop! Have a nice day!")
                    exit()
                else:
                    print("Invalid Input! Please enter a number between 1 - 6")

            elif choice == "E" or choice == "e" :

                print("Thank you for trusting JRRK Wardrove Rental Shop! Have a nice dayyyy!")
                break
            else:
                print("Invalid Input! Please enter A, B or E!")

        except ValueError:
            print("Value Inputted is not a number!")
            continue


# START PROGRAM
welcome()
start = input("\nPress any key to continue...")
ch = ""   
op = "" 
while (ch != "E" and ch != "e"):
    menu()
    ch = input("Enter your choice: ")
    if ch == "A" or ch == "a":  
        
        while (op != "E" and op != "e"):
            customerOperation()
            op = input("Enter your choice: ")

            if op == "A" or op == "a":
                CustomerManage.createAccount()
            elif op == "B" or op == "b":
                CustomerManage.deleteAccount()
            elif op == "E" or op == "e":
                print("\nThank You Very Much!")
                
            else:
                print()
    elif ch == "B" or ch == "b":
        rental()
    elif ch == "E" or ch == "e":
        print("\nThank You Very Much!")
    else:
        print("\nInvalid Input")
