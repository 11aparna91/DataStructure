### Depth first traversal
### Inorder (Left, Root, Right)
### Preorder (Root, Left, Right)
### Postorder (Left, Right, Root)





####################################### BFS ##################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            queLen=len(q)
            level=[]
            for i in range(queLen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)
        return res
    
################################################################
#### Time complexity= O(m+n) #############################
############### Merge two Binary trees ##################
######### Problem Number 617 ########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2:
            return None
        v1= root1.val if root1 else 0
        v2= root2.val if root2 else 0
    
        root=TreeNode(v1+v2)
        
        root.left= self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right= self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        return root
           
