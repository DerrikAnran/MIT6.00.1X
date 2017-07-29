import random
import math
class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE / 3

        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1

        for i in range(numVowels, self.HAND_SIZE):
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1

    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = self.hand.keys()
        hand_keys.sort()
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.

        word: string
        returns: Boolean (if the word was or was not made)
        """
        try:
            temp = self.hand.copy()
            for i in word:
                if temp.get(i, 0) != 0:
                    temp[i] -= 1
                else:
                    return False
            self.hand = temp
            return True
        except:
            raise NotImplementedError()
def genPrimes():
    prime = 2
    while True:
        for i in range(1, int(math.sqrt(prime)) + 1):
            if prime % i == 0 and i != 1:
                break
        else:
            yield prime
        prime += 1




import string
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    assert type(shift) == int
    result = {}
    strings = string.ascii_uppercase + string.ascii_lowercase
    for i in strings:
        if (ord(i) >= ord('a') and ord(i) <= ord('z') - shift) or ord(i) <= ord('Z') - shift:
            result[i] = chr(ord(i) + shift)
        else:
            result[i] = chr(ord(i) + shift - 26)
    return result
