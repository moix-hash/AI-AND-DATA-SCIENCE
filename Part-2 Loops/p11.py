# Initialize sums
even_sum = 0
odd_sum = 0

# Loop through numbers from 1 to 50
for i in range(1, 51):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

# Print results
print(f"Sum of even numbers from 1 to 50: {even_sum}")
print(f"Sum of odd numbers from 1 to 50: {odd_sum}")

