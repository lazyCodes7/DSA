class Solution:
    def solveRecursive(self, root, traversal):
        if(root == None):
            return traversal
        else:
            Solution.solveRecursive(self, root.left, traversal)     
            traversal.append(root.val)
            Solution.solveRecursive(self, root.right, traversal)
            return traversal
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #print(root)
        #traversal = self.solveRecursive(root, [])
        traversal = []
        current = root
        while(current is not None):
            if(current.left == None):
                traversal.append(current.val)
                current = current.right
                
            else:
                next_node = current.left
                while(next_node.right is not None and next_node.right != current):
                    next_node = next_node.right
                
                if(next_node.right is None):
                    next_node.right = current
                    current = current.left
                else:
                    traversal.append(next_node.right.val)
                    next_node.right = None
                    current = current.right
                
                
                
        return traversal