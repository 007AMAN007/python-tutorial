# What is NumPy?
# NumPy is a python library used for working with arrays.

# It also has functions for working in domain of linear algebra, fourier transform, and matrices.

# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

# NumPy stands for Numerical Python.

# Why Use NumPy ?
# In Python we have lists that serve the purpose of arrays, but they are slow to process.

# NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# Arrays are very frequently used in data science, where speed and resources are very important.

# Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

# Why is NumPy Faster Than Lists?
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

# This behavior is called locality of reference in computer science.

# This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

# Which Language is NumPy written in?
# NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

# Where is the NumPy Codebase?
# The source code for NumPy is located at this github repository https://github.com/numpy/numpy

# import numpy

# arr = numpy.array([1,2,3,4]) #note: it different from inbuild list, dict,tupple in python

# #we will use this rather than other things so read carefully

# print(type(arr))

# arr = numpy.array(1) #0d array

# arr = numpy.array([1,2,3]) #1d array

# arr = numpy.array([[1,2,3],[3,4,5]]) #2d array

# arr = numpy.array([[[1,2,3],[3,4,5],[7,8,9]]]) #3d array

# arr = numpy.array([[[1,2,3],[3,4,5],[8,9]]]) #but this is 2d array, see the difference carefully



# print(arr.ndim) #check dimension off array

#Create an array with 5 dimensions and verify that it has 5 dimensions:

# import numpy as np

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)


#array indexing is same 

#array slicing/range is same as we read previous

# arr = np.array([1,2,3,'am'])

# print(arr.dtype) #check data type of array

#Create an array with data type string:

# arr = np.array([1,2,3], dtype='S') #You can't write small s


# print(arr)
# print(arr.dtype)

#For i, u, f, S and U we can define size as well.

#A non integer string like 'a' can not be converted to integer (will raise an error):





# The Difference Between Copy and View
# The main difference between a copy and a view of an array is that the copy
# is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not affect
# original array, and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect
# the original array, and any changes made to the original array will affect the view.

# import numpy

# arr = numpy.array([1,2,3])

# x= arr.copy() #it will change only arr
# arr[0]=90
# print(arr)

# print(x)


# arr = numpy.array([1,2,3])

# x= arr.view() #it will change both x & arr
# arr[0]=90
# print(arr)

# print(x)


# Shape of an Array
# The shape of an array is the number of elements in each dimension.

# Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a tuple with 
# each index having the number of corresponding elements.


# arr = numpy.array([[1,2,3],[2,4,5]]) #2d with 3 eles

# arr = numpy.array([[1,2,3],[2,4]]) #2d with null eles

# print(arr.shape)

#iteration is same as we read previous
 



#  Use concatenate for join two or more arrays


# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])

# # newarr = np.array_split(arr, 3) #it will split array into 3 arrays, 2els in each

# newarr = np.array_split(arr, 5) #it will split array into 5 arrays, 2els, in arr1, left all have 1 els

# print(newarr)


# Searching Arrays
# You can search an array for a certain value, and return the indexes that get a match.

# To search an array, use the where() method.

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 4, 4]) #Find the indexes where the value is 4:

# x = np.where(arr == 4)

# print(x)

# import numpy as np

# arr = np.array([6, 7, 8, 9])

# x = np.searchsorted(arr, 7) #Find the indexes where the value 7 should be inserted:

# print(x)


# Sorting Arrays
# Sorting means putting elements in a ordered sequence.

# Ordered sequence is any sequence that has an order corresponding
# to elements, like numeric or alphabetical, ascending or descending.

# The NumPy ndarray object has a function called sort(), that will sort a specified array.


# import numpy as np

# arr = np.array([3, 2, 0, 1])

# print(np.sort(arr))

#I am not reading "unfunc" & "filter" topic read it if need anywhere