class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        len_arr = len(intervals)
        curr_interval = intervals[0]
        for i in range(1,len_arr):
            if(intervals[i][0] <= curr_interval[1]):
                curr_interval[1] = max(intervals[i][1], curr_interval[1])
                curr_interval[0] = min(intervals[i][0], curr_interval[0])
            else:
                ans.append(curr_interval)
                curr_interval = intervals[i]
        ans.append(curr_interval)
            
        return ans
                
        
cap.set(3,1280)

cap.set(4,1024)

time.sleep(2)

cap.set(15, -8.0)