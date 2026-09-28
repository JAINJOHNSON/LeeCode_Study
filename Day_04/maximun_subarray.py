# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


nums = [-2,1,-3,4,-1,2,1,-5,4]
sorted_array = sorted(nums,reverse=True)
print(sorted_array)

new_array = []

for item in sorted_array:
    if item >0 :
        new_array.append(item)

print("New array :: ",new_array)
print("Array Sum ::",sum(new_array))