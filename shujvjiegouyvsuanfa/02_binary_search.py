def binary_search_1(alist, item):
    """二分查找，递归版本"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search_1(alist[:mid], item)
        else:
            return binary_search_1(alist[mid + 1:], item)
    return False

def binary_search_2(alist, item):
    """二分查找，指针版本"""
    first = 0
    last = len(alist) - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return mid
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return -1




def array_binary_search(nums,target):

    def find_idx(l,r):

        mid = (r - l) // 2 + l
        tmp = nums[mid]

        # if nums[l]>nums[r]:


# 二分搜索变形之：查找升序数组中target第一次出现和最后一次出现时的索引位置
def test01(nums,target):

    def search_lower_bound(alist, item):
        l = 0
        r = len(alist) - 1
        while l <= r:
            mid = l +( r-l) // 2
            if alist[mid] == item and (mid==0 or alist[mid-1]<item):
                return mid
            elif alist[mid] >= item:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def search_upper_bound(alist, item):
        l = 0
        r = len(alist) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if alist[mid] == item and (mid==len(alist)-1 or alist[mid+1]>item):
                return mid
            elif alist[mid] <= item:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    a = search_lower_bound(nums,target)
    b = search_upper_bound(nums,target)
    return [a,b]


# 二分搜索变形之：查找第一个大于target的位置
def test02(nums,target):

    def search_one(alist, item):
        l = 0
        r = len(alist) - 1
        while l <= r:
            mid = l +( r-l) // 2
            if alist[mid] > item and (mid==0 or alist[mid-1]<=item):
                return mid
            elif alist[mid] < item:
                l = mid + 1
            elif alist[mid] > item:
                r = mid - 1
            elif alist[mid] == item:
                l = mid + 1
        return -1
    return search_one(nums,target)

# 二分搜索变形之：查找target在升序变形数组中的位置
def test03(nums,target):

    def search_one(nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l +(r-l) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if nums[mid]>target>=nums[l]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid]<target<=nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    return search_one(nums,target)







if __name__ == '__main__':
    li = [65,78,98,1,2,3,6]
    print(test03(li,3))