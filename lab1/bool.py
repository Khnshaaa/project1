x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#2
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))