from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        hashSet = set(letters)
        for i in range(ord("a"), ord("z") + 1):
            if i > ord(target) and chr(i) in hashSet:
                return chr(i)
        
        return letters[0]
        
        
    
target = "a"
letters = ["c","f","j"]
test = Solution()
answer = test.nextGreatestLetter(letters, target)
print(answer)