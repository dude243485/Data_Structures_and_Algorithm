class MyHashSet:

    def __init__(self):
        self.keyArr = []
        

    def add(self, key: int) -> None:
        if key not in self.keyArr:
            self.keyArr.append(key)
        

    def remove(self, key: int) -> None:
        self.keyArr.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.keyArr:
            return True
        return False