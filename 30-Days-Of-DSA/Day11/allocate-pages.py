class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def isPossible(self, A, limit, B):
		pages = 0
		allocated = 1
		for i in range(len(A)):
			if(A[i]>limit):
				return False
			else:
				if(pages+A[i]>limit):
					pages = A[i]
					allocated+=1
				else:
					pages+=A[i]

		return True if allocated<=B else False

	def books(self, A, B):
		low = min(A)
		high = sum(A)

		if(B>len(A)):
			return -1

		while(low<=high):
			mid = int((low + high)/2)

			if(self.isPossible(A,mid,B)):
				high = mid-1

			else:
				low = mid+1
		return low