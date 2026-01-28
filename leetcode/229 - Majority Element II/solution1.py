from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #hash table solution
        map = {}
        res = set()
        threshold = len(nums) // 3
        for num in nums:
            map[num] = map.get(num, 0) + 1
            if map[num] > threshold:
                res.add(num)
        return list(res)
        

nums = [3,2,3]
test = Solution()
print(test.majorityElement(nums))