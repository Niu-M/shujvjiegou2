def binarySearch(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

def find_begin(array, l, r):
    if r - l <= 1:
        return r
    middle = (r + l) // 2
    if array[l] > array[middle]:
        return find_begin(array, l, middle)
    else:
        return find_begin(array, middle, r)

def find_num(array, num):
    index = find_begin(array, 0, len(array) - 1)
    a = array[index:] + array[:index]
    index = binarySearch(array, 0, len(a) - 1, num)
    return index


def binarySearch02(nums, l, r, x):
    if l > r:
        return -1

    mid = l + (r - l) // 2

    if nums[mid] == x:
        return mid

    if nums[mid] >= nums[l]:

        if x > nums[mid]:
            return binarySearch(nums, mid + 1, r, x)
        else:
            return binarySearch(nums, l, mid - 1, x)
    else:

        if x >= nums[l]:
            return binarySearch(nums, l, mid - 1, x)
        else:
            return binarySearch(nums, mid + 1, r, x)


if __name__ == '__main__':
    a = [9,10,12,24,34,2,3,6]

    print(binarySearch02(a,0,len(a)-1,2))


