
from typing import List
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        hashSet = set(nums)
        for n in nums:
            if (n+diff) in hashSet and (n + diff*2) in nums:
                count += 1

        return count