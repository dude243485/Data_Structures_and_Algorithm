class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m = str(n)
        product = 1
        for digit in m:
            product *= int(digit)

        sum = 0
        for digit in m:
            sum += int(digit)

        return product - sum 

        