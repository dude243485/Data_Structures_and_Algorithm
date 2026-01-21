from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        pos = 0

        for i in range(n):
            if nums[pos] == val:
                nums.pop(pos)
                nums.append("_")
                count += 1
                
            else:
                pos += 1
                
                
        print(nums)
        print(count)
        return n - count
    

nums = [3,2,2,3]
val = 3
test = Solution()
print(test.removeElement(nums, val))