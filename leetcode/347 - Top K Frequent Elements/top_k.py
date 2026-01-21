from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            if (i not in map):
                map[i] = 1
                
            else:
                map[i] = map[i] + 1
        
        max_value = 0
        sorted_map = dict(sorted(map.items(), key=lambda item: item[1], reverse=True)) #sort the dictionary
        print(sorted_map)
        
        return list(sorted_map)[:k]
                      
                
            
    
 
input = [1,1,1,2,2,3]   
test = Solution()
answer = test.topKFrequent(input, 2)

print(answer)
