#can't name function my-func

def myfunc():
  print("Hi aman")

#myfunc() # can't write it above of def

#argument same as other language

def my_func2(*names): #Arbitrary Arguments, *args
  print(names[2])

my_func2("aman","rahul",2)

def my_func3(name1,name23):
  print(name1)

my_func3(name1="aman",name23="rahul") #You can also send arguments with the key = value syntax.


def my_func4(**names): #Arbitrary Keyword Arguments, **names
  print(names['name1'])

my_func4(name1="aman",name23="rahul")

def my_func5(name="aman"): #Default Parameter Value
  print(name)

my_func5("")

#return is same as in other languages