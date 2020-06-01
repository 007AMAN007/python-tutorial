import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mypythondb"
)

# print(mydb) #check if connected

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mypythondb") #create database

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") #create table


#again now there are many things to learn in it, but mysql is same everywhere you know it very well