# https://leetcode.com/problems/merge-k-sorted-lists/description/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        value_list = []
        for i in lists:
            while i:
                value_list.append(i.val)
                i = i.next
        if not value_list:
            return None
        value_list.sort()
        dummy_node = head = ListNode(value_list[0])
        for i in value_list[1:]:
            node = ListNode(i)
            dummy_node.next = node
            dummy_node = node

        return head