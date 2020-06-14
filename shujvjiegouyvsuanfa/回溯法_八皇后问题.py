
"""8*8表格放8个皇后，不能同行或同列或同斜线，试问，有多少中放法？"""

def eight_queens003(n=5,A=[None]*5,cur=0):

    if cur>=5:
        return 0
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
        if flag == 1:
            continue
        else:
            count = eight_queens003(n,A,cur+1) + 1

    return count















def eight_queens(n=8,A=[None]*8,cur=0):
    """每一行每一列有且只能放一个，在斜线方向上暂时不确定"""


    if cur==n:
        return 1

    count = 0


    # cur表示为在行号为cur上放置当前一个皇后

    for col in range(n): # 遍历列索引值
        A[cur] = col # 表示在cur行col列放置

        flag = 0
        # 验证当前列放置后，是否与之前的同对角线或者同列
        for row in range(cur):  # 遍历前面几个放好的行号
            if abs(col-A[row]) == cur-row or col==A[row]:
                flag = 1
                break


        if flag == 0:
            count += eight_queens(8,A,cur+1)


        # 在放置当前列的前提下，进行下一个第二行皇后的放置

    return count

def eight_queens2(n=8,A=[None]*8,cur=0):

    if cur==n:
        print(A)
        return 1

    count = 0  # 只有所有的函数进入时，count初始为0，当达到边界条件收尾之后，上一级的，会收取下一级中的count总数；
                # 所以，即便多次初始为0，最后收尾入口函数的仍然能汇总出一个总和

    for col in range(n):

        A[cur] = col
        flag = True
        for row in range(cur):
            if abs(col-A[row])==cur-row or col==A[row]:
                flag = False
                break

        if flag:
            count += eight_queens2(8,A,cur+1)
    return count

def eight_queens3(n=5,A=[None]*5,cur=0):
    if cur==n:
        print(A)
        return 1

    count = 0

    for col in range(n):

        A[cur] = col
        flag=True
        for row in range(cur):
            if abs(col-A[row])==cur-row or col==A[row]:
                flag=False
                break
        if flag:
            count += eight_queens3(n,A,cur+1)

    return count




class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
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


        return eight_queens003(n,[None]*n,0)


print("第三次编写结果为：",Solution().totalNQueens(4))

