#User function Template for python3
answer = []
def permute(a, l, r):
    if(l == r):
        global answer
        answer.append("".join(a))
    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l] #swapping the value for generating permutation
            permute(a, l+1, r) # calculating perumuation by recursion call
            a[l],a[i] = a[i],a[l] ## Once the permutation are generated swap back to original string
class Solution:
    def find_permutation(self, S):
        permute(list(S), 0, len(S)-1)
        global answer
        return answer