class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if(self.stack2==[]):
            while(self.stack1!=[]):
                element = self.stack1.pop()
                self.stack2.append(element)
            
        return self.stack2.pop()
        
        

    def peek(self) -> int:
        if(self.stack2==[]):
            while(self.stack1!=[]):
                element = self.stack1.pop()
                self.stack2.append(element)
        return self.stack2[-1]
        

    def empty(self) -> bool:
        if(self.stack1 == [] and self.stack2 == []):
            return True
        return False