from queue import Queue
class Solution:
    def freshCount(self, grid):
        fresh = 0
        queue = Queue()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 2):
                    queue.put([i,j])
                if(grid[i][j] == 1):
                    fresh+=1
        return queue, fresh
       
            
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        queue, fresh = self.freshCount(grid)
        if(queue.empty() and fresh>0):
            return -1
        elif(queue.empty() and fresh == 0):
            return 0
        
        fresh+=queue.qsize()
        
        while(queue.empty() == False and fresh>0):
            size = queue.qsize()
            fresh-=size
            while(size):
                idx = queue.get()
                x, y = idx[0], idx[1]
                if(x+1<len(grid) and grid[x+1][y] == 1):
                    grid[x+1][y] = 2
                    queue.put([x+1,y])
                if(y-1>=0 and grid[x][y-1] == 1):
                    grid[x][y-1] = 2
                    queue.put([x,y-1])

                if(y+1<len(grid[0]) and grid[x][y+1] == 1):
                    grid[x][y+1] = 2
                    queue.put([x,y+1])

                if(x-1>=0 and grid[x-1][y] == 1):
                    grid[x-1][y] = 2
                    queue.put([x-1,y])
                size-=1
            if(queue.empty() == False):
                mins+=1
        #print(grid)
             
        if(fresh>0):
            return -1
        else:
            return mins