from queue import PriorityQueue


def nth_largest(arr, k):
    q = PriorityQueue(k)
    min = arr[0]
    q.put(arr[0])
    for i in range(1, len(arr)):
        if q.full():
            if min < arr[i]:
                q.get()
                min= q.get()
                q.put(min)
            elif q.full():
                continue
        q.put(arr[i])
    return q.get()


arr = [4,  12, 23, 34,5,89,67,988,23,9]

print(nth_largest(arr, 3))
