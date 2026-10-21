




class Solution:
    def findMaxAverage(self, nums, k):

        # Sum of the first k elements
        current_sum = sum(nums[:k])

        max_sum = current_sum

        # Start checking the next windows
        for i in range(k, len(nums)):

            current_sum = current_sum - nums[i - k] + nums[i]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum / k



nums = [1, 12, -5, -6, 50, 3]
k = 4

class_instance = Solution()
result = class_instance.findMaxAverage(nums, k)

print(result)
