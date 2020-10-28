# Remove Kth Node From End

#Write a function that takes in the head of a singly linked list and an integer k and remoxed the kth node from the end of the list.

#The remove should be done in place, meaning that the original data structure should be mutated (no new structure should be created)

#furthermore, the input head of the linked list should remain the head of the linked list after the removal is done, even if the head is the node that is supposed to be removed. In other words, if the head is the node that is supposed to be removed, your function should simply mutate its value and next pointer

#Sample input: head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 ->8 ->9, head node with value 0
#k = 4

#output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 ->9
#The 4th node from the end of the list (the node with value 6) is removed

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
def removeKthNodeFromEnd(head, k):
    pass