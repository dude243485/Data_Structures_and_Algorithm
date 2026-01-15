from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted = nums.copy()
        sorted.sort()
        
        n = len(sorted)
        map = {}
        map[sorted[0]] = 0    
        for i in range(1, n):
            if sorted[i- 1] != sorted[i]:
                map[sorted[i]] = i
            
                
        output = []
        for i in range(n):
            output.append(map[nums[i]])
            
        return output       
        
        

nums =  [8,1,2,2,3]
test = Solution()
print(test.smallerNumbersThanCurrent(nums))