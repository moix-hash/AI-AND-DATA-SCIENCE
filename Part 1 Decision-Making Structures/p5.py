age = int(input("Enter your age :"))
if (age>=18 and age <=60):
    print("You are an adult ")
elif(age<18 and age>0):
    print ("You are a minor ")
elif(age>60):
    print("You are a senior citizen ")
else:
    print("Invalid age entered")