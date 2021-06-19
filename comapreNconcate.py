#compare and cancate two strings
str1=str(input("enter first string"))
str2=str(input("enter second string"))

concate = str1 + str2
print(concate)
if(str1>str2):
    print("string1 is greater")
elif (str1==str2):
    print("string1 and string2 are equal")
else:
    print("string 2 is greater")