# group all the odd positioned nodes together and even positioned nodes together, odd group first then even group.
#approach :
# to do this in-place, 
# take the head as odd list and the 2nd node as even list
# link every odd node to the next odd node ( 2 pos after it)
# link every even node to the next even node ( 2 pos after it)
# advance these odd and even pointers on pos forward (thus they act as tails for odd and even list)
# thus the point to next odd and even nodes

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        # if head is null or there are only 1 or 2 nodes
        if(not head or not head.next or not head.next.next):
            return head
        
        odd=head
        even=head.next
        evenHead=even
        
        while(even and even.next):
            odd.next=odd.next.next # odd gets linked to next odd
            even.next=even.next.next # even gets linked to next even
            odd=odd.next # move odd tail forward
            even=even.next # move even tail forward
            
        #link the even list at the end of odd list
        odd.next=evenHead
        
        return head
