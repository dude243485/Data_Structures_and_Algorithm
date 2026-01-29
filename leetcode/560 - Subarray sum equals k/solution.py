from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res =0
        curSum = 0
        map = { 0 : 1 }
        
        for n in nums:
            curSum += n
            diff = curSum - k
            
            res += map.get(diff, 0)
            map[curSum] = 1 + map.get(curSum, 0)
        
        return res
        
    

nums = [1, 1, 1]
k = 2
test = Solution()
answer = test.subarraySum(nums, k)
print(answer)