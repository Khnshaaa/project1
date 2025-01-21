#  If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#If the item to remove does not exist, discard() will NOT raise an error.
thisset2 = {"apple", "banana", "cherry"}

thisset2.discard("banana")

print(thisset2)

# Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
#The del keyword will delete the set completely:
#The clear() method empties the set:
