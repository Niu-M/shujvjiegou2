"""

单调双端队列：放入里面的元素值一定是从左向右递减的，

操作步骤：
（1）依次逐个遍历原数组中的值，遍历取出来一个a；
（2）查看双端队列左侧是否有超出窗口长度的元素，如果有，逐个删除一个；
（3）从右侧查看是否有比a小的元素，如果有，则删除；
（4）将a放入双端对列的右侧；
（5）返回左侧第一个元素值，作为当前窗口中的最大值。



"""
import operator
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        my_dict = {}

        for idx,list_tmp in enumerate(graph):
            flag = [i for i in range(len(graph))]
            flag.remove(idx)
            for i in range(len(list_tmp)):
                flag.remove(list_tmp[i])
            my_dict[idx] = flag

        a = []
        count = 0
        for i in my_dict.values():
            i.append(count)
            a.append(i)
            count += 1
        b = []
        for i in a:
            i = sorted(i)
            b.append(i)
        for i in range(len(b)-1):
            for j in range(i+1,len(b)):
                operator.eq(b[i],b[j])

        return True





print(Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))




