fruits = ["apple", "raspberry", "pineapple", "cherry"]

# a) Check if apple is present
if "apple" in fruits:
    print("Apple is present at index:", fruits.index("apple"))

# b) Replace raspberry and pineapple with orange
fruits[1:3] = ["orange"]

# c) Insert "apricot" at index 2
fruits.insert(2, "apricot")

# d) Extend with other items
fruits.extend(["car", "bike", "aeroplane"])

print("Updated Fruits List:", fruits)
