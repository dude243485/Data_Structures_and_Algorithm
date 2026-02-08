
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        for i in range(len(nums)):
            target = -nums[i]
            l, r = 0,len(nums) - 1
            while l < r:
                if l == i:
                    l += 1
                    continue 
                elif r == i:
                    r -= 1
                    continue 
                
                sum = nums[l] + nums[r]
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    # res.add(f'{nums[l]},{nums[i]},{nums[r]}')
                    ans = [nums[l], nums[i], nums[r]]
                    ans.sort() #sort to check
                    if ans not in res:
                        res.append(ans)
                    break
                    
       
        return res
    

nums = [-1,0,1,2,-1,-4]
test = Solution()
answer = test.threeSum(nums)
print(answer)
                    
        
