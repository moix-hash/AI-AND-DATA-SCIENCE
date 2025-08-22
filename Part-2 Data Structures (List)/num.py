nums = [32, 54, 66, 11, 77, 10, 90]

# a) Remove items less than 20
nums = [x for x in nums if x >= 20]

# b) Sort ascending and descending
asc = sorted(nums)
desc = sorted(nums, reverse=True)

# c) Compute average
average = sum(nums) / len(nums)

print("Filtered List:", nums)
print("Ascending:", asc)
print("Descending:", desc)
print("Average:", average)
