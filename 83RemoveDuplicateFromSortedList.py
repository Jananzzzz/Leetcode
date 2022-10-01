# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currr = head 
        
        while currr :
            while currr.next and currr.next.val == currr.val:
                currr.next = currr.next.next
            currr = currr.next
        
        return head 