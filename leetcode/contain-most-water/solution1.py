from typing import List
"""This was solved using a two-pointer approach, figure it out"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        left = 0
        right = n -1
        
        while (left < right):
            area = min(height[left], height[right]) * (right - left)
            if (area > max_area):
                max_area = area
                
            if (height[left] < height[right] ):
                left += 1
            else:
                right -= 1
        
        return max_area
 
   
input_data = [1,8,6,2,5,4,8,3,7]        
test = Solution()
print(test.maxArea(input_data))