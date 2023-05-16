# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if not node:
            return head
        if not node.next:
            return head
        else:
            post = node.next
        
        idx = 0
        
        while post:
            if (idx % 2) == 0:
                node.val, post.val = post.val, node.val
            node = post
            post = node.next
            idx += 1
        
        return head
        