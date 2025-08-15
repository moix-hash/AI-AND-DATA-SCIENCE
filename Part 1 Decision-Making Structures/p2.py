#taking inputs of the two numbers 
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
# comparing two number to check which one is greater
if (num1>num2):
    print("The first number is greater than the second number : ",num1)
elif(num1<num2):
    print("The second number is greater than the first number : ",num2)
else:
    print("Both of them are equal  : ", num1 , "and" , num2 )
    