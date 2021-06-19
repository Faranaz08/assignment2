# decimal to binary usingfunction
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2 ,end=' ' )

# decimal number
dec = int(input("enter a decimal number"))

convertToBinary(dec)
print()