# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.flag = True

        def search(node1):
            if not node1:
                return 0

            l = search(node1.left) + 1
            r = search(node1.right) + 1

            if abs(l-r)>1:
                self.flag = False
            return max(l,r)
        search(root)
        return self.flag

def binarySearch(nums,l,r,x):

    if l>r:
        return -1
    mid = int(l + (r-l)/2)


    if nums[mid] == x:
        return mid
    elif nums[mid]>x:
        return binarySearch(nums,l,mid-1,x)
    else:
        return binarySearch(nums,mid+1,r,x)


def search(nums,target):
    res = []
    for i in range(len(nums)):

        a = target - nums[i]
        b = binarySearch(nums,i+1,len(nums)-1,a)
        if b != -1:
            res.append((nums[i],nums[b]))
    return res



def find_num(array, num):



    def binarySearch01(nums, l, r, x):

        if l > r:
            return -1
        mid = int(l + (r - l) / 2)

        if nums[mid] == x:
            return mid
        if nums[mid]>=nums[l]:
            if nums[l] <= x:
                return binarySearch(nums, l, mid - 1, x)
            else:
                return binarySearch(nums, mid+1, r, x)
        else:
            if nums[l] <= x:
                return binarySearch(nums, l, mid - 1, x)
            else:
                return binarySearch(nums, mid+1, r, x)

    return binarySearch01(array,0,len(array)-1,num)

if __name__ == '__main__':

    s = input()
    tem = ''
    res = 0
    for letter in s:
        if letter >= '0' and letter <= '9':
            tem += letter
            if res < int(tem):
                res = int(tem)
        else:
            tem = ''
    print(res)