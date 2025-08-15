number = int(input("Enter a number: "))
lower_limit = 20   # inclusive
upper_limit = 40   # exclusive

if number >= lower_limit:
    
    if number < upper_limit:
        print(f"{number} lies in the range {lower_limit} to {upper_limit} (exclusive).")
    else:
        print(f"{number} is greater than or equal to {upper_limit}, so it's outside the range.")
else:
    print(f"{number} is less than {lower_limit}, so it's outside the range.")

