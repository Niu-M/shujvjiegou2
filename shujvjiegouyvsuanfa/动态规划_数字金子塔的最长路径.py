


def maxDis(arr):

    # arr = [
    #     [7],
    #     [3, 8],
    #     [8, 1, 0],
    #     [2, 7, 4, 4],
    #     [4, 5, 2, 6, 5],
    # ]
    n = len(arr)-1
    import numpy as np
    status = np.ones((n+1,n+1))*-1

    def f(i,j):
        if i == len(arr)-1:
            status[i][j] = arr[i][j]
            return status[i][j]

        if status[i][j] != -1:
            return status[i][j]

        left = f(i+1,j)
        right = f(i+1,j+1)
        status[i][j] = max(left,right)+arr[i][j]

        return status[i][j]
    return f(0,0)



def maxDis02(arr):

    # arr = [
    #     [7],
    #     [3, 8],
    #     [8, 1, 0],
    #     [2, 7, 4, 4],
    #     [4, 5, 2, 6, 5],
    # ]

    n = len(arr)

    status = {}
    def a(i,j):
        if str(i)+"-"+str(j) in status:
            return status[str(i)+"-"+str(j)]

        if i>n-1 :
            return 0
        status[str(i)+"-"+str(j)] = max(a(i+1,j),a(i+1,j+1)) + arr[i][j]
        return status[str(i)+"-"+str(j)]

    return a(0,0)
if __name__ == '__main__':
    arr = [
        [7],
        [3, 8],
        [8, 1, 0],
        [2, 7, 4, 4],
        [4, 5, 2, 6, 5],
    ]


    print(maxDis02(arr))