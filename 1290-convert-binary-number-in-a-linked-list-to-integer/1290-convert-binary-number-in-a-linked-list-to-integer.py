# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        total = 0
        while current != None:
            total *=2
            total +=current.val
            current = current.next
        return total
        