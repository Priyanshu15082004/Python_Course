# ----String is data type that stores a sequence of characters.

# str1 ="this is a string."
# str2 ='This is '
# str3 = """this is a string"""

# ----escape sequence character \n - next line 
                    # ------  \t - Tab
# str1 = "This is a string.\n we are creating it in python. "
# print(str1)


# -----Basic Operations 
# ---Concatenations

# str1 ="apna"
# len1 = len(str1)
# print(len1)
# str2 = "College"
# len2 = len(str2)
# print(len2)
# final_str = str1 + " "+str2
# print(final_str)
# print(len(final_str))


# -------Indexing - position

# str = "apna college"
# ch = str[0]
# print(ch)


#------- Slicing - Accesing parts of a string 

# str = "apna college"
# print(str [1:4])
# print(str[:4])#[0:4]
# print(str[5: len(str)])
# print(str[5:]) #[5: len(str)]

# ----Negative Index

# str = "apple"
# print(str[-5:-1])

# ------ Functions 

str ="i am studying python from ApnaCollege"
print(str.endswith("ege")) # returns true if string ends with substr
print(str.capitalize()) # capitalizes 1st char
str = str.capitalize()
print(str.replace("o","a"))# replaces all occurences of old
print(str.find("o"))#returns 1st index of 1st occurrer
print(str.count("o"))# counts the occurance of substr
