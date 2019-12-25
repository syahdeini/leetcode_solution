# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:                
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        headNode = ListNode(0)
        pointNode = headNode
        carry = 0
        while (l1 or l2):
            node1_val = l1.val if l1 else 0
            node2_val = l2.val if l2 else 0
            _sum = node1_val + node2_val + carry
            carry = _sum // 10
            _res = _sum % 10
            pointNode.next = ListNode(_res)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            pointNode = pointNode.next
        if carry!=0:
            pointNode.next = ListNode(carry)
        return headNode.next
        
