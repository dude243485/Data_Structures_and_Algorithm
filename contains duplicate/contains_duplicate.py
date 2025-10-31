from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = list(set(nums))
        for i in range(len(nums)):
            if nums[i] in no_duplicates:
                no_duplicates.remove(nums[i])
                
            else:
                return True
            
        return False
        
    
  
  

nums = [1, 2, 3, 3]
test = Solution()
print(test.hasDuplicate(nums))