

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """



        def f01(node):
            return f01(node.left) + [node.val] + f01(node.right) if node else []

        return f01(root)[k-1]



