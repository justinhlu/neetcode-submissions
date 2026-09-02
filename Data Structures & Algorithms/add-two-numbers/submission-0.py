# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1Num, l2Num = "","" 

        l1Curr = l1
        l1Prev = None
        l2Curr = l2
        l2Prev = None
        while l1Curr:
            nextNode = l1Curr.next
            l1Curr.next = l1Prev
            l1Prev = l1Curr
            l1Curr = nextNode 
        
        l1Curr = l1Prev
        while l1Curr:
            l1Num += str(l1Curr.val)
            l1Curr = l1Curr.next

        while l2Curr:
            nextNode = l2Curr.next
            l2Curr.next = l2Prev
            l2Prev = l2Curr
            l2Curr = nextNode 
        
        l2Curr = l2Prev
        while l2Curr:
            l2Num += str(l2Curr.val)
            l2Curr = l2Curr.next
        
        sum = int(l1Num) + int(l2Num)
        sum = str(sum)
        sumArr = []
        for i in range(len(sum)-1, -1,-1):
            sumArr.append(int(sum[i]))
        
        dummy = ListNode()
        sumNode = dummy

        for digit in sumArr:
            sumNode.next = ListNode(digit)
            sumNode = sumNode.next 

        return dummy.next 
        