"""
两种方法实现深度优先搜索：
（1）递归
（2）非递归，使用栈



"""

def my_test(maze,x,y,B):

    if x==B[0] and y==B[1]:
        return True

    maze[x][y] = -1

    for i in range(4):
        x_i = x + 1

