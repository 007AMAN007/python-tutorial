import bankModule

class BankFeature:
    def add(self):
        print("Enter deposite amount: ")
        depAmt = raw_input()
        obj = bankModule.totalBalance
        obj = obj+int(depAmt)
        bankModule.totalBalance = obj
        print(bankModule.totalBalance)

    def withdrawl(self):
        print("Enter withdrawl amount: ")
        withAmt = raw_input()
        obj = bankModule.totalBalance
        if obj<1:
          print("You don't have sufficient balance")
        else:
            obj = obj - int(withAmt)
            bankModule.totalBalance = obj
            print(bankModule.totalBalance)
