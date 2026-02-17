from typing import List
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        minNum = nums[0]
        maxNum = nums[-1]
        res = []
        pointer = 0
        for n in range(minNum, maxNum+1):
            if n != nums[pointer]:
                res.append(n)
                pointer -= 1
            pointer += 1

        return res