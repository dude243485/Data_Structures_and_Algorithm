class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        map = {}
        res = set()
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
                    res.add(f'{nums[l]},{target},{nums[r]}')
                    break
                    
          sol = []
          res = list(res)
          for j in res:
              sol.append(j.split(","))
          return sol
                    
        
