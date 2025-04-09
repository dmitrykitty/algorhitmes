from typing import Optional
import os
import sys


# nie zmieniaj implementacji ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def showList(self, head):
        cur = head
        while cur:
            print(cur.val, end="")
            if cur.next:
                print(" -> ", end="")
            else:
                print(" -> None")
            cur = cur.next

    def get(self, index):
        if  index < 0 or index > self.length - 1:
            return - 1
        counter = 0
        cur = self.head
        while cur and counter < index:
            cur = cur.next
            counter += 1
        if cur:
            return cur.val

    def addAtHead(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def addAtTail(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next

            cur.next = node

        self.length += 1

    def addAtIndex(self, index, val):
        if  index < 0 or index > self.length - 1:
            return
        node = ListNode(val)
        if index == 0:
            node.next = self.head
            self.head = node
            self.length += 1
            return

        cur = self.head
        counter = 0
        while cur and counter < index - 1:
            cur = cur.next
            counter += 1

        node.next = cur.next
        cur.next = node
        self.length += 1

    def deleteAtIndex(self, index):
        if  index < 0 or index > self.length - 1:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        cur = self.head
        counter = 0
        while cur.next and counter < index - 1:
            cur = cur.next
            counter += 1
        if cur.next.next:
            cur.next = cur.next.next
        else:
            cur.next = None
        self.length -= 1




lst1 = MyLinkedList()
lst1.addAtHead(2)
lst1.addAtTail(3)
lst1.addAtIndex(3, 2)
lst1.showList(lst1.head)
print(lst1.get(1))


