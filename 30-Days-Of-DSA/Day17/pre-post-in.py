class BinaryTreeNode :
    def __init__(self, data, left = None, right = None) :
        self.data = data
        self.left = None
        self.right = None
def solveRecursive(root, visited, pre, post, inord):
    if(root == None):
        return inord, pre, post
    else:
        if(root not in visited):
            pre.append(root.data)
            visited[root] = 1
        solveRecursive(root.left, visited, pre, post, inord)
        if(visited[root] == 1):
            inord.append(root.data)
            visited[root]+=1
        solveRecursive(root.right, visited, pre, post, inord)
        if(visited[root] == 2):
            post.append(root.data)
            visited[root]+=1


        
        
    return inord, pre, post
        
def getTreeTraversal(root):
    inord, pre, post = solveRecursive(root, {}, [], [], [])
    return inord, pre, post


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

print(getTreeTraversal(root))