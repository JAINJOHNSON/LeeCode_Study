class Solution:
    def sortedSquares(self, nums):

        result = []

        for num in nums:
            result.append(num * num)

        result.sort()

        return result



nums = [-4, -1, 0, 3, 10]

class_instance = Solution()
result = class_instance.sortedSquares(nums)

print(result)