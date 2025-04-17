# 1.WAP to ask the user to enter names of their 3 favorite movies & store them in a list 
# movies= []
# mov1 =input("enter 1st movie:") #Second method = movies.appendinput("enter 1st movie:")
# mov2 =input("enter 2nd movie:")
# mov3 =input("enter 3rd movie:")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# 2. WAP to check if a list contains a palindrome of elements .(Hint: use copy() method)
# Palindrome - [1,2,3,2,1] [1,"abc","abc",1] ["ma'am"]  ["racecar"] - In this the same number of element are shown in same order

# list1 = [1,2,1]
# list2 = [1,2,3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("NOT palindrome")    

# 3.WAP to count the number of students with the "A" grade in the following tuple.
# tup = ("C","D","A","A","B","B","A")
# print(tup.count("A"))

# 4.Store the above values in a list & sort then from "A"to "D"
grade = ["C","D","A","A","B","B","A"]
print(grade.sort())
print(grade)