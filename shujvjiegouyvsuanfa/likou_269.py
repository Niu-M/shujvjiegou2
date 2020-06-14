"""
269. 火星词典
现有一种使用字母的全新语言，这门语言的字母顺序与英语顺序不同。

假设，您并不知道其中字母之间的先后顺序。但是，会收到词典中获得一个 不为空的 单词列表。因为是从词典中获得的，所以该单词列表内的单词已经 按这门新语言的字母顺序进行了排序。

您需要根据这个输入的列表，还原出此语言中已知的字母顺序。
"""

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        res = []  # 用于存放一对对字符顺序
        for i in range(1,len(words)):

            a = words[i-1]
            b = words[i]

            min_len = min(len(a),len(b))

            for j in range(min_len):

                if a[j] != b[j]:
                    res.append((a[j],b[j]))
                    break
        print(res)
        my_dict = {} # 用于存放各个字符的入度值

        for i in res:
            my_dict[i[0]] = 0
            my_dict[i[1]] = 0
        for i_tuple in res:
            my_dict[i_tuple[1]] += 1

        result = [] # 存放结果顺序
        n = len(my_dict)
        print(my_dict)
        while len(result)<n:
            key_1 = ""
            flag = 1
            for key, value in my_dict.items():

                if value==0:
                    result.append(key)
                    key_1 = key
                    del my_dict[key_1]
                    flag = 0
                    break
            if flag==1:
                # a = ""
                # for i in my_dict.keys():
                #     a += i
                # return a
                return ""

            # 更新入度值
            for i_tuple in res:
                if i_tuple[0] == key_1:
                    my_dict[i_tuple[1]] -= 1

        return "".join(result)

a = ["z","x","z"]
print(Solution().alienOrder(a))