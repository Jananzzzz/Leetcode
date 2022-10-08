# prev  a   b   c
#       curr 
#      1--->2--->3--->4--->5--->6--->7
#      3--->2--->1--->6--->5--->4--->7
       
 # classical method for reverse a linked list 
def reverseLinkedList(self, head: ListNode) -> ListNode:
    prev = curr = None, head 
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        
        # Check if we need to reverse the group
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
		        
				
        # Reverse the group (basic way to reverse linked list)
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
		
        # After reverse, we know that `head` is the tail of the group.
		# And `curr` is the next pointer in original linked list order
        head.next = self.reverseKGroup(curr, k)
        return prev
        