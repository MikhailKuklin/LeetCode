# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = []
        l2 = []
        if list1 is None and list2 is None:
            return None
        else:
            while list1:
                l1.append(list1.val)
                list1 = list1.next
            while list2:
                l1.append(list2.val)
                list2 = list2.next
            for i in sorted(l1):
                cur = ListNode(val=i)
                l2.append(cur)
            for i in range(len(l2)-1):
                l2[i].next = l2[i+1]
            return l2[0]