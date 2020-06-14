

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        n = len(heights)


        def f(num,i,count):
            if i==n :
                return count


            if num<=heights[i]:
                return f(num,i+1,count+1)
            else:
                return count
        def f2(num,i,count):
            if i==-1 :
                return count

            if num<=heights[i]:
                return f2(num,i-1,count+1)
            else:
                return count
        max_val = -1
        for i in range(n):
            tmp1 = f(heights[i],i,0)
            tmp2 = f2(heights[i],i-1,0)

            tmp_count = tmp1+tmp2


            tmp = tmp_count*heights[i]
            # print(tmp)
            if tmp>max_val:
                max_val = tmp
        return max_val

print(Solution().largestRectangleArea([1,1]))

