from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_left = []
        c_max_l = 0
        for i in range(len(height)):
            max_left.append(c_max_l)
            if height[i] > c_max_l:
                c_max_l = height[i]
   
        max_right = [0] * len(height)
        c_max_r = 0    
        for i in range(len(height)-1, -1, -1):
            max_right[i] = (c_max_r)
            if height[i] > c_max_r:
                c_max_r = height[i]
                
                
        total_unit = 0
        for i in range(len(height)):
            unit = min(max_left[i], max_right[i]) - height[i]
            if unit < 0: unit = 0
            
            total_unit += unit
        
        return total_unit
            
            
        
    
    
input_data = [0,1,0,2,1,0,1,3,2,1,2,1]        
test = Solution()
print(test.trap(input_data))