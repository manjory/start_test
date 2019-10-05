def sum_subArray(A,start,fast):
    sum=0
    while start<fast:
        sum=sum+A[start]
        start=start+1
    return sum

def subarrays_zerosum(A):
    start=0
    sub_arrays=[]
    while start<=len(A)-1:
        fast=start+1
        while fast<=len(A):
            if (sum_subArray(A,start,fast))==0:
                print("start = ", start , " ::: end =", fast )
                sub_arrays.append(A[start:fast])
                # fast=fast+1
            fast = fast + 1
        start=start+1

    return sub_arrays
A=[1,-1,0]
print (subarrays_zerosum(A))

