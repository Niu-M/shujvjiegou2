

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row_list = []
        row = 0
        flag=1
        for i in range(len(s)):

            row_list.append(row)

            if flag==1:
                row += 1
            else:
                row -= 1


            if row==numRows-1:
                flag = 0
            if row==0 and flag==0:
                flag=1
        res = ''
        print(row_list)
        import numpy as np
        a = np.argsort(row_list,kind="mergesort")
        print(a)
        s_list = np.array(list(s))
        b = s_list[a]
        res = "".join(b)
        return res
s = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers"

# zhuy1111111111111111
print(Solution().convert(s,2))
