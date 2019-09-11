# def search(nums,target):
#     if not nums:
#         return -1
#
#     left, right = 0, (len(nums) - 1)
#
#     while left <= right:
#         mid = (left + right) // 2
#             # print(left, right, mid)
#
#         if nums[mid] == target:
#             return mid
#
#         if nums[mid] < target:  # if target is on the right of mid (supposly)
#             if nums[mid] > nums[right]: #[4,5,6,1,2,3]
#                 left = mid + 1
#             else:
#                 if nums[right] >= target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#
#         elif target < nums[mid]:
#             if nums[mid] > nums[right]:
#                 if nums[left] <= target:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             else:
#                 right = mid - 1
#
#     return -1
#
# A = [1, 2, 3, 4, 5, 6]
# target = 4
# print(search(A, target))
# def toLowerCase(str):
#     c=""
#     for i in str:
#         val=ord(i)
#         if 65 <= val <= 90:
#             #val = val+32
#             c+=chr(val+32)
#         else:
#             c+=i
#     return c
# print(toLowerCase('I am JJJere'))

# def reverseOnlyLetters(S):
#     i = 0
#     j = len(S)-1
#     s=list(S)
#     c=''
#     while i<j:
#         if s[i].isalpha() and s[j].isalpha():
#             c=s[i]
#             s[i]=s[j]
#             s[j]=c
#             i=i+1
#             j=j-1
#         else:
#             if not s[i].isalpha():
#                 i=i+1
#             if not s[j].isalpha():
#                 j=j-1
#     return s
#
# S="ab-cd"
# print(reverseOnlyLetters(S))

# def compress(chars):
#     N = len(chars)
#     slow = 0
#     counter = 0
#     for fast in range(N):
#         if chars[slow] != chars[fast]:
#             if counter > 1:
#                 s_counter = str(counter)
#                 digits = len(s_counter)
#                 chars[slow + 1:(slow + 1 + digits)] = list(s_counter)
#                 chars[slow + 1 + digits] = chars[fast]
#                 slow += 1 + digits
#             else:
#                 chars[slow + 1] = chars[fast]
#                 slow += 1
#             counter = 1
#         else:
#             counter += 1
#
#     if counter > 1:
#         s_counter = str(counter)
#         digits = len(s_counter)
#         chars[slow + 1:(slow + 1 + digits)] = list(s_counter)
#         slow += digits
#
#     return slow + 1;
#
#

# def compress(chars):
#     c=""
#     sum = 1
#
#     for i in range(len(chars)-1):
#
#         if chars[i]==chars[i+1]:
#             sum=sum+1
#         else:
#             c=c+chars[i]+ str(sum)
#             sum=1
#
#     c= c+chars[len(chars)-1]+str(sum)
#     if len(c)<len(chars):
#         return c
#     else:
#         return chars
#
# chars=["a", "a","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]
# print (compress(chars))
# print("""I\m string"""""
# def isValid(s):
#     stack = []
#     for i in s:
#         if i == "(" or i="{" or i="[":  # stack="("
#             stack.append("(")
#         else:
#             if i == ")" or stack[len(stack) - 1] != "(":
#                 return False
#             if i == "}" or stack[len(stack) - 1] != "{":
#                 stack.pop()
#             if i == "]" or stack[len(stack - 1)] != "[":
#                 stack.pop()
#         return False
#     return True
# s="()"
# print (isValid(s))
# def reverseWords(s):
#     a=""
#
#     for i in s.split(' '):
#         a =a + ' '+ (i[::-1])
#
#     return (a)
# s="my name"
# print(str(reverseWords(s)))


# s= "aaca"
# s.replace(s,s[0],"",1)
# # s.replace()
# def removeDuplicates(S):
#     new = ""
#     i = 0
#     while S:
#         if S[i] == S[i + 1]:
#             S=S.replace(S[i] and S[i+1],"")
#             i=i+1
#
#
#         else:
#             i = i + 1
#     return S

# def removeDuplicates(S):
#     i = 0
#     while i < len(S) - 1:
#         # print(i, S)
#         if S[i] == S[i + 1]:
#             # S = S.replace(S[i + 1], "")
#
#             S[i+1]=""
#
#             if i > 0:
#                 i = i - 1
#             else:
#                 i = 0
#         else:
#             i = i + 1
#     return S




# S="aa"
# print(removeDuplicates(S))

# import re
# def is_allowed_specific_char(string):
#     charRe = re.compile(r'[^a-zA-Z0-9.]')
#     string = charRe.search(string)
#     return not bool(string)
#
# print(is_allowed_specific_char("ABCDEFabcdef123450"))
# print(is_allowed_specific_char("*&%@#!}{"))

# def reverseVowels(s):
#
#     A = list(s)
#     i, j = 0, len(s) - 1
#
#     while i < j:
#         if A[i] == 'a' or A[i] == 'e' or A[i] == 'i' or A[i] == 'o' or A[i] == 'u':
#             if A[j] == 'a' or A[j] == 'e' or A[j] == 'i' or A[j] == 'o' or A[j] == 'u':
#                 c = A[i]
#                 A[i] = A[j]
#                 A[j] = c
#                 i=i+1
#                 j=j-1
#
#             else:
#                 j = j - 1
#         else:
#             i = i + 1
#     return ''.join(A)
# S='time'
# print (reverseVowels(S))

nums=[1]
target=0

#
# def search(nums, target):
#     l = 0
#     u = len(nums)
#     i = 0
#     if u == 0:
#         return -1
#     if u ==1 :
#         if nums[0] == target:
#             return 0
#         else:
#             return -1
#     newLeftlist = []
#     while i < u:
#         if nums[i] > nums[i + 1]:
#             pivot = i + 1
#         else:
#             newLeftlist.append(nums[i])
#         i = i + 1
#
#     if target >= newLeftlist[0]:
#         for j in newLeftlist:
#             if j == target:
#                 return j
#             else:
#                 return -1
#     elif target >= nums[pivot] or target <= nums[u - 1]:
#         for j in range(pivot, u - 1):
#             if target == nums[j]:
#                 return j
#             else:
#                 return -1
# print (search(nums,target))

# def binary_search(nums,target):
#     if len(nums)<1:
#         return -1
#     l=0
#     r=len(nums)-1
#     while l<=r:
#         mid = (l+r)//2
#         if target==nums[mid]:
#             return mid
#         elif target < nums[mid]:
#             r=mid-1
#         else:
#             l=mid+1
#
#     return -1
# nums=[1,2,3,4,5,6]
# target=2
#
# print(binary_search(nums,target))

def search(nums, target):
    if len(nums) < 1:
        return -1
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        if nums[mid] >= nums[l]:
            if target < nums[mid] and target >= nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        if nums[mid] < nums[r]:
            if target <= nums[r] and target >= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

nums=[2]
target=0
print(search(nums,target))