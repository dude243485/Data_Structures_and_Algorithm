
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.prefix = [0]*len(nums)
        self.sum = 0
        for i in range(len(nums)):
            self.sum += nums[i]
            self.prefix[i] = self.sum
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)