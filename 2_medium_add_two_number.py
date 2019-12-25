# 22:57 25-12-2019, Djambistraat 44-1 Amsterdam.
# https://leetcode.com/problems/add-two-numbers/
# A Syahdeini

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def NodeToInt(self, node: ListNode, scaler=1)-> int:
        if not node.next:
            return node.val*scaler
        else:
            _val = self.NodeToInt(node.next, scaler*10)
            return  node.val*scaler + _val
    
    def IntToNode(self, val):
        _mod = val % 10
        _div = val // 10
        if _mod == val:
            return ListNode(val)
        else:
            # it is till
            _temp = ListNode(_mod)
            _temp.next = self.IntToNode(_div)
            return _temp
        
        
                
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.IntToNode(
            self.NodeToInt(l1) + self.NodeToInt(l2)
        )
        
        
