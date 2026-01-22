class MyHashMap:

    def __init__(self):
        self.keyArr = []
        self.valArr = []
        

    def put(self, key: int, value: int) -> None:
        if key in self.keyArr:
            pos = self.keyArr.index(key)
            self.valArr[pos] = value
            return
        self.keyArr.append(key)
        self.valArr.append(value)
        
            
    def get(self, key: int) -> int:
        if key in self.keyArr:
            pos = self.keyArr.index(key)
            return self.valArr[pos]
        return -1
        

    def remove(self, key: int) -> None:
        if key in self.keyArr:
            pos = self.keyArr.index(key)
            self.valArr.pop(pos)
            self.keyArr.pop(pos)