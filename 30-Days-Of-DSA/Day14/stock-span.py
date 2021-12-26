import copy
class StockSpanner:

    def __init__(self):
        self.stocks = []
        self.stack = []
        

    def next(self, price: int) -> int:
        self.stocks.append(price)
        ans = 0
        pop_cnt = 0
        if(self.stack == []):
            self.stack.append([price, 0])
            ans = pop_cnt+1
        else:
            while(self.stack!=[] and self.stack[-1][0]<=price):
                pop_cnt+=1
                element=self.stack.pop()
                pop_cnt+=element[1]
            self.stack.append([price, pop_cnt])
            ans = pop_cnt+1
        return ans