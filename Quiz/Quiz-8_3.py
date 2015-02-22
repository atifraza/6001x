def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    print 'in fixedpoint'
    print 'f=', type(f), f
    guess = 1.0
    for i in range(100):
        print i
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

#def sqrt(a):
#    def tryit(x):
#        return 0.5 * (a/x + x)
#    return fixedPoint(tryit, 0.0001)

def babylon(a):
    def test(x):
        print 'in test', x
        print 
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    print 'in sqrt'
    print a
    return fixedPoint(babylon(a), 0.0001)

print sqrt(20.0)