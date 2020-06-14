
class Node(object):
    def _init_(self, item):
        self.elem=item
        self.lchild=None
        self.rchild=None


class Tree(object):
    """二叉树"""
    def _init_(self):
        self.root=None

    def add(self, item):
        node=Node(item)

        if self.root is None:
            self.root=node
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)

        if cur_node.lchild is None:
            cur_node.lchild=node
            return
        else:
            queue.append(cur_node.lchild)
        if cur_node.rchild is None:
            cur_node.rchild=node
            return
        else:
            queue.append(cur_node.rchild)