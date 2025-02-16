import json

with open("lab4/jsonn/sample-data.json" , 'r') as file :
    data= json.load(file)

# interfaces = data["imdata"]

# print("Interface Status")
# print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<5}")
# print("-"*80)

# for i in interfaces:
#     interface = i["l1PhysIf"]["attributes"]
#     dn = interface["dn"]
#     description = interface.get("descr" ,"")
#     speed = interface.get("speed" , "inherit")
#     mtu = interface.get("mtu" , "")
    
# print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<5}")
 

print("Interface Status")
print("=" * 85)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU'}")
print("-" * 85)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else ""  # Пустая строка, если нет описания
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu}")