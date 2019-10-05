from solution import Solution
from listnode import ListNode
def main():
    # print("Starting")
    # head1 = ListNode(1)
    # head1.next = ListNode(3)
    # head1.next.next = ListNode(16)
    # # head1.next.next.next = ListNode(5)
    # tmp = head1
    # head2 = ListNode(1)
    # head2.next = ListNode(1)
    # head2.next.next=ListNode(9)
    sol=Solution()
    # head3 = sol.mergeSortedLists(head1,head2)
    # tmp = head3
    sample_del=ListNode(1)
    sample_del.next=ListNode(1)
    sample_del.next.next=ListNode(2)
    sample_del.next.next.next=ListNode(3)
    sample_del.next.next.next.next=ListNode(3)
    sample_del.next.next.next.next.next=ListNode(4)
    head4=sol.deleteDuplicates(sample_del)
    tmp_del=head4
    while tmp_del:
        print(tmp_del.val)
        tmp_del=tmp_del.next
    print ("\n\n")
    # while tmp:
    #     print(tmp.val)
    #     tmp=tmp.next


    # head = ListNode(0)
    # tmp =head
    # for i in range(1,10):
    #         tmp.next= ListNode(i)
    #         tmp=tmp.next
    # t=head
    # i=1
    #
    # while t!=None:
    #
    #     print ("index is this:",i,"value is :", t.val)
    #     t=t.next
    #     i = i + 1
    # print ("\n")
    # sol = Solution()
    # tmp = sol.delNode(head,5)
    #
    # print (tmp.val)
    # print("\n")
    # i=0
    #
    # t=head
    # while t!=None:
    #     # print (t.val)
    #     print ("index is this:",i,"value is :", t.val)
    #     i=i+1
    #     t=t.next
    #


    # while tmp:
    #     print(tmp.val)
    #     tmp = tmp.next
    #
    # tmp=head2
    # while tmp:
    #     print(tmp.val)
    #     tmp=tmp.next

    # sol = Solution()
    # var = sol.mergeTwoLists(head1, head2)
    # while var:
    #     print (var.val)
    #     var=var.next


if __name__ == '__main__':
    main()
