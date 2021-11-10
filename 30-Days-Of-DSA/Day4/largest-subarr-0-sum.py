class Solution:
    def maxLen(self, n, arr):
        visited = {}
        max_count = 0
        sum = 0
        for i in range(len(arr)):
            sum+=arr[i]
            try:
                    if(sum == 0):
                        max_count = max(i+1, max_count)
                    elif(visited[sum][0] == True):
                        max_count = max(i-visited[sum][1], max_count)
            except:
                visited[sum] = [True, i]
            
        return max_count