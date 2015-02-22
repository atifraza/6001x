#def isWordGuessed(secretWord, lettersGuessed):
#    '''
#    secretWord: string, the word the user is guessing
#    lettersGuessed: list, what letters have been guessed so far
#    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
#      False otherwise
#    '''
#    # FILL IN YOUR CODE HERE...
#    isGuessed = False
#    secWordList = list(secretWord)
#    secWordList.sort()
#    print('Sorted word list', secWordList)
#    lettersGuessed.sort()
#    print('guessed word list', lettersGuessed)
#    for letInGuessed in lettersGuessed:
#        for letInWord in secWordList:
#            if (letInWord == letInGuessed):
#                secWordList.pop(secWordList.index(letInGuessed))
#    print secWordList
#    if(len(secWordList)>0):
#        return False
#    else:
#        return True
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    


secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
lettersGuessed = ['e', 'l', 'a', 'p']
#print isWordGuessed(secretWord, lettersGuessed)
print getGuessedWord(secretWord, lettersGuessed)

