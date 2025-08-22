Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

# a) Separate strings and numbers
strings = [x for x in Gadgets if isinstance(x, str)]
numbers = [x for x in Gadgets if isinstance(x, (int, float))]

# b) Sort strings ascending & descending
asc_strings = sorted(strings)
desc_strings = sorted(strings, reverse=True)

# c) Sort strings by length
length_sorted = sorted(strings, key=len)

# d) Sort numbers ascending & descending
asc_numbers = sorted(numbers)
desc_numbers = sorted(numbers, reverse=True)

print("Strings:", strings)
print("Numbers:", numbers)
print("Ascending Strings:", asc_strings)
print("Descending Strings:", desc_strings)
print("Strings Sorted by Length:", length_sorted)
print("Ascending Numbers:", asc_numbers)
print("Descending Numbers:", desc_numbers)
