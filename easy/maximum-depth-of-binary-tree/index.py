from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverse(self, root, depth):   
        if not root:
            return 0
            
        l = self.traverse(root.left, 1)
        r = self.traverse(root.right, 1)
        
        if l > r:
            return depth + l
        else:
            return depth + r

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = self.traverse(root, 1)

        return depth