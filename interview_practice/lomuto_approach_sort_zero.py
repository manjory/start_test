# lomuto: using a pivot

def swap(A,left,right):
    temp=0
    temp= A[left]
    A[left]=A[right]
    A[right]=temp
    return A

def sort_zeroes(A):
    left=0
    right=len(A)-1
    while left<right:
        while A[left]==0 and left<right:
            left=left+1
        while A[right]==1 and left<right:
            right=right -1
        if A[left]==1 or A[right]==0:
            swap(A,left,right)
    return A
array=[1,1,0,0,1]
print(sort_zeroes(array))
