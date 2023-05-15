# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        
        node = head
        
        while node:
            l += 1
            if l == k:
                a = node
            node = node.next
            
            
        if l == 1:
            return head
        
        node = head
        for _ in range(l - k):
            node = node.next
        
        b = node
        
        tmp = a.val
        a.val = b.val
        b.val = tmp
        
        return head
        
        
        
        
            