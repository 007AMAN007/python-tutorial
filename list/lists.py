# list is same as that of arrays, let's see some properties

x = ['aman', 'rohit', 'rahul']  # Create a List:

# print(x) print list
# print(x[1]) Print the second item of the list:
# print(x[-1]) Negative indexing means beginning from the end, -1 refers to the last item,
# -2 refers to the second last item etc.
# print(x[0:2]) #This will return the items from position 0 to 2.
# Remember that the first item is position 0,
# and note that the item in position 2 is NOT included
# print(x[:2]) #This example returns the items from the beginning to "rohit":
# -ve index can also included
# x[1] = 'raman' #change list value at certain index
#for i in x: #loop in list
#  print(i) #loop in list continue
#rint("amans" in x) Check if Item Exists, same as that in string as string is also array of chars



#There are many methods in list some of we are explaining here which are not in java
#x.append("herman") Using the append() method to append an item:
#x.remove('aman')The remove() method removes the specified item:
#x.pop() The pop() method removes the specified index, (or the last item if index is not specified):
#del x[0] The del keyword removes the specified index:
#del x The del keyword can also delete the list completely:
#y=[1,2,3]
#z=x+y #Join Two Lists
print(x) 