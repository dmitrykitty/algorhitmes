class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        linkedlist = ""
        current = self

        while current and current.next is not None:
            linkedlist += str(current.val) + " "
            current = current.next

        linkedlist += str(current.val)
        return linkedlist

def show_list(head):
    curr = head
    while curr:
        print(curr.val, end="")
        if curr.next:
            print(" -> ", end="")
        curr = curr.next
    return head


def reverse_list(head):
    curr = head
    head.next = None
    while curr:
        curr.next.next = curr
        curr = curr.next

def add_at_head(head, value):
    new_node = ListNode(value)
    new_node.next = head
    return new_node

node1 = ListNode(3)
show_list(add_at_head(node1, 1))



node2 = ListNode(5)
node3 = ListNode(7)
node4 = ListNode(9)


node1.next = node2
node2.next = node3

