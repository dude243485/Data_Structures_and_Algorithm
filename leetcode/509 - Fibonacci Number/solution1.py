class Solution:
    def fib(self, n: int) -> int:
        if n <= 2:
            return 1
        return self.fib(n-1) + self.fib(n-2)
    

test = Solution()
print(test.fib(2))
        