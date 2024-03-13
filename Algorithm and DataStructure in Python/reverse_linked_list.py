#Reverse Linked List
#Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #create pointer for prev and current nodes
        #create temp pointer for next node
        prev_node = None
        current_node = head

        while current_node:
            next_node = current_node.next #save the next node in this temp pointer
            current_node.next = prev_node #reverse the current node
            current_node = next_node #move current to next
        head = prev_node #update head to the new firs element
        return head
#this solution passes all leet code test cases and has runtime of 33ms