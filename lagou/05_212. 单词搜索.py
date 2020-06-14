import sys
sys.setrecursionlimit(1000000)
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """


        result = []
        status = {}
        def robot(i,j,str1):

            if str(i)+str(j)+str1 in status:
                return status[str(i)+str(j)+str1]

            if i>=len(board) or i<0:
                return
            if j>=len(board[0]) or j<0:
                return

            str1 = str1 + board[i][j]
            status[str(i) + str(j) + str1] = str1
            result.append(str1)

            # robot(i+1,j,str1)
            # robot(i,j+1,str1)
            # robot(i-1,j,str1)
            # robot(i,j-1,str1)



        for i in range(len(board)):
            for j in range(len(board[0])):
                robot(i,j,"")
        out = []
        for str_tmp in words:

            if str_tmp in result:
                out.append(str_tmp)
        return out

words = ["oath","pea","eat","rain"]
board =[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
# print(Solution().findWords(board,words))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count = 0

    def dfs(self, root):
        if not root:
            return True


        l = self.dfs(root.left)
        r = self.dfs(root.right)
        cur = True
        if root.left and root.val != root.left.val:
            cur = False
        if root.right and root.val != root.right.val:
            cur = False
        if l and r and cur:
            self.count += 1

        return l and r and cur

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.count
class Solution01(object):
    def isBipartite(self, graph):

        color = {}

        for node in xrange(len(graph)): # 遍历出行索引

            if node not in color:

                stack = [node]

                # 在字典中添加该键值对
                color[node] = 0

                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = 0 if color[node]==1 else 1
                        elif color[nei] == color[node]:
                            return False
        return True
class Solution03(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []
        for idx1 in range(len(nums)):
            count = 0
            for idx2 in range(idx1+1,len(nums)):

                if nums[idx2]<nums[idx1]:
                    count += 1
            result.append(count)
        return result



print(Solution03().countSmaller([5,2,6,1]))
class Solution004:

    def countSmaller(self, nums):
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        temp = [None for _ in range(size)]
        indexes = [i for i in range(size)]
        res = [0 for _ in range(size)]

        self.__helper(nums, 0, size - 1, temp, indexes, res)
        return res

    def __helper(self, nums, left, right, temp, indexes, res):
        if left == right:
            return
        mid = left + (right - left) // 2

        # 计算一下左边
        self.__helper(nums, left, mid, temp, indexes, res)
        # 计算一下右边
        self.__helper(nums, mid + 1, right, temp, indexes, res)

        if nums[indexes[mid]] <= nums[indexes[mid + 1]]:
            return
        self.__sort_and_count_smaller(nums, left, mid, right, temp, indexes, res)

    def __sort_and_count_smaller(self, nums, left, mid, right, temp, indexes, res):
        # [left,mid] 前有序数组
        # [mid+1,right] 后有序数组

        # 先拷贝，再合并

        for i in range(left, right + 1):
            temp[i] = indexes[i]

        l = left
        r = mid + 1
        for i in range(left, right + 1):
            if l > mid:
                # l 用完，就拼命使用 r
                # [1,2,3,4] [5,6,7,8]
                indexes[i] = temp[r]
                r += 1
            elif r > right:
                # r 用完，就拼命使用 l
                # [6,7,8,9] [1,2,3,4]
                indexes[i] = temp[l]
                l += 1
                # 注意：此时前面剩下的数，比后面所有的数都大
                res[indexes[i]] += (right - mid)
            elif nums[temp[l]] <= nums[temp[r]]:
                # [3,5,7,9] [4,6,8,10]
                indexes[i] = temp[l]
                l += 1
                # 注意：
                res[indexes[i]] += (r - mid - 1)
            else:
                assert nums[temp[l]] > nums[temp[r]]
                # 上面两种情况只在其中一种统计就可以了
                # [3,5,7,9] [4,6,8,10]
                indexes[i] = temp[r]
                r += 1