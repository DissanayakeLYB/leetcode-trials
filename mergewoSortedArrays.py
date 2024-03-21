# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy_head = ListNode
        temp = dummy_head

        if list1 == None and list2 == None:
            return None


        while (list1 != None or list2 != None):

            if list1 == None:
                temp.next = list2
                return dummy_head.next
            
            elif list2 == None:
                temp.next = list1
                return dummy_head.next

            else:   
                if (list1.val <= list2.val):
                    temp.next = list1
                    temp = list1
                    list1 = temp.next
                    temp.next = None

                else: 
                    temp.next = list2
                    temp = list2
                    list2 = temp.next
                    temp.next = None
                        
        
        return dummy_head.next


        
print(Solution.mergeTwoLists([1,2,3],[2,4,5]))
        