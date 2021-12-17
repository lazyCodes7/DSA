class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        arr = nums
        while(left<=right):
            mid = int((left+right)/2)
            
            if(arr[mid] == target):
                return mid
            
            else:
                if(arr[left] <= arr[mid]):
                    if(target>=arr[left] and target<=arr[mid]):
                        right = mid-1
                    
                    else:
                        left = mid+1
                    
                else:
                    if(target>=arr[mid] and target<=arr[right]):
                        left = mid+1
                    
                    else:
                        right = mid-1
        return -1