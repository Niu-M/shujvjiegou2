

def binary_search(nums,target,left=0,right=None):

    if right is None:
        right = len(nums)-1

    if left>right:
        return -1

    mid = (right+left)//2
    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        return binary_search(nums,target,left=mid+1,right=right)
    else:
        return binary_search(nums,target,left=left,right=mid-1)

# print(binary_search([1,4,8,21,65,74,99,145,625,879],21))


# 分治法
def fz(nums,target,left=0,right=None):
    """使用分治法，类似于归并排序，首选不断的进行二分割，界限是左边界等于右边界"""
    if right is None:
        right = len(nums)-1

    if left >= right:
        if nums[left] == target:
            return left
        else:
            return -1

    mid = (right+left)//2
    if nums[mid] == target:
        return mid


    left_idx = fz(nums, target, left=left, right=mid - 1)


    right_idx = fz(nums, target, left=mid+1, right=right)

    idx = max(left_idx,right_idx)
    return idx

# print(fz([1,4,8,21,45,89,74,52,65,52,56],45))

def sqrt_X(x):
    """使用二分查找法，找到根号下X的整数部分"""

    if x==0:
        return 0


    def f(left=0,right=None):

        if right-left==1:
            if right*right<=x:
                return right
            else:
                return left
        elif right-left<1:
            return right
        mid = (left+right)//2

        if mid*mid==x:
            return mid
        elif mid*mid>x:
            return f(left,mid-1)
        else:
            return f(mid,right)


    return f(0,x)

print(sqrt_X(16))

















