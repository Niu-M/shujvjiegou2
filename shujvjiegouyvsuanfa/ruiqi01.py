


def binary_search(nums,first,last,target):

    l = first
    r = last


    while l<=r:

        mid = (r-l)//2+l

        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def get_all_combs(array, target):
    res = []
    for i in range(len(array)-1):
        if array[i]>target//2+1:
            break
        idx = binary_search(array[i+1:],0,len(array)-2-i,target-array[i])
        if idx != -1:
            res.append((array[i],array[idx]))

    return res














if __name__ == '__main__':
    # li = [1,2,3,6,65,78,98]
    # print(binary_search(li,0,len(li)-1,3))
    # a = li
    # print(a.pop(),a,li)
    array = [2, 3, 4, 7, 10, 12]
    print(get_all_combs(array,14))