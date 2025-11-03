#In this solution, we'll first sort the string
#then we'll check if all character at each index matches
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            s = sorted(s)
            t = sorted(t)
            if (s != t):
                return False
        return True
        
        
test = Solution()
answer = test.isAnagram("racecar", "carrace")
print(answer)
