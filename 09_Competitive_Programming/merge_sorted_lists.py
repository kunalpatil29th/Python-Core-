# merge_sorted_lists.py

"""
Problem: Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new sorted list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    return dummy.next

# Example
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
merged = merge_two_lists(l1, l2)
print("Merged list values:")
while merged:
    print(merged.val, end=" ")
    merged = merged.next
print()
