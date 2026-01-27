from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Convert to set for O(1) lookup
        num_set = set(nums)
        max_length = 0
        
        # Only start counting from the beginning of each sequence
        for num in num_set:
            # Check if this is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length

nums = [100,4,200,1,3,2]
test = Solution()
answer = test.longestConsecutive(nums)
print(answer)