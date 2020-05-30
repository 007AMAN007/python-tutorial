#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are 
#written with curly brackets, and they have keys and values.
#what I found it also order the list with excending order of index

x = {
  1: 'Ford',
  7: 'male',
  3: 26
}

#print(x['age']) Get the value of the "age" key:

#some functions of dictionary
#print(x.get('age')) #There is also a method called get() that will give you the same result:
#x['age'] = 25 #Change the "age" to index or add "age" index with value:

# for i in x.values(): # return values
#   print(i)

# for i in x: # return indexes
#   print(i)
#del x # delete dictionary




#Create three dictionaries, then create one dictionary
#that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)