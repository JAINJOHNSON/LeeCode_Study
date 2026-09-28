# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

nums = [0,1,0,3,12]
print("input :: ",nums)

w_index = 0

for r_index in range(len(nums)):
    print (r_index)
    if nums[r_index] != 0:
        nums[r_index],nums[w_index] = nums[w_index],nums[r_index]
        w_index = w_index + 1

    print(f"after {r_index} loop ::",nums)