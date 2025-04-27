# 1.WAF to print the length of a list.( list is the parameter)
# cities = ["Delhi", "Gurgaon","pune","chennai","Mumbai","noida"]
# heroes =["Thor","ironman","Captain America","Shaktiman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)    
# print_len(heroes)

# 2.WAF to print the elements of a list in a single line.(list is the parameter)

# cities = ["Delhi", "Gurgaon","pune","chennai","Mumbai","noida"]
# heroes =["Thor","ironman","Captain America","Shaktiman"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")    

# print_list(cities)

# 3.WAF to find the factorial of n . ( n is the parameter)


# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)    

# cal_fact(6)

# 4. WAF to convert USD to INR

# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val,"USD =", inr_val, "INR")

# converter(20)

# HOmework question

# n = int(input("Enter a number :"))
# def num_check(n):
#     if (n % 2 == 0):
#         print("Even")
#     else:
#         print("odd")    

# num_check(n)        


# 5 RECURSIVE
# write a rrecursive funtion to calculate the sum of first n natural numbers.
# n = int(input("Enter the number :"))
# def cal_sum(n):
#     if(n==0):
#         return 0
#     return cal_sum(n-1) + n
# sum = cal_sum(n)   
# print(sum) 
    
#6. Write a recursive function to print al elements in a list .
# Hint : use list $ index as parameters.
def print_list(list , idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits = ["MANGO","Litchi","Apple","Banana"] 
print_list(fruits)   
 