"""

23. 合并K个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """



        fake_head = ListNode(-1)

        cur = fake_head

        my_heapq = []
        node_list = []

        import heapq
        for index,node in enumerate(lists):
            if node != None:
                heapq.heappush(my_heapq,(node.val,index))
            node_list.append(node)



        while my_heapq:

            value,index = heapq.heappop(my_heapq)
            cur.next = lists[index]
            cur = cur.next

            if cur.next != None:
                lists[index] = cur.next
                heapq.heappush(my_heapq,(cur.next.val,index))

        return fake_head.next
# Definition for singly-linked list.

class Solution02(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def merge_sort02(nums):
            n = len(nums)
            if n < 2:
                return nums[0]

            mid = n // 2

            left = merge_sort02(nums[:mid])
            right = merge_sort02(nums[mid:])


            fake_head = ListNode(-1)
            cur = fake_head

            while left and right:
                if left.val > right.val:
                    cur.next = right
                    cur = cur.next
                    right = right.next
                else:
                    cur.next = left
                    cur = cur.next
                    left = left.next

            while left:
                cur.next = left
                cur = cur.next
                left = left.next
            while right:
                cur.next = right
                cur = cur.next
                right = right.next

            return fake_head.next



        return merge_sort02(lists)

