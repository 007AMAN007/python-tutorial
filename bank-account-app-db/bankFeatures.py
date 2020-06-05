from dbconfig import mydb

class BankFeatures:
    def show(self):
        mycursor = mydb.cursor()
        mycursor.execute("select * from bank")
        myresult = mycursor.fetchall()
        for x in myresult:
          print(x[1])
    def addBalance(self):
        mycursor = mydb.cursor()
        mycursor.execute("select * from bank")
        myresult = mycursor.fetchall()
        for x in myresult:
          balance = x[1]
        addAmt = raw_input("Enter amount to add: ")
        totalBalance = balance + int(addAmt)
        sql = "update bank set balance=%s where id=%s"
        val = (totalBalance,1)
        mycursor.execute(sql,val)
        mydb.commit()
    def withdrawlBalance(self):
        mycursor = mydb.cursor()
        mycursor.execute("select * from bank")
        myresult = mycursor.fetchall()
        for x in myresult:
          balance = x[1]
        withAmt = raw_input("Enter amount to withdrawl: ")
        totalBalance = balance - int(withAmt)
        sql = "update bank set balance=%s where id=%s"
        val = (totalBalance,1)
        mycursor.execute(sql,val)
        mydb.commit() 
    def addAcct(self):
        print("Enter User id: ")
        userId = raw_input()
        print("Enter zero balance: ")
        balance = raw_input()
        mycursor = mydb.cursor()
        sql = "Insert into bank (id,user_id,balance) values(%s,%s,%s)"
        val = (2,userId,balance)
        mycursor.execute(sql,val)
        mydb.commit()



#use same logic for input condition