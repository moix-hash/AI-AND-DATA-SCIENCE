def checkage(age):
    if (age < 18):
       return " You are a minor."
    elif(age >=18 and age <60):
        return " You are an adult."
    else:
        return " You are a Senior Citizen."
    
print(checkage(16))
print(checkage(56))       
print(checkage(89))   