







class Single_number:
    def singleNumber(self, nums):

        for i in nums:
            count = 0

            for j in nums:
                if i == j:
                    count += 1

            if count == 1:
                return i


nums = [4, 1, 2, 3, 4, 1, 2]

class_instance = Single_number()
answer = class_instance.singleNumber(nums)

print("single Numbe :",answer)
