# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        tail = dummy_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0

            sum = num1 + num2 + carry
            
            new_num = sum % 10
            carry = sum // 10

            new_node = ListNode(new_num)
            tail.next = new_node
            tail = tail.next

            l1 = l1.next if l1 is not None else None 
            l2 = l2.next if l2 is not None else None

        result = dummy_head.next
        # dummy_head.next = None # free
        return result
    
