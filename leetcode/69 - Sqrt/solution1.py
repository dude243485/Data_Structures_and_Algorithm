class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1:
            return 1

        mid = x//2
        while mid**2 > x:
            mid = mid//2
        
        while (mid + 1)**2 <= x:
            mid = mid + 1
        return mid
        