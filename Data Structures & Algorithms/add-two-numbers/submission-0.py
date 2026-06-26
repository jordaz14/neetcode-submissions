# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1, str2 = "", ""

        cur1, cur2 = l1, l2
        while cur1:
            str1 += str(cur1.val)
            cur1 = cur1.next

        while cur2 :
            str2 += str(cur2.val)
            cur2 = cur2.next

        num = str(int(str1[::-1]) + int(str2[::-1]))
        num = num[::-1]
        
        ans = []
        for digit in num:
            node = ListNode(int(digit), None)
            ans.append(node)

        head = ans[0]
        for i in range(len(ans)-1):
            node = ans[i]
            node.next = ans[i+1]
        
        return head


        