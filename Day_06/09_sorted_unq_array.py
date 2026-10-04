


class Solution:
    def removeDuplicates(self, nums):

        unique = []

        for i in nums:
            if i not in unique:
                unique.append(i)

        
        return len(unique)


nums = [0,0,1,1,1,2,2,3,3,4]

class_instance = Solution()
answer = class_instance.removeDuplicates(nums)
print("Input Array :",nums)
print("no of unique numbers :",answer)
unwanted_slots = len(nums) - answer
print("remaining slots :",unwanted_slots)

uniq_array_set = list(set(nums))
print("Uniq list :",uniq_array_set)
for i in range(0,unwanted_slots):
    a = '_'
    uniq_array_set.append(a)

print(" list :",uniq_array_set)

