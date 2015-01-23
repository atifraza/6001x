print "Please think of a number between 0 and 100!"
low = 0
high = 100
ans = (high + low)/2
char = 'y'
while char != 'c':
    print "Is your secret number " + str(ans) + "?"
    char = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if char == 'l':
        low = ans
    elif char == 'h':
        high = ans
    elif char == 'c':
        print "Game over. Your secret number was: " + str(ans)
        break
    else:
        print "Sorry, I did not understand your input."
    if char == 'l' or char == 'h':
        ans = (high + low)/2