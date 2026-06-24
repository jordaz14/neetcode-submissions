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

        dummy = ListNode(0, prev)
        prev2 = dummy

        for _ in range(n-1):
            prev2 = prev2.next

        prev2.next = prev2.next.next

        prev3, curr2 = None, dummy.next

        while curr2:
            tmp = curr2.next
            curr2.next = prev3
            prev3 = curr2
            curr2 = tmp

        return prev3
