from rent import Gown_Rent, Suit_Rent, Customer

gown = Gown_Rent(100)
suit = Suit_Rent(100)
customer = Customer()

def welcome():
    print("||||| Welcome to JRRK Wardrove Rental Shop System |||||")
    start = input("\nPress any key to continue...")

welcome()

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
                gown.displayStock()
            elif gSelect == 2:
                customer.rentalTimeG = gown.rentDay(customer.rentOutfit("gown"))
                customer.rentalBasisG = 1
                print("------------------------------------")
            elif gSelect == 3:
                customer.rentalTimeG = gown.rentWeek(customer.rentOutfit("gown"))
                customer.rentalBasisG = 2
                print("------------------------------------")
            elif gSelect == 4:
                customer.bill = gown.returnOutfit(customer.returnOutfit("gown"), "gown")
                customer.rentalBasisG, customer.rentalTimeG, customer.gowns = 0, 0, 0
                print("------------------------------------")
            elif gSelect == 5:
                print("||||| Welcome to JRRK Wardrove Rental Shop System |||||")
            elif gSelect == 6:
                print("Thank you for trusting JRRK Wardrove Rental Shop! Have a nice day!")

                break
            else:
                print("Invalid Input! Please enter a number between 1 - 6")
        elif choice == "B" or choice == "b":
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
                    suit.displayStock()
                elif sSelect == 2:
                    customer.rentalTimeS = suit.rentDay(customer.rentOutfit("suit"))
                    customer.rentalBasisS = 1
                    print("------------------------------------")
                elif sSelect == 3:
                    customer.rentalTimeS = suit.rentWeek(customer.rentOutfit("suit"))
                    customer.rentalBasisS = 2
                    print("------------------------------------")
                elif sSelect == 4:
                    customer.bill = suit.returnOutfit(customer.returnOutfit("suit"), "suit")
                    customer.rentalBasisS, customer.rentalTimeS, customer.suits = 0, 0, 0
                    print("------------------------------------")
                elif sSelect == 5:
                    print("------------------------------------")
                elif sSelect == 6:
                    break
                else:
                    print("Invalid Input! Please enter a number between 1 - 6")
            
        elif choice == "E" or choice == "e":
            print("Thank you for trusting JRRK Wardrove Rental Shop! Have a nice dayyyy!")
            break
        else:
            print("Invalid Input! Please enter A, B or E!")

    except ValueError:
        print("Value Inputted is not a number!")
        continue