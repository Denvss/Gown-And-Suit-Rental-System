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
   
print("testing")

