
class Solusion():
    """
    39：
    给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

    """
    def __init__(self):
        self.ans = []
        self.path = {}
        self.pidx = 0

    # 迭代方法
    def robot(self,idx,c,target):
        # 边界停止条件
        if target == 0:
            # 符合正常结束条件，记录当前递归出的结果
            tmp = []
            for  i in range(self.pidx):
                tmp.append(self.path[i])
            self.ans.append(tmp)

            return
        if idx >= len(c) or target<0:
            return

        # 每次有两种可能情况：取/不取，都要进行一次

        # 当前索引值取
        # 为什么不用追加？因为不同的递归路线会共享这个变量，如果不改值，而是追加，会导致混在一起
        self.path[self.pidx] = c[idx]

        self.pidx += 1
        self.robot(idx,c,target-c[idx])
        # 当前索引值不取
        self.pidx -= 1
        self.robot(idx+1, c, target)






    # 入口方法
    def combinationSum(self,candidates,target):
        self.ans = []
        self.robot(0,candidates,target)
        return self.ans


candidates = [2,3,6,7]
target = 7
a = Solusion().combinationSum(candidates,target)

print(a)










