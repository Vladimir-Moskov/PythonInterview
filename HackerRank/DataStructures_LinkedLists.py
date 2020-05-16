# https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
# Reverse a linked list


# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    current_node = head
    prev_node = None
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node, current_node = current_node, next_node


    return prev_node

##########################################################################################################