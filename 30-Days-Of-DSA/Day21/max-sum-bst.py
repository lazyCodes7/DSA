class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.maxsum = 0
    def solveRecursive(self, root, bound):
        if(root == None):
            return 0, True
        else:
            val = True
            if((root.val<bound[0] or root.val>bound[0]) == False):
                bound = [float('-inf'), float('inf')]
                val = False
            
            lsum, isleftbst = Solution.solveRecursive(
                self,
                root.left,
                [bound[0],root.val]
            )
            rsum, isrightbst = Solution.solveRecursive(
                self,
                root.right,
                [root.val, bound[1]]
            )
            
            if(isleftbst and isrightbst):
                self.maxsum = max((lsum+rsum+root.val), self.maxsum)
            
            isbst = val and isleftbst and isrightbst
            
            return (lsum+rsum+root.val), isbst
            
    def maxSumBST(self, root) -> int:
        self.solveRecursive(root, [float('-inf'), float('inf')])
        return self.maxsum


root = TreeNode(1)
root.right = TreeNode(10)
root.right.left = TreeNode(-5)
root.right.right = TreeNode(20)

sol = Solution()
print(sol.maxSumBST(root))