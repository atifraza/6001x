def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    result = 0
    while start < stop:
        result += f(start)*step
        start += step
    return result








result = radiationExposure(0, 5, 1)
print result
print(39.10318784326239)
if ( abs( result-39.10318784326239 ) <1e-3):
    print('Success 1')
result = radiationExposure(5, 11, 1)
print result
print(22.94241041057671)
if ( abs( result-22.94241041057671 ) <1e-3):
    print('Success 2')
result = radiationExposure(0, 11, 1)
print result
print(62.0455982538)
if ( abs( result-62.0455982538 ) <1e-3):
    print('Success 3')
result = radiationExposure(40, 100, 1.5)
print result
print(0.434612356115)
if ( abs( result-0.434612356115 ) <1e-3):
    print('Success 4')


#    print(range(start, stop, step))
#    #years = seq(start, stop, step)
#    #import numpy
#    #years = numpy.arange(start, stop, step)
#    years = [start * step for start in range(start, stop)]
#    print(years)
#    totalRadiation = applyFunc(years, f)
#    return totalRadiation
#
##def seq(start, stop, step=1):
##    n = int(round((stop - start)/float(step)))
##    if n > 1:
##        return([start + step*i for i in range(n+1)])
##    else:
##        return([])
#
#def applyFunc(list, func):
#    result = 0
#    for current in list:
#        result += func(current)
#    return result
#
