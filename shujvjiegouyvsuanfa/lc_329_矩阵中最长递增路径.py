
class Solusion():
    """
    329：
    给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。
    """
    def __init__(self):
        self.ans = 0
        self.path = {}
        self.pidx = 0
        self.n = 0
        self.m = 0

    # 方法
    def robot(self,idx_x,idx_y,matrix):
        max1 = 0
        # 从当前点，向前走一步，遍历出四种可能：
        for dx in range(-1,2): # -1，0，1
            for dy in range(-1,2): # -1，0，1
                if dx == 0 and dy != 0 or dx != 0 and dy == 0:
                    check(matrix[idx_x][idx_y] > matrix[idx_x+dx][idx_y+dy])
                    max1 = max(max1,self.robot(idx_x+dx,idx_y+dy,matrix)) + 1
        return max1


    # 入口方法
    def longestIncreasingPath(self, matrix):
        """
        1、遍历出各个起点，然后调用方法进行查找；
        2、在递归方法中，向各个方向走
        """
        n = len(matrix)
        m = len(matrix[0])

        # 遍历尝试各个点作为可能的起点
        for i in range(n):
            for j in range(m):
                self.ans = max(self.ans,self.robot(i,j,matrix))
        return self.ans


candidates = [2,3,6,7]
target = 7
a = Solusion().combinationSum(candidates,target)

print(a)










