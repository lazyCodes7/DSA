class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        jobs = []
        #print(Jobs[0].profit)
        num_jobs = 0
        profit = 0
        true_count = 0
        visited = {}
        max_deadline = 0
        for job in Jobs:
            max_deadline = max(max_deadline, job.deadline)
            jobs.append([job.profit, job.deadline])
            
        for i in range(1,max_deadline+1):
            visited[i] = False
        
        jobs.sort(reverse = True)
        len_visited = len(list(visited.keys()))
        for i in range(len(jobs)):
            curr_profit, deadline = jobs[i][0], jobs[i][1]
            if(visited[deadline] == False):
                num_jobs+=1
                profit+=curr_profit
                true_count+=1
                visited[deadline] = True
            else:
                while(deadline>=1 and visited[deadline] == True):
                    deadline-=1
                if(deadline>0):
                    num_jobs+=1
                    visited[deadline] = True
                    true_count+=1
                    profit+=curr_profit
                elif(true_count == len_visited):
                    break
                
               
        return [num_jobs,profit]