class Solution(object):
    def maxSumDivThree(self, nums):
        """
        1262. 可被三整除的最大和
        :type nums: List[int]
        :rtype: int
        """


        sta = {}
        def f1(i):
            if str(i) in sta:
                return sta[str(i)]

            if i==len(nums):
                return 0
            a = 0
            b = 0

            if (f1(i-1)+nums[i]) % 3 == 0:
                a = max(f1(i-1) + nums[i],f1(i-1))
            else:
                b = f1(i-1)

            sta[str(i)] = max(a,b)
            return sta[str(i)]

        res = 0
        for i in range(1,len(nums)):
            res = f1(i)


        return res

# print(Solution().maxSumDivThree([3,6,5,1,8]))



def f0001(nums):

    dp = [0, float('-inf'), float('-inf')] # 初始化结果存储矩阵

    for n in nums:
        """
        1、元素值一个一个遍历出来；
        2、对于当前元素值，如果满足条件，就放入结果中，如果不满足条件，就暂存起来；
        
        """

        # for i in range(3):
        #     dp[i] = max(dp[i], dp[(i+n)%3]+n)

        dp = [max(dp[i], dp[(i + n) % 3] + n) for i in range(3)]

    return dp[0]

# print(f0001([3,6,5,1,8]))




# class Solution01 {
# public:
#     int maxSumDivThree(vector<int>& nums) {
#        int n = nums.size();
# 	vector<vector<int>> dp(n + 1, vector<int>(3, 0));
# 	dp[0][0] = 0; dp[0][1] = INT_MIN; dp[0][2] = INT_MIN;
#
#
# 	for (int i = 1; i <= n; i++) {
# 		if (nums[i - 1] % 3 == 0) {
# 			dp[i][0] = max(dp[i - 1][0], dp[i - 1][0] + nums[i - 1]);
# 			dp[i][1] = max(dp[i - 1][1], dp[i - 1][1] + nums[i - 1]);
# 			dp[i][2] = max(dp[i - 1][2], dp[i - 1][2] + nums[i - 1]);
# 		}
# 		else if (nums[i - 1] % 3 == 1) {
# 			dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] + nums[i - 1]);
# 			dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + nums[i - 1]);
# 			dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + nums[i - 1]);
# 		}
# 		else if (nums[i - 1] % 3 == 2) {
# 			dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + nums[i - 1]);
# 			dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] + nums[i - 1]);
# 			dp[i][2] = max(dp[i - 1][2], dp[i - 1][0] + nums[i - 1]);
# 		}
# 	}
# 	return dp[n][0];
#     }
# };


class Solution:

    def maxSumDivThree(self, nums) -> int:

        all_sum = sum(nums)
        r = all_sum % 3
        if r == 0:
            return all_sum

        ones = list()
        twos = list()
        for num in nums:
            if num % 3 == 0:
                continue
            elif num % 3 == 1:
                ones.append(num)
            else:
                twos.append(num)
        ones.sort()
        twos.sort()

        subtract = list()
        if r == 1:
            if ones:
                subtract.append(ones[0])
            if len(twos) >= 2:
                subtract.append(sum(twos[:2]))
            if not subtract:
                return 0
            else:
                return all_sum - min(subtract)
        else:
            if twos:
                subtract.append(twos[0])
            if len(ones) >= 2:
                subtract.append(sum(ones[:2]))
            if not subtract:
                return 0
            else:
                return all_sum - min(subtract)


def f01(nums):


    a = sum(nums)

    if a%3==0:
        return a

    mo = a % 3

    mo_1 = []
    mo_2 = []

    for n in nums:
        if n%3 == 1:
            mo_1.append(n)
        elif n%3 == 2:
            mo_2.append(n)
    mo_2.sort()
    mo_1.sort()

    if mo == 1 and len(mo_1)>0:
        return a-mo_1[0]
    elif mo == 1 and len(mo_1)==0:
        return 0
    elif mo == 2 and len(mo_1)>1 and len(mo_2)>0:
        return max(a-mo_1[0]-mo_1[1],a-mo_2[0])
    elif mo == 2 and len(mo_1)<=1 and len(mo_2)>0:
        return a-mo_2[0]
    elif mo == 2 and len(mo_1) > 1 and len(mo_2) <= 0:
        return a-mo_1[0]-mo_1[1]
    else:
        return 0

print(f01([2,6,2,2,7]))



