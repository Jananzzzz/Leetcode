# 1->3->4->7

class Solution:
    def deleteMiddle(self, head):
        curr = head 
        count = 0
        while curr:
            count += 1
            curr = curr.next 
        
        middle = count//2

        dummy = head
        while middle > 1:
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return head 

        

        






            
