class Solution:
    def solveRecursive(self, arr, idx, currentIndex):
        if(currentIndex < 0):
            return arr
        else:
            if(arr[idx]<arr[currentIndex]):
                arr[idx], arr[currentIndex] = arr[currentIndex], arr[idx]
                return Solution.solveRecursive(self, arr, currentIndex, currentIndex-1)
            else:
                return Solution.solveRecursive(self, arr, idx, currentIndex-1)
	
    def sortArray(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            nums = self.solveRecursive(nums, idx, idx-1)
        return nums
        
        