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
# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
# Compare two linked lists


def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
    else:
        if (llist1 and not llist2) or (not llist1 and llist2):
            return 0

    return 1