class Solution:
    def findNextSmaller(self, arr, direction = 'left'):
        if(direction == 'left'):
            left_res = {}
            right_res = {}
            stack = []
            left_res[0] = 0
            stack.append(0)
            for i in range(1,len(arr)):
                while(stack!=[] and arr[stack[-1]] >= arr[i]):
                    idx = stack.pop()
                    right_res[idx] = i-1
                
                if(stack == []):
                    left_res[i] = 0
                    stack.append(i)
                else:
                    left_res[i] = stack[-1]+1
                    stack.append(i)
        
            while(stack != []):
                idx = stack.pop()
                right_res[idx] = len(arr)-1
            return left_res, right_res
        else:
            res = []
            stack = []
            res.append(len(arr)-1)
            stack.append(len(arr)-1)
            for i in range(len(arr)-2, -1, -1):
                while(stack!=[] and arr[stack[-1]] >= arr[i]):
                    stack.pop()
                if(stack == []):
                    res.append(len(arr)-1)
                    stack.append(i)
                else:
                    res.append(stack[-1]-1)
                    stack.append(i)
            return res
        
                
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_smaller, right_smaller = self.findNextSmaller(heights, direction = 'left')
        #right_smaller = self.findNextSmaller(heights, direction = 'right')
        #print(left_smaller)
        #print(right_smaller)
        
        i = 0
        maxHeight = 0
        while(i<len(heights)):
            height = (right_smaller[i] - left_smaller[i] + 1)*heights[i]
            #print(height)
            maxHeight = max(height, maxHeight)
            i+=1
        return maxHeight