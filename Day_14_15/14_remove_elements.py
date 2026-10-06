

#Remove Elements from array

class Solution:
    def removeElement(self, nums, val):

        k = 0

        for i in range(len(nums)):

            if nums[i] != val:
                nums[k] = nums[i]
                k = k + 1

        return k

nums = [3, 2, 2, 3,4,5,3,3,3,3,3,5]
val = 3

class_instance = Solution()
k = class_instance.removeElement(nums, val)

print("k =", k)
print("nums =", nums)
print("after removal =", nums[:k])
print(nums)