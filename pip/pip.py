#PIP is a package manager for Python packages, or modules if you like.

#means pip in python is like module

#so just use it, and save time to write code(already written code)

#A package contains all the files you need for a module.

#Modules are Python code libraries you can include in your project.


#How to install it


#Check PIP version:

#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version


#Download a package named "camelcase":

#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase


#use installed pip, we have installed camelcase

import camelcase

c= camelcase.CamelCase()

txt="hello world"
print(c.hump(txt))


#we can find packages

#Find Packages
#Find more packages at https://pypi.org/.


#Remove a Package
#Use the uninstall command to remove a package:

#Example
#Uninstall the package named "camelcase":

#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase

#List installed packages:

#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list