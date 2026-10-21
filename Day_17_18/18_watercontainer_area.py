









class Solution:
    def maxArea(self, height):

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:

            width = right - left

            
            water_height = min(height[left], height[right])

            area = width * water_height

            if area > max_area:
                max_area = area

            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7,9]
class_instacne = Solution()
result = class_instacne.maxArea(height)

print(result)
