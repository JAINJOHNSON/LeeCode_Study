# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.



class max_Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:

            current_sum = max(num, current_sum + num)

            max_sum = max(max_sum, current_sum)

        return max_sum

nums = [-3, 5, -10, 4,9]

class_instance = max_Solution()

solution = class_instance.maxSubArray(nums)
print(solution)