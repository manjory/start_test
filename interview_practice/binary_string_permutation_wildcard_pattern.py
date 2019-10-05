# def get_all_combo(size, array):
#     if size<len(array):
#         return (size-1,array)
#     else:
#         get_all_combo()
def fact(n):
    f=1

    if n<=1:
        return n
    else:
        f=fact(n-1)*n

n=5
print(fact(n))
