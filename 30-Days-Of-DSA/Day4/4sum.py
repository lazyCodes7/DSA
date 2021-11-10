class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        isFound = {}
        ans = []
        for i in range(n-3):
            a = nums[i]
            for j in range(i+1, n-2):
                b = nums[j]
                L = j+1
                R = n-1
                while(L<R):
                    c = nums[L]
                    d = nums[R]
                    sum = a+b+c+d
                    if(sum<target):
                        L+=1
                        
                    elif(sum>target):
                        R-=1
                    else:
                        key = frozenset([a,b,c,d])
                        if key not in isFound:
                            ans.append([a,b,c,d])
                            isFound[key] = True
                            
                        L += 1
                        R -= 1
                            
        return ans