# python linkedList

# we only need to store where the list starts when initialize a list


from platform import python_branch


class LinkedList:
    def __init__(self, nodes=None): # define linkedlist quickly with input node (default 0)
        self.head = None
        if nodes is not None:
            node = ListNode(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = ListNode(data=elem)
                node = node.next
        
    def __repr__(self): # represent the whole list from head, then traverse the list
        node = self.head
        nodes = []  # create a node function to repr the linked list as a common list
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)

    def __iter__(self): # built in function for outer call 
        node = self.head
        while node is not None:
            yield node
            node = node.next

# next, we create ListNode() to represent the linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data
     


linkedlist1 = LinkedList(["a", "b", "c", "d","e"])
print(linkedlist1)

# how to retrieve and insert a node in the linked list we create?
for i in linkedlist1:
    if i.data == "b":
        i.next = i.next.next

print(linkedlist1)





'''
Llist = LinkedList()
print(Llist)

first_node = ListNode("a")
Llist.head = first_node
print(Llist)

second_node = ListNode("b")
third_node = ListNode("c")
first_node.next = second_node
second_node.next = third_node

print(Llist)

first_node = ListNode("M")  # we defined a repr module.
print(first_node)

for node in linkedlist2:   
    print(node)
# change the variable name to A with give you a better understanding
for A in linkedlist2:
    print(A)
'''   