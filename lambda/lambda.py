# this is new thing in python
# see how % why we can use this

#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.

#syntax (lambda argument:excpression)

#x = lambda a : a + 10 #A lambda function that adds 10 to the number passed in 
#as an argument, and print the result:
x= lambda a,b,c: a+b+c
print(x(2,3,4))

#we can use lamda in function also



#Why Use Lambda Functions?
#The power of lambda is better shown when you use them as
#  an anonymous function inside another function.

#Say you have a function definition that takes one argument,
#and that argument will be multiplied with an unknown number: