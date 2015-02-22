def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    def getCount(a,b,c):
        return 6*a+9*b+20*c
    a = 0
    b = 0
    c = 0
    count = getCount(a,b,c)
    while (count<=n):#{
        while (count<=n):#{
            while (count<=n):#{
                if(count==n):
                    return True
                elif(count<n):
                    a += 1
                count = getCount(a,b,c)
            #}
            a = 0
            b += 1
            count = getCount(a,b,c)
            if (count==n):
                return True
        #}
        b = 0
        c += 1
        count = getCount(a,b,c)
        if(count==n):
            return True
    #}
    return False

print McNuggets(0)
print McNuggets(7)
print McNuggets(9)
print McNuggets(15)
print McNuggets(26)
print McNuggets(29)
print McNuggets(35)
