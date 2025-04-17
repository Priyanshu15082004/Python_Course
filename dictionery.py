# Dictionaries are used to store data values in key.value pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys

# info ={
#     "key" : "value",
#     "name" : "apnacollege",
#     "learning": "coding",
#     "subjects":["python","C","Java"],
#     "topics":("dict","set"),
#     "age" : 35,
#     "is_adult" : True,
#     "marks" :94.4

# }

# # null_dict = {} #Also add null dictionary
# # null_dict["name"] ="Priyanshu"
# # print(null_dict)
# info["name"] = "Priyanshu"
# info["surname"] ="Chauhan"
# print(type(info))
# print(info["key"])
# print(info["subjects"])
# print(info)


# -----------Nested Dictionaries-------------------
# student ={
#     "name" :"priyanshu chauhan",
#     "subjects":{
#         "phy": 97,
#         "chem":76,
#         "maths":80
#     }
# }
# print(student["subjects"]["chem"])
# print(student)


# ----------Dictionary Methods---------
# student ={
#     "name" :"priyanshu chauhan",
#     "subjects":{
#         "phy": 97,
#         "chem":76,
#         "maths":80
#     }
# }
# print(list(student.keys()))# returs all keys
# print(len(list(student.keys())))# returns length
# print(list(student.values())) #returns all values
# pairs = print(list(student.items())) #returns all (key,val) pairs as tuples
# print(pairs[0])
# print(student.get("name"))#returns the key according to value 
# print(student["name2"])#error
# print(student.get("name2"))# print None

# student.update({"city" : "delhi" ,"age" :16})# inserts the specified items to the dictionary
# print(student)


