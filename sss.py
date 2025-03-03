import json 

data = {"name:" : "kahnshaiiym" , "age: " : 18 , "grade: " :2}

# json_string = json.dumps(data)

# pthon_dict = json.loads(data)

with open ("students.json"  , "w") as file :
    json.dump(data , file)
    
with open ("students.json" , "r") as file :
    tetxt = json.load(file)
    print(tetxt)