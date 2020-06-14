class Solusion:
    def __init__(self):
        self.result = {}

    # 定义一个方法，用于迭代调用
    def solve1(self, idx, nums):

        # 当取完第一位时，结束方法
        if idx < 0:
            return 0

        """
        当列表中的该位置有值时，直接取出并返回

        引入该列表，是为了避免重复计算，已经计算过的，重新取出值即可。


        """
        if self.result[idx] >= 0:
            return self.result[idx]

        # 当取当前节点的值时，下一次只能隔一个再取；
        # 当不取当前节点值时，调用取下一个的值
        self.result[idx] = max(nums[idx] + self.solve1(idx - 2, nums), self.solve1(idx - 1, nums))

        return self.result[idx]

    # 定义一个该程序的入口方法
    # 从尾部开始遍历
    def rob(self, nums):

        for i in range(len(nums)):
            self.result[i] = -1

        # 开始计算，从最后一个开始判断
        return self.solve1(len(nums) - 1, nums)

    def tui(self, nums):
        """
        从头开始遍历

        不用递归，使用for循环递推

        此时，result记录的是从从位置0迭代到当前位置时的结果值

        :param nums:
        :return:
        """
        if len(nums) == 0:  # 考虑输入为空情况
            return 0

        if len(nums) == 1:  # 考虑输入为1个的情况
            return nums[0]

        self.result[0] = nums[0]  # 第一位置时的结果
        self.result[1] = max(nums[0], nums[1])  # 第二位置时的结果

        n = len(nums)
        # 从第三位置开始用for循环
        for i in range(2, n):
            self.result[i] = max(nums[i] + self.result[i - 2], self.result[i - 1])

        return self.result[n - 1]

    def fei(self, num):
        if num <= 1:
            return 1
        return self.fei(num - 1) + self.fei(num - 2)


if __name__ == '__main__':
    so = Solusion()
    # print(so.tui([1,2,3]))
    print(so.fei(10))