"""
给一个无序数组，找到其中的最长上升子序列（元素可以不紧挨着），返回该子序列长度
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

"""

def aa(nums):


    result = []
    def f(idx1,idx2,s):

        if idx2>=len(nums):
            result.append(len(s))
            return 0

        if nums[idx1]<nums[idx2]:
            f(idx1, idx2 + 1, s)
            s.append(nums[idx2])
            f(idx2,idx2+1,s)
        else:
            f(idx1,idx2+1,s)


    for i in range(len(nums)):
        s = [nums[i]]
        f(i,i+1,s)
    print(result)
    result.sort()
    return result[-1]

a = [10,9,2,5,3,7,101,18]
print(aa(a))


# Dynamic programming.
class Solution:
    def lengthOfLIS(self, nums):
        if nums == [] :
            return 0

        dp = [1] * len(nums)  # 初始化一个列表，用于存放以各个位置结尾时，
                              # 的各个上升子序列的长度中，最大的长度

        for i in range(len(nums)): # 从各个位置开始

            for j in range(i):
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# Dynamic programming.
class Solution3:
    def lengthOfLIS(self, nums):



        n = len(nums)
        dp = [1]*n

        for i in range(n):

            for j in range(i):

                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)

        return max(dp)








class Solution(object):

    def robot(self, idx, nums):
        """
        定义一个用于搜索的迭代方法，方法的返回值是指针处时的结果值（子序列长度）
        """
        # 设置递归边界条件
        if idx < 0:  # 当索引到头时，返回0，表示长度加0
            return 0
        ans = 0
        # 从0遍历到idx位置
        for i in range(idx):  # 虽然传入的是最大索引，但此处表明了，递归还是从头开始的！！！

            # 当被遍历到的值小于指针idx处的值时，递归调用该方法，且idx更新为i
            # if nums[i] < nums[idx]:
            # 加入去掉前大于后的判断，就不是找递增子序列了
            ans = max(ans, self.robot(i, nums))  # 每次递归，判断并更新历史最大结果值

        return ans + 1  # 返回的结果值要加上当前指针处的一个位置

    def lengthOfLIS(self, nums):

        nums.append(10000000000)  # 在最后添加一个很大的数，为了从最后一个开始搜索且留住最后一个

        return self.robot(len(nums) - 1, nums) - 1  # 传入索引从最大开始，表示从后往前搜索（因为人为加了一个值，所以最后要减掉）

# a = 4
# print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))



class Solution2(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # for i in range(len(nums)-1,0,-1):
        #
        #     if nums[i]>nums[i-1]:
        #         nums[i] ,nums[i - 1] = nums[i-1], nums[i]
        #         return nums

        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                res_nums = nums[i:]
                res_nums.sort()
                nums[i:] = res_nums
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        break
                return
        nums.sort()

        return nums

def eight_queens003(n,A,cur):

    if cur==n:
        return 1
    count = 0

    for i in range(n):

        # 假设对于行号cur，放在列i上
        A[cur] = i

        flag = 0
        # 判断是否同列或同斜线
        for j in range(cur):

            if A[j] == i or abs(A[cur]-i) == cur-j:
                flag = 1
                break
        if flag == 0:
            count += eight_queens003(n, A, cur + 1)


    return count
