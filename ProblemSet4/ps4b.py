from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    totalPoints = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if (isValidWord(word, hand, wordList)):
            # Find out how much making that word is worth
            currWordPoints = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (currWordPoints>totalPoints):
                # Update your best score, and best word accordingly
                totalPoints = currWordPoints
                bestWord = word
    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    totalPoints = 0
    while (calculateHandlen(hand)>0):
        print 'Current Hand: ',
        displayHand(hand)
        compStr = compChooseWord(hand, wordList, n)
        if (compStr != None):
            currPoints = getWordScore(compStr, n)
            hand = updateHand(hand, compStr)
            totalPoints += currPoints
            print '"', compStr, '" earned', currPoints, 'points. Total:', totalPoints, 'points.'
        else:
            break
    print 'Total score:', totalPoints, 'points.'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    # print "playGame not yet implemented." # <-- Remove this when you code this function
    playOpt = ''
    lastHand = dict()
    while (playOpt != 'e'):
        playOpt = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if (playOpt == 'n'):
            currHand = dealHand(HAND_SIZE)
            lastHand = currHand
            playOpt2 = ''
            while(playOpt2 != 'u' or playOpt2 != 'c'):
                playOpt2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if(playOpt2 == 'u'):                
                    playHand(currHand, wordList, HAND_SIZE)
                    break
                elif(playOpt2 == 'c'):
                    compPlayHand(currHand, wordList, HAND_SIZE)
                    break
                else:
                    print 'Invalid command.'
        elif (playOpt == 'r'):
            if (len(lastHand) != 0):
                playOpt2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if(playOpt2 == 'u'):                
                    playHand(currHand, wordList, HAND_SIZE)
                elif(playOpt2 == 'c'):
                    compPlayHand(currHand, wordList, HAND_SIZE)
                else:
                    print 'Invalid command.'
            else:
                print 'You have not played a hand yet. Please play a new hand first!'
        elif (playOpt == 'e'):
            break
        else:
            print 'Invalid command.'


        
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    wordScore = 0
    lenWord = len(word)
    if (lenWord == 0):
        return 0
    else:
        for ind in range(lenWord):
            wordScore += SCRABBLE_LETTER_VALUES[word[ind]]
        wordScore *= lenWord
        if (lenWord==n):
            wordScore += 50
        return wordScore


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    try:
        newHand = hand.copy()
        for ind in range(len(word)):
            x = word[ind]
            newHand[x] = newHand.get(x,0) - 1
            if (newHand[x] < 0):
                raise KeyError('')
        return True
    except KeyError, e:
        return False


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


