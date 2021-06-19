#summin,counting,averaging of numbers using looping
lst=[]
sum=0
avg=0

n= int(input("enter number of elements:"))
count=n
for i in range(0,n):
    e = int(input())

    sum = sum + e
    lst.append(e)
avg=sum/n
print("List of numbers you have enterd is")
print(lst)
print("The sum of "+str(n)+" numbers is"+str(sum))
print("The average of "+str(n)+"numbers is"+str(avg))
print("The count is "+str(count))

