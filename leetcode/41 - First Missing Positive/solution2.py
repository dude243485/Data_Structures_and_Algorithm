from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        hashSet = set(nums)

        if 1 not in hashSet:
            return 1

        n = len(nums)
        for i in range(1, n+2):
            if i not in hashSet:
                return i
                
            
    

nums = [1,2,0]
test = Solution()
answer = test.firstMissingPositive(nums)
print(answer)