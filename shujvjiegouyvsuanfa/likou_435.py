"""
435. 无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals)==0:
            return 0

        import copy
        intervals.sort(key=lambda i:[i[0],i[1]])
        print(intervals)
        status = {}

        def search(i,tmp,inter):
            if i==len(inter):
                return tmp
            str01 = ""
            for indx in inter:
                str01 = str01 + "_"+str(indx[0])+"-"+str(indx[1])

            if str(i)+"-"+str(tmp)+"-"+str01 in status:
                return status[str(i)+"-"+str(tmp)+"-"+str01]

            a = float("inf")
            b = float("inf")

            if inter[i][0]<inter[i-1][1]:
                del inter[i]
                a = search(i,tmp+1,inter)
            else:
                tmp_inter = copy.copy(inter)
                del inter[i]
                b = min(search(i,tmp+1,inter),search(i+1,tmp,tmp_inter))
            status[str(i)+"-"+str(tmp)+"-"+str01] = min(a,b)
            return status[str(i)+"-"+str(tmp)+"-"+str01]

        res = 0
        while True:
            tmp = search(1, 0, intervals)
            res = res + tmp
            if tmp == 0:
                return res


class Solution02(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda i:i[1])

        end = -float("inf")









class Solution03(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals)==0:
            return 0

        import copy
        intervals.sort(key=lambda i:[i[0],i[1]])
        print(intervals)
        status = {}

        def search(i,tmp,inter):
            if i==len(inter):
                return tmp
            tu = ""
            for i_idx in inter:
                tu += str(hash(tuple(i_idx)))+"-"

            if str(i)+"-"+str(tmp)+"-"+str(tu) in status:
                return status[str(i)+"-"+str(tmp)+"-"+str(tu)]

            a = float("inf")
            b = float("inf")

            if inter[i][0]<inter[i-1][1]:
                if inter[i][1]>inter[i-1][1]:
                    del inter[i]
                else:
                    del inter[i-1]
                a = search(i,tmp+1,inter)
            else:
                b = search(i+1,tmp,inter)
            status[str(i)+"-"+str(tmp)+"-"+str(tu)] = min(a,b)
            return status[str(i)+"-"+str(tmp)+"-"+str(tu)]

        res = 0
        while True:
            tmp = search(1, 0, intervals)
            res = res + tmp
            if tmp == 0:
                return res
# a = [ [1,2], [2,3], [3,4], [1,3] ]
a = [[0,2],[1,3],[2,4],[3,5],[4,6]]
print(Solution03().eraseOverlapIntervals(a))