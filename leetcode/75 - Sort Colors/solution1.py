from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
       
        n = len(nums)
        l, i, r = 0, 0, n - 1

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:  
                i += 1


nums = [2, 0, 1]
test = Solution()
test.sortColors(nums)
print(nums)
                    