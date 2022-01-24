from collections import deque
class Solution:
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append([root, 0])
        size = 1
        curMin = 0
        maxWidth = 0
        while(len(q) > 0):
            size = len(q)
            node = q[0]
            curMin = node[1]
            for i in range(size):
                node = q.popleft()
                idx = node[1] - curMin
                currNode = node[0]
                if(i == 0):
                    leftmost = node[1]
                if(i == size - 1):
                    rightmost = node[1]
                if(currNode.left != None):
                    q.append([
                        currNode.left,
                        2*idx+1
                    ])
                if(currNode.right!= None):
                    q.append([
                        currNode.right,
                        2*idx+2
                    ])
            maxWidth = max((rightmost-leftmost+1),maxWidth)
        
        return maxWidth