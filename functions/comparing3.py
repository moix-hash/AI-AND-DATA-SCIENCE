def compare(a , b , c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c >b):
        return c
    
print(compare(5,190,432))
print(compare(50,10,3))
print(compare(50,50,90))    