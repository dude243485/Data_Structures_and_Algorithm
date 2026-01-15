class MinStack:

    def __init__(self):
        self.contain = []
        self.minArr = []
        self.min = 0
        
        

    def push(self, val: int) -> None:
        if not self.contain:
            self.minArr.append(val)             
        
        else:
            if self.minArr[-1] < val:
               self.minArr.append(self.minArr[-1]) 
            else:
                self.minArr.append(val)
                
        self.contain.append(val)
            

    def pop(self) -> None:
        self.contain.pop()
        self.minArr.pop()
        

    def top(self) -> int:
        return self.contain[-1]
        

    def getMin(self) -> int:
        return self.minArr[-1]
    
    
test = MinStack()
test.push(-2)
test.push(0)
test.push(-3)

print(test.contain)
print(test.minArr)