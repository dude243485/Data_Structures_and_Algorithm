from typing import List
input = ["neet","code","love","you"]


class Solution:

    def encode(self, strs: List[str]) -> str:
        
        map = {}
        #fill the map
        for i in range(256):
            map[chr(i)] = i
           
        input_str = ",".join(strs)    
        map_size = 256
        w = ""
        result = []
        
        for c in input_str:
           wc = w + c
           if wc in map:
               w = wc
           else:
               result.append(map[w]) 
               map[w] = map_size
               map_size += 1
               w = c
               
        if w: 
            result.append(map[w])
        
        return result

    def decode(self, s: str) -> List[str]:
        map = {}
        #fill the map
        for i in range(256):
            map[chr(i)] = i
            
        result = ""
        map_size = 256
        w = chr(s.pop(0))
        result += w
        
        for k in s:
            if k in map:
                entry = map[k]
            elif k == map_size:
                entry = w + w[0]
                
            else:
                raise ValueError("Bad compressed data")
            result += entry
            map[map_size] = w + entry[0]
            map_size += 1
            w = entry 
        return result
            
        

test = Solution()
answer = test.encode(input)
print(answer)