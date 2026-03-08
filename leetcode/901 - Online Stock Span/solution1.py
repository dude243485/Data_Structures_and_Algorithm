class StockSpanner:

    def __init__(self):
        self.stk = []
        
    def next(self, price: int) -> int:
        if len(self.stk) == 0:
            span = 1
            self.stk.append([price, span])
            return span
        
        span = 1
        endPos = len(self.stk) - 1
        while self.stk[endPos][0] <= price and endPos >= 0:
            span += self.stk[endPos][1]
            endPos -= self.stk[endPos][1]
       
        self.stk.append([price, span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)