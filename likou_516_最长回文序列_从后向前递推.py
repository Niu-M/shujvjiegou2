a = "cbbd"

"""
初始化dp矩阵，各个位置的值为0
初始化切入位置的值，也就是dp[n-1][n-1]=1
然后递推并更新dp中的值

dp[i][j]，表示索引i-j范围内的子串中，最长回文序列的长度

"""
def f(s):
    n = len(s)
    import numpy as np
    dp = np.zeros((n, n), dtype=int)

    for i in range(n - 1, -1, -1):

        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    return dp[0][n - 1]


print(f(a))

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        也是一种递推方法
        :type n: int
        :rtype: List[str]
        """


        def f(n):
            res = []
            if n == 1:
                res.append("1")
                res.append("8")
                return res
            if n == 0:
                res.append("")
                return res

            a = f(n - 2)

            for i in a:
                res.append("1" + i + "1")
                res.append("6" + i + "9")
                res.append("9" + i + "6")
                res.append("8" + i + "8")
            return res


        return f(n)
print(Solution().findStrobogrammatic(2))