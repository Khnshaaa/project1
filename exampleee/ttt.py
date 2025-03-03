import re 
text = "my name is khanshaiym and i love apple bannans apricot avacado age 17 18  example@gmail.com"
# pattern = r"\ba\w*"
# pattern = r"\d+"

# matches = re.findall(pattern , text)
# print (matches )

# pattern = r"\s"
# newtext = re.sub(pattern  , "-" ,text)
# print (newtext)


pattern  = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
matches = re.findall(pattern , text)
print(matches)

