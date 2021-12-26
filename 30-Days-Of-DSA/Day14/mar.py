def findNextSmaller(arr):
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

def largestRectangleArea(heights) -> int:
    left_smaller, right_smaller = findNextSmaller(heights)
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


def maxRectangleArea(matrix):
    arr = []
    maxArea = 0
    for i in range(0, len(matrix[0])):
        arr.append(0)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if(matrix[i][j]!="0"):
                arr[j]+=1
            else:
                arr[j]=0
        area = largestRectangleArea(arr)
        maxArea = max(area, maxArea)
    return maxArea
matrix = [["1"]]
print(maxRectangleArea(matrix))
