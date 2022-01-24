from queue import Queue
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = Queue()
        q.put((root, 0, 0))
        visited = {}
        visited[0] = {}
        visited[0][0] = [root.val]
        while(q.empty() == False):
            node, v_level, h_level = q.get()
            
            if(node.left!=None):
                q.put((node.left, v_level-1, h_level+1))
                if(v_level-1 not in visited):
                    visited[v_level-1] = {}
                    
                    if(h_level+1 not in visited[v_level-1]):
                        visited[v_level-1][h_level+1] = [node.left.val]
                                        
                else:
                    if(h_level+1 not in visited[v_level-1]):
                        visited[v_level-1][h_level+1] = [node.left.val]
                    else:
                        visited[v_level-1][h_level+1].append(node.left.val)
            
            if(node.right!=None):
                q.put((node.right, v_level+1, h_level+1))
                if(v_level+1 not in visited):
                    visited[v_level+1] = {}
                    
                    if(h_level+1 not in visited[v_level+1]):
                        visited[v_level+1][h_level+1] = [node.right.val]
                                        
                else:
                    if(h_level+1 not in visited[v_level+1]):
                        visited[v_level+1][h_level+1] = [node.right.val]
                    else:
                        visited[v_level+1][h_level+1].append(node.right.val)
        ans = []
        for i in sorted(visited):
            li = []
            for j in sorted(visited[i]):
                for ele in sorted(visited[i][j]):
                    li.append(ele)
            ans.append(li)
        return ans