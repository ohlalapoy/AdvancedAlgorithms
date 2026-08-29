# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = []
        x = []
        for i in list1 :
            new_list.append(i)

        for j in list2:
            new_list.append(j)
        #print(new_list)
            x = sorted(new_list)
        return x

list1 = [1,2,4]
list2 = [1,3,4]
test = Solution()
print(test.mergeTwoLists(list1,list2))