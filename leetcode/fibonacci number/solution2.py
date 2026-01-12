
"""Memoization approach"""
class Solution:
    memo = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n in self.memo:
            return self.memo[n]
            
        if n <= 1:
            return n
        else:
            result = self.fib(n-1) + self.fib(n-2)
        
        self.memo[n] = result
        return result
    

test = Solution()
print(test.fib(50))
        