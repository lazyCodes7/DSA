from collections import deque
class MyStack:

    def __init__(self):
        self.last_element = 0
        self.queue1 = deque()
        self.queue2 = deque()
        
        

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.last_element+=1
        

    def pop(self) -> int:
        idx = 0
        while(self.empty() == False and idx<self.last_element-1):        
            element = self.queue1.popleft()
            self.queue1.append(element)
            idx+=1
        self.last_element-=1
        return_element = self.queue1.popleft()
        return return_element
        
        

    def top(self) -> int:
        element = None
        idx = 0
        while(self.empty() == False and idx<self.last_element):
            element = self.queue1.popleft()
            self.queue1.append(element)
            idx+=1
            
        return element
        
        
        
        

    def empty(self) -> bool:
        if(len(self.queue1) == 0):
            return True
        return False