class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        while list1 and list2:                    # loop only while BOTH have nodes
            if list1.val <= list2.val:
                cur.next = list1                  # link
                list1 = list1.next                # advance the source
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next                        # advance the tail
        cur.next = list1 or list2                 # attach whatever is left, in one go
        return dummy.next