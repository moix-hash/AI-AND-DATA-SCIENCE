def check_prime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):  
            if num % i == 0:
                return f"{num} is not a prime number"
        return f"{num} is a prime number"
    else:
        return f"{num} is not a prime number"

print(check_prime(11))   
print(check_prime(15))   
print(check_prime(1))    
print(check_prime(2))    
