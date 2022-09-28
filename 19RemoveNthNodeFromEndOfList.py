# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_length():
            cur = head
            count = 0
            while cur:
                count += 1
                cur = cur.next
            return count
        cur = head
        count = 0
        prev = None
        length = get_length()
        if length > 0: 
            while cur and count != length - n:
                prev = cur
                cur = cur.next
                count += 1
            if prev:
                prev.next = cur.next
            else:
                head = cur.next
        return head
        
