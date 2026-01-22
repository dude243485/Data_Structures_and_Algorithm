class MyHashMap:

    def __init__(self):
        self.map = []
        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.map)):
            if key == self.map[i][0]:
                self.map[i] = (key, value)
                return
        self.map.append((key, value))

    def get(self, key: int) -> int:
        for i in range(len(self.map)):
            if key == self.map[i][0]:
                return self.map[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.map)):
            if key == self.map[i][0]:
                self.map.pop(i)
                return