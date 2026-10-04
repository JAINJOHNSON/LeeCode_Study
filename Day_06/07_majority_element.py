


class Solution:
    def majorityelement(self, nums):

        for i in nums:
            count = 0

            for j in nums:
                if i == j:
                    count += 1

            if count > len(nums) // 2:
                return i


nums = [2, 2, 1, 1, 1, 2, 2]

class_instance = Solution()
answer = class_instance.majorityelement(nums)

print("Majority Element :",answer)
