def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print '3', Square(3)
print '1', Square(1)
print '-3', Square(-3)
print '0', Square(0)