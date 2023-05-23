# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p=head
        l=[]
        while(p!=None):
            l.append(p.val)
            p=p.next
        return l==l[::-1]