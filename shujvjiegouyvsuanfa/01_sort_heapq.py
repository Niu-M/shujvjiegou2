"""
堆排序
"""


# 交换一个数组中的两个元素的位置
def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]


# 从堆顶开始(i=0)，调整成大根堆（从前往后比较并调整父子节点位置）
def heapify(arr,i,size):

    # 获取第二层的两个节点索引
    l = 2*i+1
    r = 2*i+2

    while l<size:

        if arr[l]<arr[r] and r<size:
            largest = r
        else:
            largest = l

        if arr[largest]<arr[i]:
            largest = i

        if i==largest:
            break

        swap(arr,i,largest)

        i = largest
        l = 2 * i + 1
        r = 2 * i + 2

# 用于初始化构造大根堆（从后往前比较并调整父子节点位置）
def buildMaxHeap(arr):

    for i in range(len(arr)):
        cur = i
        father = (cur-1)//2  # 获取当前节点的父节点索引
        while arr[cur]>arr[father]:
            swap(arr,cur,father)
            cur = father
            father = (cur-1)//2
            if father<0:
                break


def heap_sort(arr):
    n = len(arr)
    buildMaxHeap(arr)  # （从后往前比较并调整父子节点位置）初始化构造大根堆
    while n>1:  # 不断的筛选出一个个最大值，直到全部筛选出来
        swap(arr,0,n-1)  # 将最大值放在末尾
        n -= 1
        heapify(arr,0,n) # （从前往后比较并调整父子节点位置）将前面部分，通过从上而下的方式，调整至大根堆结构
    return arr
arr = [4,8,6,9,52,32,7,12,11]
heap_sort(arr)
print(arr)


