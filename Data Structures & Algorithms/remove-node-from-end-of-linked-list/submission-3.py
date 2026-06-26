# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        curr2 = dummy = ListNode(0, prev)

        for i in range(n-1):
            curr2 = curr2.next

        curr2.next = curr2.next.next

        prev2, curr3 = None, dummy.next

        while curr3:
            tmp = curr3.next
            curr3.next = prev2
            prev2 = curr3
            curr3 = tmp

        return prev2