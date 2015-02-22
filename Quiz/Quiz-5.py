def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    ret = ''
    ind = 0
    while (ind < len(s1) or ind < len(s2) ):
        if(ind < len(s1) ):
            ret = ret + s1[ind]
        if(ind < len(s2) ):
            ret = ret + s2[ind]
        ind += 1
    return ret

print laceStrings('abcd','efghi')
print laceStrings('abcdefg','xyz')
print laceStrings('abcd','')
