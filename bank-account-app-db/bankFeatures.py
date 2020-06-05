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



#use same logic for input condition