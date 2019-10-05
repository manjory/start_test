# tmp=head
# i=0
# while i<3:
#     tmp=tmp.next
#     i++
# tmp.next=ListNode(500)
# tmp=tmp.next
# tmp.next=l2
# tmp=head
# i=0
# tmp=head
# del=head
# while i!=3:
#     tmp=tmp.next
#     del.next=tmp.next
#     i=i+1
# tmp.next=tmp.next.next
# del.next=None
# while tmp.next!=None:
#     print (tmp.val)
#     tmp=tmp.next
# j=0
# tmp=head
# while j==4:
#     print (tmp.val)
#     j++
class Solution(object):



    def delNode(self, head, num):
        i = 0
        tmp = head
        while i < num:
            tmp = tmp.next
            i = i + 1
        d = tmp.next
        tmp.next = tmp.next.next
        d.next = None
        return d
    def mergeSortedLists(self, l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        tmp=None
        if l1.val <=l2.val:
            tmp=l1
            l1=l1.next
        elif l2.val<=l1.val:
            tmp=l2
            l2=l2.next
        t=tmp

        while l1 and l2:
            if l1.val<=l2.val:
                t.next=l1
                l1=l1.next

            elif l2.val<=l1.val:
                t.next=l2
                l2=l2.next

            t=t.next
        if not l1:
            t.next=l2
        if not l2:
            t.next=l1
        return tmp

    def deleteDuplicates(self, head):
        tmp = head
        while tmp and tmp.next :

            while tmp.val == tmp.next.val:
                d=tmp.next
                tmp.next = tmp.next.next
                d.next=None
            tmp=tmp.next
        return head




    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: listnode
    #     :type l2: listnode
    #     :rtype: listnode
    #     """
        # if l1.val<l2.val:
        #     tmp3=l1
        #     return tmp
        #
        # else:
        #     tmp3=l2
        #     return tmp
        #
        # while l1 and l2:
        #     if l1.val<l2.val:
        #         tmp3.next=l1
        #         l1=l1.next
        #         tmp3.next=None
        #     else:
        #             tmp3.next=l2
        #             l2.l2.next
        #
        #             tmp3.next=None
        #
        #     if l1!=None:
        #         tmp3.next=l1
        #     else:
        #         tmp3.next=l2
        #     return h3





