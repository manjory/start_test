def reverse_string(string):
    i=0
    j=len(string)-1
    string=list(string)
    while i<j:
        string[i],string[j]=string[j],string[i]
        i=i+1
        j=j-1
    return ''.join(string)
print (reverse_string('abcd'))
