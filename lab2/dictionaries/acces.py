# There is also a method called get() that will give you the same result:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
s = thisdict["model"]

#2
#The keys() method will return a list of all the keys in the dictionary.
#x = thisdict.keys()
#x = thisdict.get("model")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"

print(x) #after the change