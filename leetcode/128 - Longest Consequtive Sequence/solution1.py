from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashSet = set(nums)
        
        maxCount = 0
        for n in nums:
            if (n - 1) not in hashSet:
                count = 1
                current = n 
                while current + count in hashSet:
                    count += 1
                maxCount = max(maxCount, count )
                
        return maxCount
        

nums = [100,4,200,1,3,2]
test = Solution()
answer = test.longestConsecutive(nums)
print(answer)