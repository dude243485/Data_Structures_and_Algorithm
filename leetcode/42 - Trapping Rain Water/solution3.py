from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        #compute max left for each position
        
        n = len(height)
        maxLeft = [0]*n
        curr_max = height[0]
        
        for i in range(1, n):
            curr_max = max(curr_max, height[i - 1])
            maxLeft[i] = curr_max
            
        #compute max right for each position
        maxRight = [0] * n
        curr_max = height[-1]
        for i in range(n-2, 0, -1):
            curr_max = max(curr_max, height[i + 1] )
            maxRight[i] = curr_max
        
        #solve the problem
        res = 0
        for i in range(1, n-1): #last and first positions cannot hold water
            unit = min(maxLeft[i], maxRight[i]) - height[i]
            if not unit < 0:
                res += unit
        return res
    

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
test = Solution()
print(test.trap(height))