from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        for i in range(1, len(grid)):
            grid[0].extend(grid[i])
        
        res = [0]*2
        hashSet = set()
        
        for n in grid[0]:
            if n in hashSet:
                res[0] = n
            hashSet.add(n)

        for i in range(1, len(grid[0]) + 1):
            if i not in hashSet:
                res[1] = i

        return res


        