from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        l = 0
        r = len(letters) - 1
        
        while l <= r:
            mid = (l+r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return letters[l] if l < len(letters) else letters[0]
        
            
       
        
        
    
target = "a"
letters = ["c","f","j"]
test = Solution()
answer = test.nextGreatestLetter(letters, target)
print(answer)