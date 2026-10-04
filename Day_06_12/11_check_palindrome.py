


class Solution:
    def isPalindrome(self, s):

        
        clean = ""

        for char in s.lower():
            if char.isalnum():
                clean = clean + char

        
        reverse = clean[::-1]
        return clean == reverse



s = "A man, a plan, a canal: Panamas"

class_instance = Solution()
result = class_instance.isPalindrome(s)

print("is palindrome :",result)
