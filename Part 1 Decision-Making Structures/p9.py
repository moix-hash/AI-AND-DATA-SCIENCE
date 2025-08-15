number = int(input("Enter the number : "))
if(number %2 == 0 and number %3 ==0):
    print("Number is divisible by both 2 and 3")
elif(number %2 == 0 and number %3 !=0):
    print("Number is divisible by 2 but not buy 3 ")
elif(number %2 !=0 and number %3 ==0):
    print("Number is divisible by 3 but not by 2") 
else:
    print("Number is not divisible by both 2 and 3 ")
         