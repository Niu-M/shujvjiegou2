"""
215. 数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，
而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k==1:
            nums.sort()
            return nums[-1]

        tar_idx = len(nums)-k

        def quickly_sort(nums,left,right):

            if left>=right:
                return -1

            mid_value = nums[right]
            low = left
            high = right

            while low<high:

                while low<high and nums[low]<=mid_value:
                    low += 1
                nums[high] = nums[low]
                while low<high and nums[high]>=mid_value:
                    high -= 1
                nums[low] = nums[high]
            nums[low] = mid_value

            if low ==tar_idx:
                return nums[low]
            elif low < tar_idx:
                return quickly_sort(nums,low+1,right)
            else:
                return quickly_sort(nums,left,low-1)
        return quickly_sort(nums,0,len(nums)-1)


class Solution02(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k==1:
            nums.sort()
            return nums[-1]

        if k<=len(nums)//2:
            while True:

                for i in range(len(nums)-1):
                    if i==k:
                        return nums[-k]
                    for j in range(len(nums)-i-1):

                        if nums[j]>nums[j+1]:
                            nums[j+1] ,nums[j] = nums[j],nums[j+1]
        else:
            while True:

                for i in range(len(nums) - 1):

                    for j in range(len(nums) - i - 1):

                        if nums[j] < nums[j + 1]:
                            nums[j + 1], nums[j] = nums[j], nums[j + 1]
                    if i == len(nums)-k:
                        return nums[-len(nums)+k-1]
class Solution03(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq

        heapq.heapify(nums)



        return heapq.nlargest(k,nums)[0]


nums = [2, 1]

k = 2
print(Solution03().findKthLargest(nums,k))







