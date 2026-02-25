class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        quotient = n
        divisors = [2, 3, 5]
        while quotient > 1:
            curr = quotient
            for n in divisors:
                if quotient % n == 0:
                    quotient = quotient / n
                    break
            if quotient == curr:
                return False
        return True


