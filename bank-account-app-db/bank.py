from dbconfig import mydb
from bankFeatures import BankFeatures

class Bank:
  obj = BankFeatures()
  print("Enter option")
  option = raw_input()
  if option=='1':
    obj.show()
  elif option=='2':
    obj.addBalance()
  elif option=='3':
    obj.withdrawlBalance()
  elif option=='4':
    obj.addAcct()