# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        visited_node = {}

        while current:
            if current in visited_node:
                return True
            else:
                visited_node[current] = 'True'
            
            current = current.next
        return False
        