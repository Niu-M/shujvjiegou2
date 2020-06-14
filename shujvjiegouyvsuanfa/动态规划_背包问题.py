
class Solution3(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]，是各个物品的重量
        :type amount: int ，最大重量
        :rtype: int，最大物品数量
        """

        status = {}

        def f(idx,count):
            if str(idx)+str(count) in status:
                return status[str(idx)+str(count)]
            if idx > len(coins)-1:
                return float('inf')
            if count < 0:
                return float('inf')
            if count == 0:
                return 0

            status[str(idx)+str(count)] = min(f(idx,count-coins[idx])+1,f(idx+1,count))
            return status[str(idx)+str(count)]

        a = f(0, amount)
        if a != float('inf'):
            return a
        else:
            return -1
coins = [1, 2, 5]
amount = 11
# print(Solution3().coinChange(coins,amount))

"""背包问题：



"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        def f(i):
            if i>=len(nums):
                return 0

            return max(nums[i]+f(i+2),f(i+1))

        return f(0)
