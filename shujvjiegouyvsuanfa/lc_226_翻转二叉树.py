class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.robot(root)

    def robot(self,root):
        if root == None:
            return None
        leftRoot = root.left
        rightRoot = root.right
        root.left = rightRoot
        root.right = leftRoot
        if leftRoot != None:
            self.robot(leftRoot)
        if rightRoot != None:
            self.robot(rightRoot)

        return root


Solution().invertTree()

