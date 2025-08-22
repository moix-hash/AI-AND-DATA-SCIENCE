def fact(num):
    if num <0:
        return "Factorial is not defined for negative numbers"
    elif num==0 or num==1:
        return 1
    else:
        return fact(num-1)*num
print(fact(5))        