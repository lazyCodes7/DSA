class Solution:
    def solveRecursive(self, root, traversal):
        if(root == None):
            return traversal
        else:
            
            Solution.solveRecursive(self, root.left, traversal)     
            Solution.solveRecursive(self, root.right, traversal)
            traversal.append(root.val)
            return traversal
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]: