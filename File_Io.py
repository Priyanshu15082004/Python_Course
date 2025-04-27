# Python can be used to perform operations on afile.(read & write data)
# Types of all files
# 1.Text Files: txt, .docx,.log etc.
# Binary Files: .mp4 , .mov, .png, .jpeg etc.


# OPEN, READ & CLOSE FILE
# f = open("priyanshu.txt" ,"r")
# # data = f.read()#reads entire file
# # print(data) 
# line1 = f.readline()# reads line by line 
# print(line1)
# line2 = f.readline()
# print(line2)
# # print(type(data))
# f.close()


# Writing to a File 
# f = open("priyanshu.txt" ,"w")# for writing
# f.write("I want to learn javascript tomorow .123")

# f = open("priyanshu.txt" ,"a")#Append the data in existing file
# f.write("Then i will nove to reactJs""\n After that nodejs")
# f.close()


# f = open("priyanshu.txt","r+" )
# f.write("Here I ")
# print(f.read())
# f.close()



# with open("priyanshu.txt", "r") as f:
#     data = f.read()
#     print(data)


# import os
# os.remove("priyanshu.txt")


