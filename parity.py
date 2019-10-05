
    # [2,3,5,6,8,9]->[2,2,2,1,4,2,5]
    #                   l=0           r=6
    #                   A[0] is even, A[6] is odd
    #                   l=l+1=1      r=r-1=5
    #                   A[1] is even, A[5]is even
    #                    l=l+1,      r is constant at 5
    #                 A[2] is even r is even so constant at 5
    #                     l=l+1=3 r= 5
    #                     A[3]is odd and A[5] is odd
    #                   swap A[3] with A[5]
    #                                 l =l+1=4 and r=r-1=4
    #                    the list is now [2,2,2,2,4,1,5]
    #                    l=r come out of loop
def parity_odd_even(A):
    l=0
    r= len(A)-1
    while l<r:
        while A[l]%2==0 and l<r:
            l=l+1
        while A[r]%2!=0 and r>l:

            r=r-1
        if A[l]%2!=0 and A[r]%2==0:
            A[l],A[r]=A[r],A[l]
            l=l+1
            r=r-1

A=[2,2,2,1,2,3,5]
print(A)

parity_odd_even(A)
print((A))
