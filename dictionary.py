seen = {}  # dictionary is a collection which is ordered, changable and do not allow duplicates
seen = {1:"janan", "name": "Zhu"}
print(seen)
print(seen["name"])
print(len(seen))
print(type(seen))
print(type(3))

x = seen.keys()  
print(type(x))           # type of keys: dict_keys
seen["name"] = "Zyu"
print(x)

# add a new item to the list:
seen["color"] = "red"
print(seen)
if "name" in seen:
    print("you have learn the basic of python dictionary")