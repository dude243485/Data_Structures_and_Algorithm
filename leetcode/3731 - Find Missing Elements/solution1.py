from typing import List
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        hashSet = set(nums)
        res = []
        maxNum = max(nums)
        minNum = min(nums)

        for n in range(minNum, maxNum):
            if n not in hashSet:
                res.append(n) 
        
        res.sort()
        return res