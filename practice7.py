
# 1. Create a new file "practice.txt" using Python. Add the following data in it .
# f = open("practice.txt", "w")
# f.write("Hi everyone\n we are learning File I/O\nusing Java.\n I like programming in Java.")
# f.close()

# 2. WAF that replaces all occurances of "Java" with "Python" in above file
# f = open("practice.txt", "r")
# data = f.read()
# new_data = data.replace("Java","Python")
# print(new_data)
# f = open("practice.txt", "w")
# f.write(new_data)
# f.close()

# 3 Search If the word "learning " exists in the file or not.

# def check_for_word():
#     word = "learning"
#     f = open("practice.txt", "r")
#     data = f.read()
#     if(word in data):
#         print("found")
#     else:
#         print("not found")    
# check_for_word()   


# 4. WAF to find in which line of the file does the word "learning" occur first.
# Print -1 if word not found 
# def check_for_line():
#     word = "programming"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1    
#     return - 1
# print(check_for_line())

# 5.From a file containing numbers separated by comma, print the count of even numbers.
# with open("practice.txt","r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(num)
#             num =""
#         else:
#             num += data[i]    


# 2nd method 
count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)            