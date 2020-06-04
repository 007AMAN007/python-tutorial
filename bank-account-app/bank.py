from bankFeature import BankFeature


class Bank:
    i = 0
    accountBalance = 0
    obj = BankFeature()
    while i < 10:
        option = raw_input("Enet 1 for deposit, 2 for withdrawl, 0 for exit: ")
        if option == '1':
            obj.add()
        elif option == '2':
            obj.withdrawl()
        elif option == '0':
            exit()
        else:
          print("Enter valid option")    
        i += 1
