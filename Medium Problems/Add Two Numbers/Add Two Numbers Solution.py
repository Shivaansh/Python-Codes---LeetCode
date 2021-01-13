# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        i = 0
        while(l1 != None):
            num1 += l1.val * (10**i)
            l1 = l1.next
            i += 1
        
        num2 = 0
        j = 0
        while(l2 != None):
            num2 += l2.val * (10**j)
            l2 = l2.next
            j += 1
            
        sum = num1 + num2
        print(sum)
        num3 = sum%10
        p = ListNode(num3, None)
        head = p
        sum = sum/10
        
        while(sum >= 10):
            p.next = ListNode(sum%10, None)
            p = p.next
            sum = sum/10
        
        if(sum > 0):
            p.next = ListNode(sum%10, None)
            p = p.next
        
        return head
        