# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC  = O(N) ; SC = O(h) , where h is the maximum height of the tree.

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(root1,root2):
            if root1 == None and root2 == None:
                return True
            
            # if the root of both left and right trees are none
            # means they are symmetric
            # eg :                  1
            #                      / \
            #                    None None
            
            #if roots are not none
            if root1 is not None and root2 is not None:
                if root1.val == root2.val:
                    
                    # if data of roots of both left and right trees are same
                    # then we gotta check if left subtree of left tree is mirror                           
					# image of right subtree of right tree and vice versa.
                    
                    return isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left)
            # if none of the above condition satisfies means tree is asymmetric
            return False
        
        return isMirror(root,root)
    # we send in root, root above because both the left half and the right half
    # of the tree are going to start at the common parent node