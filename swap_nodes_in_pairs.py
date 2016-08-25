# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self is None:
            return None
        return str(self.val) + " -> "+self.next.__str__()

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # empty list (none left)
        if head is None:
            return head
        # one left (odd number)
        if head.next is None:
            return head
        # more than one left
        new_head = head.next
        tail = head.next.next
        new_head.next = head
        head.next = self.swapPairs(tail)
        return new_head

doer = Solution()


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(doer.swapPairs(head))

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print(doer.swapPairs(head))


head = ListNode(1)

print(doer.swapPairs(head))


head = None

print(doer.swapPairs(head))

