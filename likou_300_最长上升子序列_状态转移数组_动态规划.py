def myTest2(nums):
    """非递归写法，通过数组递推写法，速度快"""
    if not nums:
        return 0

    dp = []  # 该数组用于存放各个位置对应的最优解，我们最终要得到的结果是dp[len(nums)-1]的值，
             # 该值需要通过dp前面的一堆值向后一个个推导出来

    for i in range(len(nums)):  # 用于更新出dp[i]的值，表示使用nums[i]作为最后一个值时的解
        dp.append(1)
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[j]+1,dp[i])
    return max(dp)

def myTest(nums):
    """递归写法，比较耗时间，容易理解"""
    n = len(nums)
    def search(i,tmp):
        if i>=n:
            return 0
        a = 0
        if nums[i]>tmp:
            a = search(i+1,nums[i]) + 1
        b = search(i+1,tmp)

        return max(a,b)
    max_val = 0
    for i in range(n):
        t = search(i,-float('inf'))
        if t>max_val:
            max_val = t
    return max_val


print(myTest2([10,9,2,5,3,7,101,4]))



"""递推案例二
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        import numpy as np
        my_mat = np.ones((m, n))

        for i in range(1, m):
            for j in range(1, n):
                my_mat[i][j] = my_mat[i][j - 1] + my_mat[i - 1][j]
        return int(my_mat[m - 1][n - 1])