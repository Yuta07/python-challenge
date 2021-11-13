from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursive(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left and right:
            if left.val != right.val:
                return False
            else:
                return self.recursive(left.left, right.right) and self.recursive(left.right, right.left)
        elif not left and not right:
            return True
        else:
            return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        result = self.recursive(root.left, root.right)

        return result