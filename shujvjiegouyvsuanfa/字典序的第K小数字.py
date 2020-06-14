

def f01(n,k):

    dict_count = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}

    for i in range(1,n+1):

        dict_count[str(i)[0]] += 1

    a = k
    for key,v  in dict_count.items():

        if a - v == 0: # 说明在当前键k对应的最后一个值
            if v==1:
                return int(key)
            elif v>1:

                while int(key)<n:
                    key += "9"
                while int(key)==n:
                    return int(key)
                while int(key)>n:
                    key -= 1
                return int(key)
        elif a - v > 0:
            a = a-v
        elif a-v<0:

            while int(key) < n:
                key += "9"
            while int(key) == n:
                return int(key)
            while int(key) > n:
                key = int(key)-1
            return int(key)






class Solution:
    def findKthNumber(self, n, k):
        cur = 1  # 从1开始，增加到k为止，对应的数就是结果值
        prefix = 1

        while cur <k:

            cnt = self.get_count(prefix,n)  # 获取前缀为prefix，不大于n，数值的个数

            if cur + cnt >k: # 如果该前缀内中目标值
                prefix *= 10
                cur += 1
            else:    # 确定好前缀后，一个个加上去
                prefix += 1
                cur += cnt
        return prefix






    def get_count(self, i, n):

        if i <= n:
            cnt = 1
        else:
            return 0

        a = i
        b = i + 1

        while True:
            a = a * 10
            b = b * 10
            if n >= b:
                cnt += b - a
            elif n >= a:
                cnt += n - a + 1
            else:
                break
        return cnt
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None







