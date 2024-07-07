# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def recursive(node: TreeNode, right_val=0):
            if node.right is None:
                node.val = node.val + right_val
                if node.left is None:
                    return node.val
                return recursive(node.left, node.val)
            node.val = node.val + recursive(node.right, right_val)
            if node.left is None:
                return node.val
            return recursive(node.left, node.val)
        
        recursive(root)
        return root

# Runtime: 40 ms (faster than 40% of online Python3 submissions)
# Memory usage: 13.9 MB (less than 100% of online Python3 submissions)