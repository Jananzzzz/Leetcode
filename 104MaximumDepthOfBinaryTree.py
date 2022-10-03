# the simplest solution
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1      # don't forget self
'''

# more common one:

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return 0
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        return dfs(root, 0)