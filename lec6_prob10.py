animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    sum = 0
    for key in aDict:
        sum += len(aDict[key])
    return sum
    
print(howMany(animals))

def biggest(aDict):
    biggest = -1
    biggestKey = None
    for key in aDict:
        if( biggest<len(aDict[key]) ):
            biggest = len(aDict[key])
            biggestKey = key
    
    return biggestKey

print(biggest(animals))
