from curses import noecho


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next
        nextNode.next = None
        del(nextNode)

        # node.val, node.next = nextNode.val, nextNode.next
        