
"""
772. 基本计算器 III
实现一个基本的计算器来计算简单的表达式字符串。

表达式字符串可以包含左括号 ( 和右括号 )，加号 + 和减号 -，非负 整数和空格 。

表达式字符串只包含非负整数， +, -, *, / 操作符，左括号 ( ，右括号 )和空格 。整数除法需要向下截断。

你可以假定给定的字符串总是有效的。所有的中间结果的范围为 [-2147483648, 2147483647]。
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 遍历数字如果是加减，就转为正负号放入栈中，如果遇到乘除，就两个运算后结果放入栈中，最后，将栈中的值累加。

        my_nums = []
        my_ope = []
        tmp = ""
        for i in range(len(s)):

            if s[i].isdigit():
                tmp += s[i]
            elif  s[i] != " ":
                if s[i] == "+":
                    if len(tmp)!=0: my_nums.append(tmp)
                    my_ope.append("+")
                    tmp = ""
                elif s[i] == "-":
                    if len(tmp) != 0: my_nums.append(tmp)
                    my_ope.append("-")
                    tmp = ""
                elif s[i] == "*":
                    if len(tmp) != 0: my_nums.append(tmp)
                    my_ope.append("*")
                    tmp = ""
                elif s[i] == "/":
                    if len(tmp) != 0: my_nums.append(tmp)
                    my_ope.append("/")
                    tmp = ""
                elif s[i] == "(":
                    if len(tmp) != 0: my_nums.append(tmp)
                    my_ope.append("(")
                    tmp = ""
                elif s[i] == ")":
                    if len(tmp) != 0: my_nums.append(tmp)
                    my_ope.append(")")
                    tmp = ""
        if len(tmp) != 0: my_nums.append(tmp)




# print(Solution().calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))


def mytest(str01):
    """
    只有加法
    """
    num = 0  # 存放当前值
    sum = 0  # 存放相加后的和

    for i in range(len(str01)):

        if str01[i].isdigit():
            num = 10*num + int(str01[i])
        else:
            sum += num
            num = 0
    sum += num
    return sum

# print(mytest("8+9+4"))

def mytest02(str01):
    """有加号和减号"""


    str01 = str01+"+"

    sign = "+"
    num = 0
    sum = 0

    for i in range(len(str01)):

        if str01[i].isdigit():
            num = 10*num + int(str01[i])
        else:

            if sign=="+":
                sum += num
            elif sign=="-":
                sum -= num
            num = 0
            sign = str01[i]
    return sum

# print(mytest02("8-4+2-6"))

def mytest03(str01):
    """包含加减乘除"""

    stack = []
    num = 0
    sign = "+" # 存放的是当前数值的前面的符号
    str01 = str01+"+"

    for i in range(len(str01)):

        if str01[i].isdigit():
            num = 10*num + int(str01[i])
        else:

            if sign=="+":
                stack.append(num)
            elif sign=="-":
                stack.append(-num)
            elif sign=="*":
                tmp = stack[-1]
                stack[-1] = tmp*num
            elif sign=="/":
                stack[-1] = stack[-1] // num
            num = 0
            sign = str01[i]
    sum = 0
    for j in stack:
        sum += j
    return sum
# print(mytest03("8*9+6*2"))

def search(str01):
    stack = []
    num = 0
    sign = "+"  # 存放的是当前数值的前面的符号

    for i in range(len(str01)):

        if str01[i].isdigit():
            num = 10 * num + int(str01[i])
        else:


            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                tmp = stack[-1]
                stack[-1] = tmp * num
            elif sign == "/":
                stack[-1] = stack[-1] // num
            elif str01[i] == "(":
                num = search(str01[i + 1:])
                stack.append(num)
            num = 0
            sign = str01[i]
            if str01[i]==")":
                break
    sum = 0
    for j in stack:
        sum += j
    return sum

print(search("8*(8+10)+"))






