# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a arr(string) to store the values in 11
        arr = ""
        while l1 != None:
            # add each elements to a string(arr)
            arr = arr + str(l1.val)
            # change the l1 pointer to it's next
            l1 = l1.next
        # after completing the iteration of l1(linkedlist)
        # reverse the string
        arr = arr[-1::-1]
        # the same for arr2
        arr2 = ""
        while l2 != None:
            # add each elements to a string(arr2)
            arr2 = arr2 + str(l2.val)
            # change the l2 pointer to it's next
            l2 = l2.next
        # after completing the iteration of l2(linkedlist)
        # reverse the string
        arr2 = arr2[-1::-1]
        # add two strings after changing them to int and store that value
        # in variable(thoma: meaning twin)
        thoma = int(arr) + int(arr2)
        # list to string to int
        thoma = str(thoma)
        # reverse again
        thoma = thoma[-1::-1]
        # create a node
        dummy = ListNode(0)
        # create an iterator and point to head
        head = dummy
        # iterate over the elements in string(thoma)
        for i in thoma:
            # for each element create node with the value of element
            newNode = ListNode(i)
            # point head's next to newNode
            head.next = newNode
            # move head to it's own next 
            head = head.next
        # return dummy.next because first value is 0
        return dummy.next