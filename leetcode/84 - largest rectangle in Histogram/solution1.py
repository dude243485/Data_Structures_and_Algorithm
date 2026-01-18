from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        stack = []
        max_area = 0
        
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                c_height, index = stack.pop()
                width = i - index
                area = c_height * width
                max_area = max(max_area, area)
                start = index
            stack.append((height, start))
            
        while stack:
            c_height, index = stack.pop()
            width = length - index
            max_area = max(max_area, c_height * width)
        
        return max_area
    

heights = [2,1,5,6,2,3]
test = Solution()
print(test.largestRectangleArea(heights))