class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for i in s:
            if i.isalnum(): new_string += i.lower() 
           
        for i in range(int(len(new_string))):
            if (new_string[i] != new_string[len(new_string) -i -1]):
                return False
        return True
        
        
  
input_data = "A man, a plan, a canal: Panama"        
test = Solution()
answer = test.isPalindrome(input_data)
print(answer)