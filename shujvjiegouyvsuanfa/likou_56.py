"""
56. 合并区间
给出一个区间的集合，请合并所有重叠的区间

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda i:i[0])



        j=0
        while j<len(intervals)-1:

            cur_end = intervals[j][1]

            i = j+1
            while i<len(intervals):

                if intervals[i][1]>=cur_end>=intervals[i][0]:
                    tmp_end = intervals[i][1]
                    del intervals[i]
                    intervals[j][1] = tmp_end
                    cur_end = tmp_end
                    i -= 1
                elif cur_end>intervals[i][1]:
                    del intervals[i]
                    i -= 1
                i += 1
            j += 1

        return intervals



# a = [[1,3],[2,6],[8,10],[15,18]]
a = [[1,4],[0,2],[3,5]]
print(Solution().merge(a))