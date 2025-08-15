#This program calculates the factorial of a number entered by the user
while True:
    number = int(input("Enter a number (0 or negative to quit): "))
    if number <= 0:
        print("Goodbye!")
        break
    
    factorial = 1
    i = 1
    while i <= number:
        factorial *= i
        i += 1
    
    print(f"Factorial of {number} is {factorial}")

    
        
        