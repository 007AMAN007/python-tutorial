#An iterator is an object that contains a countable number of values.

#An iterator is an object that can be iterated upon, 
# meaning that you can traverse through all the values.

#Technically, in Python, an iterator is an object which 
# implements the iterator protocol, which consist of the methods __iter__() and __next__().


x = ("aman", "rahul", "rohit")
itr = iter(x)
print(next(itr))
print(next(itr))
print(next(itr))
#print(next(itr)) #gives error

#Strings are also iterable objects, containing a sequence of characters:

x="aman"

itr=iter(x)

print(next(itr)) #gives character


#skipping the "scope" topic it same in all languages
#one different thing is there is "global" keyword which we can use anywhere to make object global