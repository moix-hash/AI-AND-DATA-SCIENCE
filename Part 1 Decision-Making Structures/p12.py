#program in celsius too check the temperature
temperature = float(input("Enter the temperature in celsius: "))
if(temperature < 0):
    print(f"the weather is frezzing at {temperature} degree celsius")
elif(temperature >= 0 and temperature < 26):
    print(f"The weather is moderate at {temperature} degree celsius ")
elif(temperature >=26):
    print(f"The weather is hot at {temperature} degree celsius")
else:
    print("Invalid input")        
       
