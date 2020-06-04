from bankFeature import BankFeature


class Bank:
    i = 0
    accountBalance = 0
    obj = BankFeature()
    while i < 10:
        option = raw_input("Enet 1 for deposit, 2 for withdrawl, 3 for check balance, 0 for exit: ")
        if option == '1':
            obj.add()
        elif option == '2':
            obj.withdrawl()
        elif option == '0':
            exit()
        elif option == '3':
            obj.show()    
        else:
          print("Enter valid option")    
        i += 1
