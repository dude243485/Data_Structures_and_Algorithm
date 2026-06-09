
class ArrayClass():
    def __init__(self):
        #initialization variables
        self.size = 0
        self.capacity = 6
        self.data = []
        
        
    def resize(self):
        self.capacity = self.capacity * 2
        
        
    
    def shiftRight(self, startIndex : int) :
        if self.size >= self.capacity : self.resize()
        for i in range(self.size, startIndex , -1):
            self.data[i] = self.data[i-1]
            
        self.size += 1
        
        
    def validateIndex(self, index : int ):
        if index < 0 or index >= self.size :
            raise IndexError       
            
    
    def insertAtBegining(self, value) :
        self.shiftRight(0)
        self.data.append(value)
    
    def insertAtEnd(self, value):
        if self.size >= self.capacity : self.resize()
        self.data[self.size] = value
        self.size += 1
    
    def insertAtIndex(self, value, index) :
        self.shiftRight(index)
        self.data[index] = value
        
    
    def insertBeforeIndex(self, value, index) :
        self.validateIndex(index)
        self.shiftRight(index)
        self.data[index] = value
    
    def insertAfterIndex(self, index, value) :
        self.validateIndex(index)
        self.shiftRight(index + 1)
        self.data[index + 1] = value
        
    def print(self):
        print(self.data)
    
        
arrayobject = ArrayClass()
arrayobject.insertAtBegining(9)
arrayobject.print()
arrayobject.insertAtEnd(2)
arrayobject.print()
arrayobject.insertAtIndex(1, 6)
arrayobject.print()
arrayobject.insertAfterIndex(0, 8)
arrayobject.print()