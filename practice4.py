# 1.Store following word meanings in a python dictionary:
# dict = {
#     "table": ["a piece of furniture", "list of facts & figures"],
#     "cat" : "a small animal"
# }

# print(dict)

# 2.You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classeooms are needed by all students.
# student = {"python","java","C++","python","javascript","java","python"
#            ,"java","C++","C"}
# print(len(student))

# 3.WAP to enter marks of 3 subjects from the user and store them in a dictionary
# . Satrt with an empty dictionary & add one by one . Use subject name as key & marks as value .
# marks ={}

# x = int(input("Enter phy marks :")),
# marks.update({"phy" :x})
# y = int(input("Enter chem marks :")),
# marks.update({"chem" :y})
# z = int(input("Enter math marks:"))
# marks.update({"math" :z})


# print(marks)

# 4. figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built in data types)

# values = {9,"9.0"}
# print(values)


values ={
    ("float",9.0),
    ("int",9)
}
print(values)