"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        """
        cur是当前节点，next指向cur节点的下一个节点，prev是cur节点前一个节点；
        """

        first_head = head
        pre = None
        cur = head

        n = 0

        while True:

            # 判断cur节点之后，是否有k个节点，如果没有就直接跳出while循环,如果有k个，则进行翻转
            flag = False
            if n != 0:
                cur_text = pre
            for i in range(k):

                if not cur_text:
                    flag = True
                    break
                cur_text = cur_text.next
            if flag:
                break
            n += 1

            first,last = self.reverse(pre,cur,k)
            pre = last.next
            cur = pre.next

            if n==1:
                first_head = first

        return first_head


    def reverse(self,first,last,k):
        """
        翻转一小段
        :param head: 一小段的开始节点
        :return: 返回两个节点：翻转后的开始first节点，和结束last节点
        """

        prev = None
        cur = first
        next = cur.next
        cur.next = prev

        for i in range(k):
            prev = cur
            cur = next
            next = cur.next
            cur.next = prev
            # if cur:
            #     next = cur.next
        first = pre
        last.next = cur
        return first,last


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 使用栈的思想来解决这个问题
class Solution00:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        self.stack = []
        p = ListNode(-1)
        result = p
        # 状态标志
        flag = True
        temp_head = head
        while head:
            for i in range(k):
                if not head:
                    flag = False
                    break
                self.stack.append(head)
                head = head.next
            if not flag:
                break
            else:
                # 更新翻转后的进行连接的节点
                temp_head = head
            for i in range(k):
                cur = self.stack.pop()
                p.next = cur
                p = cur
            # 翻转后和后面的节点相连
            p.next = temp_head
        return result.next


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
b = Solution().reverseKGroup(a,2)

while b:
    print(b.val)
    b = b.next


