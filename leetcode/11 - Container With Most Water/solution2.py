from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxArea = 0
        l, r = 0, n-1

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            maxArea = max(maxArea, w*h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea

height = [1,8,6,2,5,4,8,3,7]   
test = Solution()
print(test.maxArea(height))
