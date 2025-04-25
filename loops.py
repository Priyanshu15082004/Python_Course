# Loops are used to repeat instructions.

# count = 1
# while count <= 5 :
#     print("Hello")
#     count += 1
# print(count)    


# i = 1
# while i <= 10 :
#     print("College",i)
#     i += 1
    

# print numbers from 1 to 5
# i = 1
# while i <=5:
#     print(i)
#     i +=1
# print("Loop ended")   

# ---------------------------------------------------
# BREAK & CONTINUE
# Break : used to terminate the loop when encountered
# Continue: terminates execution in the current iteration & continues execution of the loop
# with the next iteration

# ---Break-----
# i = 1
# while i <=5:
#     print(i)
#     if(i== 3):
#         break
#     i +=1
# print("Loop ended")   


# ---Continue----
# i = 1
# while i <= 10:
#     if(i%2 == 0):# odd
#         i += 1
#         continue # skip
#     print(i)
#     i +=1


#--- Loops are used for sequential traversal. For traversing list,string,tuples etc.
# nums =[1,2,3,4,5]
# for val in nums:
#     print(val)

# veggies = ["potato","brinjal","ladyfinger","cucumber"]

# for val in veggies:
#     print(val)


# tup =(1,2,3,4,5)
# for val in tup:
#     print(val)



# str ="apnacollege"

# for char in str:
#     if(char == "o"):
#         print("o found")
#         break
#     print(char)
# else:
#     print("END")    

# -----------------RANGE()-------------------------
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 
# 1(by default),and stops before a specified number.

# seq = range(5)
# for i in seq:
#     print(i)



# for i in range(10): #range(stop)
#     print(i)

# for i in range(2,10):#range(start, stop)
#     print(i)

# for i in range(2,10,2):#range(start, stop,step)
#     print(i)

# for i in range(2,101,2): # for print even no.
#     print(i)

# for i in range(1,100,2):
#     print(i)


# Pass Statement 
# pass is a null statement that does nothing . It is used as a placeholder for future code.

# for i in range(5):
#     pass
# print("some useful work")
