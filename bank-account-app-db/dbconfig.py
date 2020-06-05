import mysql.connector

mydb=None

try:
  mydb = mysql.connector.connect(

  host="localhost",
  user="root",
  passwd="",
  database="mypythondb"

)
except:
  print("database error")