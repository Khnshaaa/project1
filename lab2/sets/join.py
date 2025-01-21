set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#2
set12 = {"a", "b", "c"}
set22 = {1, 2, 3}
set32 = set12 | set22
print(set32)
#You can use the | operator instead of the union() method, and you will get the same result.

#3
#Join multiple sets with the union() method:
set13 = {"a", "b", "c"}
set23 = {1, 2, 3}
set33 = {"John", "Elena"}
set43 = {"apple", "bananas", "cherry"}

myset = set13.union(set23, set33, set43)
print(myset)

#The  | operator only allows you to join sets with sets, 
# and not with other data types like you can with the  union() method.
# Both union() and update() will exclude any duplicate items.