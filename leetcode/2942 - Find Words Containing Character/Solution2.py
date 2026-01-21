from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
                
        return res
        
        
words = ["leet","code"] 
x = "e" 
test = Solution()
print(test.findWordsContaining(words, x))