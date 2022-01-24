class Solution:
  
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #print(root)
        traversal = []
        current = root
        while(current != None):
            if(current.left == None):
                traversal.append(current.val)
                current = current.right
            else:
                next_node = current.left
                while(next_node.right!= None and next_node.right!=current):
                    next_node = next_node.right
                
                if(next_node.right!=None):
                    next_node.right = None
                    current = current.right
                else:
                    traversal.append(current.val)
                    next_node.right = current
                    current = current.left
                    
            
        return traversal