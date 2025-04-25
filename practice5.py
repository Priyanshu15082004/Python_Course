# 1.Print numbers from 1 to 100

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# 2.Print numbers from 100 to 1

# i = 100
# while i >= 1: #stoping condition
#     print(i)
#     i -= 1

# 3.Print the multiplication table of a number n.
# n = int(input("enter number :"))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# 4.Print the elements of the following list using a loop.
# nums = [1,4,9,16,25,36,49,64,81,100]
# heroes =["ironman","Thor","Superman","Batman"]

# idx = 0
# while idx < len(nums):
#     print(nums[idx]) #nums[0],  nums[1], nums[2]....
#     idx += 1

# idx = 0
# while idx < len(heroes):
#     print(heroes[idx]) #heroes[0],  heroes[1], heroes[2]....
#     idx += 1    
    
# 5. Search for a number x in this tuple using loop

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 36

# i = 0 # initialization
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at idx", i)
#         break
#     else:
#         print("finding..")    
#     i += 1
# print("end of loop")    


# Using for loop
# 6.Print the elements of the following list using a loop
# nums = [1,4,9,16,25,36,49,64,81,100]

# for val in nums:
#     print(val)

# 7. Search for a number x in this tuple using loop

# nums = (1,4,9,16,25,36,49,64,81,100,49)
# x = 49

# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx", idx)
#         break
#     idx +=1

# using for & range()

# 8. Print numbers from 1 to 100.
# for i in range (1,101):
#     print(i)

# 9. Print number from 100 to 1.
# for i in range (101,0,-1):
#     print(i)

# 10. Print the multiplication table of a number n.
# n = int(input("enter number:"))

# for i in range(1,11):
#     print(n* i)

# 11. WAP to find the sum of first n numbers. (using while )
# n = 8
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("total sum=" ,sum)

# 12.WAP to find the factorial of first n numbers.(using for )
# n = 4
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("factorial =" ,fact)    



n = 4 
fact = 1 
for i in range (1, n+1):
    fact *= i
print("factorial =" ,fact)    
