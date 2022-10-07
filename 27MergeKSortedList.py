# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# brute force with simplified code:
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
    # turn the list item into numbers
    # merge them to one unlinked list 
    # sort the list then convert it to a linked list and return
    
    self.nodes = []
    head = point = ListNode(0)
    for l in lists:
        while l:
            self.node.append(l.val)          
            l = l.next                      
    for x in sorted(self.nodes):
        point.next = ListNode(x)
        point = point.next
    return head.next
        
    # retrieve the value of a linked node directly
    
    #    while node:
    #   list.append(node.val)
    #    node = node.next
    
'''

# brute force method (with the fastest speed)
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newlist = []
    
        def convertToUnlinked(list):
            temp = []
            cur = list
            while cur != None:
                temp.append(cur.val)
                cur = cur.next 
            return temp


        for i in lists:
            new = convertToUnlinked(i)
            newlist.extend(new)

        # convert newlist to a linked list 
        newlist.sort()

        head = point = ListNode(0)     # initialize a node.
        print(newlist)
        for i in newlist:
            point.next = ListNode(i)             # can't use point.val
            point = point.next         # this is a predifined func

        return head.next
'''
