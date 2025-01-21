fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#2
newlist2 = [x if x != "banana" else "orange" for x in fruits]
print(newlist2)

