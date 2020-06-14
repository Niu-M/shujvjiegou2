# 二分搜索变形之：查找target在升序变形数组中的位置
def t003(nums,target):

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
    nums = [9, 10, 12, 24, 34, 2, 3, 6]

    print(t003(nums,24))

