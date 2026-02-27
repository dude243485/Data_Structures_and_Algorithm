class Solution:
    def makeSmallestPalindrome(self, s: str) -> str :
        l , r = 0, len(s) - 1
        count = 0
        res = list(s)
        while l < r:
            
            if s[l] != s[r]:
                minPos = min(ord(s[l]), ord(s[r]))
                res[l] = chr(minPos)
                res[r] = chr(minPos)
                count += 1
            l += 1
            r -= 1
                           
            
        return "".join(res)
   
s = "egcfe" 
test = Solution()
print(test.makeSmallestPalindrome(s))