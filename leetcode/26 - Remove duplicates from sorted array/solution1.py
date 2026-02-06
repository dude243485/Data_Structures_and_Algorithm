from typing import List
 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        r = 1
        l = 0

        while r < (n) and nums[r] != "-":
            while nums[l] == nums[r] and nums[r] != "_":
                nums.pop(r)
                nums.append("_")
                count += 1
            print("inner nums: ", nums)
            l += 1
            r = l + 1
        return n - count

nums = [1, 1]
test = Solution()
print(test.removeDuplicates(nums))
print( nums )