class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers

    def solveRecursive(self, A, B, path = []):
        if(A == None):
            return None

        path.append(A.val)
        if(A.val == B):
            return path

        res = Solution.solveRecursive(self, A.left, B, path)
        if(res!=None):
            return path
        res = Solution.solveRecursive(self, A.right, B, path)
        if(res!=None):
            return path
        else:
            path.pop()

        return None
    def solve(self, A, B):
        path = self.solveRecursive(A, B, [])
        return path

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.solve(root, 4))
