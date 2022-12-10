class CustomerClass:
    def __init__(self, customerID, firstname, lastname):
        self.customerID = customerID
        self.firstname = firstname
        self.lastname = lastname

    def data(self):
        return ("{:<25} {:<25} {:<25}".format(self.customerID, self.firstname, self.lastname))


def createAccount():
    try:
        ctrExist = False
        customerID = int(input("Enter Customer ID: "))
        
        with open("CustomerAccount.txt", "r") as prs:
            lines = prs.readlines()
            for n in range(len(lines)):
                if str(customerID) in lines[n].split():
                    print("\nInvalid! Customer ID is already Exist!")
                    ctrExist = True
                    break
        
        if not ctrExist:
            firstname = input("Enter your firstname: ")
            lastname = input("Enter your lastname: ")
            customer = CustomerClass(customerID, firstname, lastname)
            with open("CustomerAccount.txt", "a") as val:
                val.write("\n")
                val.write(customer.data())

            print("\nAccount Created Successfully!")


    except ValueError:
        print("\nYou have entered an invalid input.\n")


def deleteAccount():
    found = False
    customerID = input("Enter Customer ID: ")

    with open("CustomerAccount.txt", "r") as prs:
        lines = prs.readlines()
        with open("CustomerAccount.txt", "w") as prs:
            for thisLine in lines:
                data = thisLine.split()
                if len(data) != 0:
                    if data[0] != customerID:
                        prs.write(thisLine)
                    else:
                        found = True
                else:
                    prs.write(thisLine)
        prs.close()
        if not found:
            print("\nCustomer does'nt Exist!")
        else:
            print("\nAccount deleted Successfully!")