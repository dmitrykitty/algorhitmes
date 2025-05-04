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
        if index < 0 or index >= self.length:
            return - 1

        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index, val):
        if index < 0 or index > self.length:
            return

        self.length += 1

        cur = self.head
        for i in range(index - 1):
            cur = cur.next
        temp = cur.next
        cur.next = ListNode(val, temp)

    def deleteAtIndex(self, index):
        if index < 0 or index > self.length - 1:
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
