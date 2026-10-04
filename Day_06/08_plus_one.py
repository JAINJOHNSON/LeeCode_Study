
class Solution:
    def plusOne(self, digits):

        num = 0

        for i in digits:
            num = num * 10 + i

        num = num + 1

        result = []

        for i in str(num):
            result.append(int(i))

        return result


digits = [1, 8, 9]

class_instance = Solution()
answer = class_instance.plusOne(digits)

print("Plus one array : ",answer)
