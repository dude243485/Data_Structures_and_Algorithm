from typing import List

"""two pointer solution"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
            
            
                   
        
     
input_data = [4,2,0,3,2,5]        
test = Solution()
print(test.trap(input_data))