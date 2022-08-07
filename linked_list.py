class ListNode:
     def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if None in (l1,l2):
                return l1 or l2
            
        if(l1.val < l2.val):
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return 
#####################################
## Fast Slow Pointer and Middle List of Linked List ########
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
###################################
########Reverse the linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev=None
        while head:
            cur=head
            head=head.next
            cur.next=rev
            rev=cur
        return rev
