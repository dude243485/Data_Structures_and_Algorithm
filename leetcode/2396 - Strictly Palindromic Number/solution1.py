class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        #helper function
        def convert(n , b):
            quotient = n
            remainder = ""
            
            while quotient > 0:
                remainder += str(quotient % b)
                quotient = quotient // b    
            return remainder[::-1]

        
        for b in range(2, n-1):
            string = convert(n, b)
            print(string)
            if string != string[::-1]:
                return False
            
        return True

        