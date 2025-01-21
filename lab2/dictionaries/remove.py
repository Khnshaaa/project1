thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The pop() method removes the item with the specified key name:


#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):4
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2.popitem()
print(thisdict2)