def bubble_sort(alist):
    """冒泡排序，右部先有序"""
    n = len(alist)
    for i in range(n - 1):
        count = 0
        for j in range(0, n - 1 - i):
            if alist[j] > alist[j + 1]:
                count = 1
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
        # 如果从到到尾没有发生一次交换操作，则说明已经是排好序的，可以直接退出
        if count == 0:
            break
    return alist

def quick_sort(alist, first, last):
    """快速排序，（不断选出一个中间值，类似于二分搜索）
    """

    if first >= last:
        return

    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # high左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    # 从循环退出时，low==high
    alist[low] = mid_value
    # 对low左边的列表执行快速排序
    quick_sort(alist, first, low - 1)
    # 对low右边的列表排序
    quick_sort(alist, low + 1, last)


def insert_sort(alist):
    """插入排序(本质是左边先局部排序)
    内层循环中，必须要从右到左遍历，因为新加入的值必须要先比较，才能间接的与内循环中的所有的进行比较
    """

    for i in range(1,len(alist)):
        while i>=1:
            if alist[i]<alist[i-1]:
                alist[i],alist[i - 1] = alist[i-1], alist[i]
                i -= 1
            else:
                break





def qui(nums):



    def robot(i,j):
        if i>=j:
            return


        first_num = nums[i]

        low = i
        hight = j

        while low<hight:
            while low < hight and nums[hight]>first_num:
                hight -= 1
            nums[low] = nums[hight]

            while low<hight and nums[low]<=first_num:
                low += 1

            nums[hight] = nums[low]


        nums[low] = first_num
        robot(i,low-1)
        robot(low+1,j)

    robot(0,len(nums)-1)

a = [12, 45, 78, 9, 6, 2, 4, 32, 55]
# qui(a)
# print(a)


def merge_sort(arr):
    """
    归并排序
    """

    n = len(arr)

    if n < 2:  # 如果数组中的元素为1个，则直接返回这个数组，不要再分割了，否则，继续分割
        return arr

    middle = n // 2

    # 对左侧的数据进行排序
    left = merge_sort(arr[:middle])
    # 对右侧的数据进行排序
    right = merge_sort(arr[middle:])

    # 对左右两边排序好的数据做一个合并的操作
    result = []
    left_n = len(left)
    right_n = len(right)
    i = 0
    j = 0
    while i < left_n and j < right_n:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < left_n:
        result.append(left[i])
        i += 1
    while j < right_n:
        result.append(right[j])
        j += 1
    return result

def merge_sort02(nums):
    n = len(nums)
    if n<2:
        return nums

    mid = n//2


    left = merge_sort02(nums[:mid])
    right = merge_sort02(nums[mid:])

    i = 0
    j = 0
    res = []

    left_n = len(left)
    right_n = len(right)

    while i<left_n and j<right_n:

        if left[i]<=right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i<left_n:
        res.append(left[i])
        i += 1
    while j<right_n:
        res.append(right[j])
        j += 1
    return res


if __name__ == '__main__':
    li = [12, 45, 78, 9, 6, 2, 4, 32, 55]
    print(merge_sort02(li))
