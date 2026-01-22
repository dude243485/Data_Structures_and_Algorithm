class Solution:
    def minTimeToType(self, word: str) -> int:
        initial = "a"
        res = 0
        n = len(word)
        for i in range(n):
            diff = abs(ord(word[i]) - ord(initial))
            res += min(diff + 1, (26 - diff) + 1)
            initial = word[i]
            
        return res
    
    
    
s = "abc"
test = Solution()
print(test.minTimeToType(s))