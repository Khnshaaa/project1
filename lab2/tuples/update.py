# to update the tuple, we can convert it to a list and then update it
# and then convert it back to a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#2
thistuple2 = ("apple", "banana", "cherry")
a = ("orange",)
thistuple2 += a
print(thistuple2)

