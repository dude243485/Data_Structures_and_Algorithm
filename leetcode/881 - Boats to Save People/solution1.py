from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        boats = 0
        l , r = 0, n-1
        while l < r:
            sum = people[l] + people[r]
            if sum <= limit:
                l += 1
            boats += 1
            r -= 1
                
        if l == r: boats += 1
        return boats
        
        
            


        
            

