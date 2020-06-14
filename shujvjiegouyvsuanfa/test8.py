class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :param strs: 字符串数组，如：["10", "0001", "111001", "1", "0"]
        :param m:0的个数
        :param n:1的个数
        :return:可以组成字符串的数量

        0-1背包问题：
        把全部的0和1放在一起，看成一个背包的总容量；
        将某个字符串装入背包中，背包的容量自然会减小；

        题目有哪些序列，就把哪些序列定义成状态dp[i][j][k],

        对于当前的字符串，可能放入包中，则：dp[i-1][j-]
        """
        # 边界条件，当数组中的元素被取完时，结束
        if len(strs) == 0:
            return 0

        # 初始化一个矩阵背包，元素值为0，行数是0的个数，列数是1的个数
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for strs_item in strs: # 遍历出数组中的各个元素，分别得到当前元素字符串中的0和1的个数
            item_count0 = strs_item.count('0')
            item_count1 = strs_item.count('1')

            # 遍历可容纳的背包

            for i in range(m, item_count0 - 1, -1):  # 从后往前遍历
                for j in range(n, item_count1 - 1, -1): # 从后往前遍历
                    # 当前取出的i个0和j个1能够组成字符串strs_item，但是，这个位置我可能用，也可能不用
                    dp[i][j] = max(dp[i][j], 1 + dp[i - item_count0][j - item_count1])

        return dp[m][n]


print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"],5,3))
print(Solution().findMaxForm(["10", "0001", "111001", "1", "0","011"],5,3))






class Solution01:
    def findMaxForm01(self, strs, m, n):
        """
        :param strs: 字符串数组，如：["10", "0001", "111001", "1", "0"]
        :param m:0的个数
        :param n:1的个数
        :return:可以组成字符串的数量
        """

        dp = {}

        def f01(i,j,k):

            if str(i)+"-"+str(j)+"-"+str(k) in dp:
                return dp[str(i)+"-"+str(j)+"-"+str(k)]

            if i<0:
                return 0



            count_0 = strs[i].count('0')
            count_1 = strs[i].count('1')
            a = 0
            b = 0
            if j>=count_0 and k>=count_1: # 在满足条件的情况下，可选可不选
                a = max(f01(i-1,j-count_0,k-count_1) + 1,f01(i-1,j,k))
            # else:
                # b = f01(i-1,j,k) # 不满足一定不选，但这个是多余的，因为上面已经包含这种状态（不选）情况了
            dp[str(i) + "-" + str(j) + "-" + str(k)] = max(a,b)
            return dp[str(i)+"-"+str(j)+"-"+str(k)]


        return f01(len(strs)-1,m,n)


