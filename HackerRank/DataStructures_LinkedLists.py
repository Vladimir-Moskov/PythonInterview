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

##########################################################################################################
# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
# Merge two sorted linked lists


def mergeLists(head1, head2):
    current_node = None
    while head1 and head2:
        prev = current_node
        if head1.data < head2.data:
            current_node = head1
            head1 = head1.next
        else:
            current_node = head2
            head2 = head2.next
        if prev:
            prev.next = current_node
        else:
            head = current_node
    if head1:
        current_node.next = head1
    else:
        current_node.next = head2
    return head

###########################################################################################################
# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
# Get Node Value


def getNode(head, positionFromTail):
    result = None
    count = 0
    current = head
    while current:
        current = current.next
        if not result and count == positionFromTail:
            result = head
        elif result:
            result = result.next
        else:
            count += 1


    return result.data

