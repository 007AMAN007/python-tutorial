# try:
#   print(x) #This statement will raise an error, because x is not defined:
# except:
#   print("An exception occurred")



#many except

# try:
#   print(x)
# except NameError: #Print one message if the try block raises a NameError and another for other error
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else: #You can use the else keyword to define a block of code to be executed if no errors were raised:
#   print("Nothing went wrong")


# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally: #The finally block, if specified, will be executed regardless if the try block raises an error or not.
#   print("The 'try except' is finished")

#Raise an error and stop the program if x is lower than 0:

# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


# Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")