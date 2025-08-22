student = ["Moiz", 20, "AI and Data Science", True]

strings = []
numbers = []
booleans = []

for item in student:
    if isinstance(item, str):
        strings.append(item)
    elif isinstance(item, bool): 
        booleans.append(item)
    elif isinstance(item, (int, float)): 
        numbers.append(item)

print("Strings:", strings)
print("Numbers:", numbers)
print("Booleans:", booleans)
