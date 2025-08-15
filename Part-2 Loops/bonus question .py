# First two Fibonacci numbers
a, b = 0, 1

print("First 10 Fibonacci numbers:")

for _ in range(10):
    print(a, end=" ")  # print current number
    a, b = b, a + b    # update values for next number
