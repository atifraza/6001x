# Lecture 3.7, slide 3

# Newton-Raphson for square root

epsilon = 1e-6
y = 925.0
guess = y/2.0
numGuesses = 1

while abs(guess*guess - y) >= epsilon:
    print(str(numGuesses)+ " " + str(guess))
    guess = guess - (((guess**2) - y)/(2*guess))
    numGuesses +=1
    #guess = ((guess**2) - y)/(2*guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))
