from Packages import Rent
from Packages import CustomerManage
from Packages.Rent import Gown_Rent, Suit_Rent, Customer

customer = Customer()

def welcome():
    print("||||| Welcome to JRRK Wardrove Rental Shop System |||||")
    start = input("\nPress any key to continue...")

def menu():
    print("\n-- MANAGEMENT --")
    print("A. Manage Customer")
    print("B. Rental")
    print("E. Exit")

def customerOperation():
    print("\n-- OPERATIONS --")
    print("A. Create Account.")
    print("B. Delete Account.")
    print("E. Exit.")

def customerManage():
    customerOperation()
    op = input("Enter your choice: ")
    
    if op == "A" or op == "a":
        CustomerManage.createAccount()
    elif op == "B" or op == "b":
        CustomerManage.deleteAccount()
    else:
        print()


def rental():
    while True:
        print("""\n
                        A. Gown Menu
                        B. Suit Menu
                        E. Exit
        """)

        choice = input("Choose Yours :) : ")

        try:
            if choice == "A" or choice == "a":
                print("""
                    ||||| Gown Menu |||||
                    1. Display Available Gowns
                    2. Rent a Gown for a Day (₱800)
                    3. Rent a Gown for a Week (₱4800)
                    4. Return a Gown
                    5. Main Menu
                    6. Exit
                    """)
                gSelect = int(input("Choose Yours:) : "))

                if gSelect == 1:
                    Rent.Gown_Rent(100).displayStock()
                elif gSelect == 2:
                    customer.rentalTimeG = Rent.Gown_Rent(100).rentDay(customer.rentOutfit("gown"))
                    customer.rentalBasisG = 1
                    print("------------------------------------")
                elif gSelect == 3:
                    customer.rentalTimeG = Rent.Gown_Rent(100).rentWeek(customer.rentOutfit("gown"))
                    customer.rentalBasisG = 2
                    print("------------------------------------")
                elif gSelect == 4:
                    customer.bill = Rent.Gown_Rent(100).returnOutfit(customer.returnOutfit("gown"), "gown")
                    customer.rentalBasisG, customer.rentalTimeG, customer.gowns = 0, 0, 0
                    print("------------------------------------")
                elif gSelect == 5:
                    print("||||| Welcome to JRRK Wardrove Rental Shop System |||||")
                elif gSelect == 6:
                    print("Thank you for trusting JRRK Wardrove Rental Shop! Have a nice day!")

                    break
                else:
                     print("Invalid Input! Please enter a number between 1 - 6")