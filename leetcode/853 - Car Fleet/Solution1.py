from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed), reverse=True))
        
        count = 0
        smallest = (target - position[0]) / speed[0]
        
        for i in range(1, len(position)):                
            if not (target - position[i]) / speed[i] <= smallest:
                count += 1
                smallest = (target - position[i]) / speed[i]
                   
        return count + 1
   
        
         
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

test = Solution()
print(test.carFleet(target, position, speed))