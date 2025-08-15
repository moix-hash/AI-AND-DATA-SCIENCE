num1 = int(input("Enter first number : "))
num2 = int(input("Enter the second number :"))
operator = input("Enter an operator (+,-,*,/) : ")
if(operator =="+"):
   print("Sum of the two number is  :",num1 + num2 )
elif(operator =="-"):
    print("Difference of the two of the two numbers is  : ",num1 - num2)
elif(operator =="*"):
    print("Product of the two numbers is : ",num1 *num2)
elif(operator == "/"):
    print("Division of the two numbers is : " , num1 / num2)
else:
    print("Invalid operator")
        