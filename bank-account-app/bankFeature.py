import bankModule

class BankFeature:
    def add(self):
        print("Enter deposite amount: ")
        depAmt = raw_input()
        obj = bankModule.totalBalance
        if depAmt.isdigit():
            obj = obj+int(depAmt)
            bankModule.totalBalance = obj
            print(bankModule.totalBalance)
        else:
            print("Please enter valid value")

    def withdrawl(self):
        print("Enter withdrawl amount: ")
        withAmt = raw_input()
        obj = bankModule.totalBalance
        if withAmt.isdigit():
            if obj<1:
                print("You don't have sufficient balance")
            else:
                obj = obj - int(withAmt)
                bankModule.totalBalance = obj
                print(bankModule.totalBalance)
        else:
            print("Please enter valid value")

    def show(self):
        print("Your Account balance is: ")
        print(bankModule.totalBalance)
