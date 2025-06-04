class Solution:
    def solveRecursive(self, arr, limit, currentIndex):
        if(currentIndex == limit):
            return arr
        else:
            if(arr[currentIndex] > arr[currentIndex+1]):
                arr[currentIndex], arr[currentIndex+1] = arr[currentIndex+1], arr[currentIndex]

            return Solution.solveRecursive(self, arr, limit, currentIndex+1)
	
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums = self.solveRecursive(nums, len(nums)-i-1, 0)
        return nums
        
        