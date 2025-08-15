#taking three input and find the largest number
num1 = int(input("Enter the first number : " ))
num2 = int(input("Enter the second number : " ))
num3 = int(input("Enter the third number : " ))
# comparing three numbers to find the largest
if (num1>num2) and (num1>num3):
 print("The first number is the largest : ",num1)
elif (num2>num1) and (num2>num3):
 print("The second number is the largest : ",num2)    
else:
  print("the third number is the largest : ",num3)
  