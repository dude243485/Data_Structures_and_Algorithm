from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def stringSorter (s):
            return "".join(sorted(s))
        map = {}
            
        for i in range(len(strs)):
            if stringSorter(strs[i]) not in map:
                map[stringSorter(strs[i])] = [strs[i]]
                
            elif stringSorter(strs[i]) in map:
                map[stringSorter(strs[i])].append(strs[i])
        return list(map.values())      
                
input = ["eat","tea","tan","ate","nat","bat"]
test = Solution()
answer = test.groupAnagrams(input)
print(answer)
print("yeah")