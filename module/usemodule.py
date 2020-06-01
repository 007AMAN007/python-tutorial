from mymodule import person #import from module
import datetime #import inbuild module

print(datetime.datetime.now())


#there are many function in "datetime" module

#similarly there is inbuild "math" module

#similarly there is inbuild "json" module

#Python has a built-in package called json, which can be used to work with JSON data.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x) #Convert from Python to JSON:

# the result is a JSON string:
print(y)


#one more inbuild module "re" => regular expression

import re

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


#note there are many module & many functions in module so read carefully & usde carefully
