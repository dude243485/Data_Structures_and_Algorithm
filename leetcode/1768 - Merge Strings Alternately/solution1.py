class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        res = ""
        i = 0
        while i < n:
            res += word1[i]
            res += word2[i]
            i += 1
        
        for j in range(i, len(word1)):
            res += word1[j]
            
        for j in range(i, len(word2)):
            res += word2[j]
        
        return res
            


word1 = "abc"
word2 = "pqr"
test = Solution()
answer = test.mergeAlternately(word1, word2)
print(answer)