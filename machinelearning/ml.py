# # Machine Learning is making the computer learn from studying data and statistics.

# # Machine Learning is a step into the direction of artificial intelligence (AI).

# # Machine Learning is a program that analyses data and learns to predict the outcome.

# # we learn mathematics terms here


# # Mean - The average value
# # Median - The mid point value
# # Mode - The most common value


# # import numpy

# # speed = numpy.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# # # print(numpy.mean(speed))
# # # print(numpy.median(speed))
# # # print(numpy.mode(speed))


# # What is Standard Deviation?
# # Standard deviation is a number that describes how spread out the values are.

# # A low standard deviation means that most of the numbers are close to the mean (average) value.

# # A high standard deviation means that the values are spread out over a wider range.

# # Example: This time we have registered the speed of 7 cars:

# # import numpy

# # speed = [86,87,88,86,87,85,86]

# # x = numpy.std(speed)

# # print(x)

# # What are Percentiles?
# # Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.

# # Example: Let's say we have an array of the ages of all the people that lives in a street.

# # ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# # What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.

# # The NumPy module has a method for finding the specified percentile:

# # import numpy

# # ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# # x = numpy.percentile(ages, 75)

# # print(x)


# # Data Distribution
# # Earlier in this tutorial we have worked with very small amounts of data in our examples, just to understand the different concepts.

# # In the real world, the data sets are much bigger, but it can be difficult to gather real world data, at least at an early stage of a project.

# # How Can we Get Big Data Sets?
# # To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.


# # import numpy
# # import matplotlib.pyplot as plt

# # x = numpy.random.uniform(0.0, 5.0, 250) #Create an array containing 250 random floats between 0 and 5:

# # plt.hist(x,5)
# # plt.show()


# Normal Data Distribution
# In the previous chapter we learned how to create a completely random array, of a given size, and between two given values.

# In this chapter we will learn how to create an array where the values are concentrated around a given value.

# In probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution, after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.


# import numpy
# import matplotlib.pyplot as plt

# x = numpy.random.normal(5.0, 1.0, 100000) #Meaning that the values should be concentrated
# #around 5.0, and rarely further away than 1.0 from the mean.

# plt.hist(x, 100)
# plt.show()


# Scatter Plot
# A scatter plot is a diagram where each value in the data set is represented by a dot.

# import matplotlib.pyplot as plt

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# plt.scatter(x, y)
# plt.show()


# Scatter Plot Explained
# The x-axis represents ages, and the y-axis represents speeds.

# What we can read from the diagram is that the two fastest cars were both 2 years old, and the slowest car was 12 years old.

# Following example is for large data, we are using random here


# import numpy
# import matplotlib.pyplot as plt

# x = numpy.random.normal(5.0, 1.0, 1000)
# y = numpy.random.normal(10.0, 2.0, 1000)

# plt.scatter(x, y)
# plt.show()


# read regression thing as well

# Regression
# The term regression is used when you try to find the relationship between variables.

# In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.

# means above we are predicting future results on the basis of previous data we have

# Linear Regression
# Linear regression uses the relationship between the data-points to draw a straight line through all them.

# This line can be used to predict future values.

# import matplotlib.pyplot as plt

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# plt.scatter(x, y)
# plt.show()


# import matplotlib.pyplot as plt
# from scipy import stats

# month = [1,2,3,4,5]
# cases = [0,0,4000,80000,160000]

# slope, intercept, r, p, std_err = stats.linregress(month, cases)

# def myfunc(month):
#   return slope * month + intercept

# mymodel = list(map(myfunc, month))

# plt.scatter(month, cases)
# plt.plot(month, mymodel)
# plt.show()


# Polynomial Regression
# If your data points clearly will not fit a linear regression
#  (a straight line through all data points), it might be ideal for polynomial regression.

# Polynomial regression, like linear regression, uses the
#  relationship between the variables x and y to find the best way to draw a line through the data points.
# import numpy
# import matplotlib.pyplot as plt

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# myline = numpy.linspace(1, 22, 100)

# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()




#Future values




# import numpy
# from sklearn.metrics import r2_score
# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [3,3,600,40000,180000]

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# myline = numpy.linspace(1, 5, 100)

# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()

# speed = mymodel(6)
# print(speed)


# Multiple Regression
# Multiple regression is like linear regression, but with more than one
# independent value, meaning that we try to predict a value based on two or more variables.


#we will take look in after some time we will do some real life example in python not machine learning