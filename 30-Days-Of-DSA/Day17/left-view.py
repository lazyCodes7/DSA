def solveRecursive(root, level, traversal):
    if(root == None):
        return traversal
    
    if(level == len(traversal)):
        traversal.append(root.data)
        
    solveRecursive(root.left, level+1, traversal)
    solveRecursive(root.right, level+1, traversal)
        
    return traversal
def LeftView(root):
    


    return solveRecursive(root, 0, [])