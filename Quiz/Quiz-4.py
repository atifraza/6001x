def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    exponent = 0
    while ( b**(exponent+1) <= x ):
        exponent += 1
    return exponent

print myLog(27,3)
print myLog(26,3)
print myLog(28,3)
print myLog(4,10)
