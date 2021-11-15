class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        curr_time = 0
        count = 0
        meetings = []
        for i in range(n):
            meetings.append([end[i], start[i]])
        
        meetings.sort()
        
        for meeting in meetings:
            end, start = meeting[0], meeting[1]
            if(curr_time<start):
                count+=1
                curr_time = end
        return count