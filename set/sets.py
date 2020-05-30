#A set is a collection which is unordered and unindexed.
#In Python sets are written with curly brackets.
# what i see in set there is no repetitive element 
#& also elements in excending order
x={1,2,3}
#print(x[1]) You cannot access items in a set by
#referring to an index, since sets are unordered the items has no index.

# functions in sets

#some related to list but we will use here which are not in list
#x.add(5) #To add one item to a set use the add() method.
x.update([7,6,4]) #To add multiple items to a set use the add() method.
print(x)