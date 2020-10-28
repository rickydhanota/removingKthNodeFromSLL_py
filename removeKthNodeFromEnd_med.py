# Remove Kth Node From End

#Write a function that takes in the head of a singly linked list and an integer k and remoxed the kth node from the end of the list.

#The remove should be done in place, meaning that the original data structure should be mutated (no new structure should be created)

#furthermore, the input head of the linked list should remain the head of the linked list after the removal is done, even if the head is the node that is supposed to be removed. In other words, if the head is the node that is supposed to be removed, your function should simply mutate its value and next pointer

#Sample input: head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 ->8 ->9, head node with value 0
#k = 4

#output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 ->9
#The 4th node from the end of the list (the node with value 6) is removed
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def removeKthNodeFromEnd(self, k):
        counter = 1
        first = self.head
        second = self.head
        while counter <= k:
            second = second.next
            counter += 1
        if second is None:
            self.head.value = self.head.next.value
            self.head.next = self.head.next.next
            return
        while second.next is not None:
            second = second.next
            first = first.next
        first.next = first.next.next

    def newNode(self, value):
        addNode = Node(value)
        if self.head:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = addNode
        else:
            self.head = addNode
        return self

    def addFront(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            node = self.head
            self.head = Node(value)
            self.head.next = node
        return self

    def removeFront(self):
        if self.head == None:
            return False
        else:
            node = self.head
            self.head = self.head.next
        return self

    def maxNode(self):
        if self.head == None:
            return
        maxNode = 0
        while self.head != None:
            if self.head.value >= maxNode:
                maxNode = self.head.value
            self.head = self.head.next
        print("the max node is", {maxNode})
        return self
    
    def printing(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next
        return self

sll = LinkedList()
sll.newNode(1).newNode(2).newNode(3).newNode(4).addFront(21).printing().maxNode().printing()
# sll.removeKthNodeFromEnd(4)

