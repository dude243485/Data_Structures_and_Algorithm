class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashSet = set()
        res = []
        for n in nums:
            if n in hashSet:
                res.append(n)
            if len(res) == 2: 
                return res
            hashSet.add(n)
        return res