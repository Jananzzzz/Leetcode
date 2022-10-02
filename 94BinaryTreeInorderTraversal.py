def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    def inOrder(root):
        if(root):
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)
    inOrder(root) 
    return res    