class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s)==0:
            return 0

        res = []



        def search(i,list01):

            if i>=len(s):
                res.append(len(list01))
                return
            if s[i] in list01:
                res.append(len(list01))
                return

            list01.append(s[i])
            search(i+1,list01)
        for i in range(len(s)):
            search(i,[])
        return max(res)

class Solution02(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """


        my_list = []
        max_len = 0
        for i in range(len(s)):

            if s[i] in my_list:
                idx = my_list.index(s[i])
                del my_list[0:idx+1]

            my_list.append(s[i])
            max_len = max(max_len,len(my_list))
        return max_len













print(Solution02().lengthOfLongestSubstring("pwwkew"))


