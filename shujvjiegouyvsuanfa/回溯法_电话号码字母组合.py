
class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        output = []

        def backtrack(combination,next_digits):

            if len(next_digits) == 0:  # 当数字遍历完后，将当前字母组合放入结果列表中
                output.append(combination)
            else:

                # 如果后续有数字没有遍历，则遍历取出其各个字母，形成各个新的字母组合
                for letter in phone[next_digits[0]]:
                    backtrack(combination+letter,next_digits[1:])

        if digits:
            backtrack("",digits)
        return output

    def f2(self,digit):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        output = []


        def zuhe(combi,digit):

            if len(digit)==0:
                output.append(combi)
            else:
                for letter in phone[digit[0]]:
                    zuhe(combi+letter,digit[1:])

        if digit:
            zuhe("",digit)
        return output

def letterCombinations(digits):
    n = len(digits)
    if n == 0:
        return []
    A = [None] * n
    chars = ["q", "a", "z", "w", "s", "x", "e", "d",
             "c", "r", "f", "v", "t", "g", "b", "y",
             "h", "n", "u", "j", "m", "i", "k", "o",
             "l", "p"]
    number_2_chars = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }


    def f1(cur):
        if cur == n:
            return ["".join(A)]
        result = []
        for char in chars:

            A[cur] = char

            if char in number_2_chars[digits[cur]]:

                tmp = f1(cur+1)

                for i in tmp:
                    result.append(i)
        return result
    return f1(0)

print(letterCombinations("45"))
# print(Solution().f2("459"))
