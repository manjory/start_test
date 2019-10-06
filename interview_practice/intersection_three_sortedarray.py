import time
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# # Output: [1,5]
# # Explanation: Only 1 and 5 appeared in the three arrays.

# using set


# using 3 for loops

def arraysIntersection_set(arr1, arr2, arr3):
    t = time.monotonic_ns()
    a2=set(arr2)
    a3=set(arr3)
    a=[]
    for i in arr1:
        if i in a2 and i in a3:
            a.append(i)
    print(time.monotonic_ns() - t)

    return a
def arraysIntersection(arr1, arr2,arr3):
    t = time.monotonic_ns()

    a=[]
    for i in arr1:
        for j in arr2:
            if j>i:
                break
            for k in arr3:
                if k>j:
                    break
                if k==j and k==i:
                    a.append(k)
    print(time.monotonic_ns()-t)

    return a

arr1=[1,5,30,31,32]
arr2=[5,9,10,30,31]
arr3=[1,5,30,31]
print(arraysIntersection_set (arr1,arr2,arr3))