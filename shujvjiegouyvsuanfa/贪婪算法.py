"""

253.会议室||
有给定一系列会议的起始时间和结束时间，求最少需要多少个会议室就可以让这些会议顺利召开。
输入: [[0, 30],[5, 10],[15, 20]]
输出: 2
"""
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        nums = intervals

        def my_sort(nums):
            for i in range(len(nums)):
                flag = 0
                for j in range(0,len(nums)-i-1):
                    if nums[j][0]>nums[j+1][0]:
                        flag = 1
                        nums[j],nums[j+1] = nums[j+1],nums[j]
                if flag==0:
                    break
        my_sort(nums)


        res = []

        res.append(nums[0])
        i = 1
        while i<len(nums):

            flag = 0
            for j in range(len(res)):

                if nums[i][0]>=res[j][1]:
                    res[j] = nums[i]
                    flag = 1
                    break
            if flag==0:
                res.append(nums[i])

            i += 1
        return len(res)

a = [[0, 30],[55, 10],[15, 20]]
# a = [[13,15],[1,13]]
# print(Solution().minMeetingRooms(a))
# print(a.sort(key=lambda i:i[0]))

import heapq


print(sorted(a,key=lambda i:i[0]))
print(a)