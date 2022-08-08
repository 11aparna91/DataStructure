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


##################### Merge Two sorted list ###########

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode()
        tail=dummy

        while list1 and list2:            
            if list1.val < list2.val:
                tail.next=list1
                list1= list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail= tail.next
        
        if list1:
            tail.next=list1
        else:
            tail.next=list2
        
        return dummy.next
            
        
