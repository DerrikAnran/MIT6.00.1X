# -*- coding: utf-8 -*-

# Hangman game
# 经典单词游戏Hangman的变形设计，第一玩家为你，第二玩家为计算机
# 计算机随机选择一个单词，并提示你该单词的长度，你有8次机会猜测
# 该单词中出现的字母，猜中不消耗次数，将所有单词中出现的字母都猜中
# 即为获胜

import random
import string

WORDLIST_FILENAME = "words.txt" # 词库

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print "Loading word list from file..."
    # inFile: file 打开词库txt文件
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string 读取打开的文件
    line = inFile.readline()
    # wordlist: list of strings 词库转为字符串列表
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    随机返回一词库(字符串)列表中的一个单词
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = list(secretWord)
    for i in range(len(result)):
        if result[i] not in lettersGuessed:
            result[i] = '_ '
    return ''.join(result)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    result = list(string.lowercase)
    for i in result[:]:
        if i in lettersGuessed:
            result.remove(i)
    return ''.join(result)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %d letters long." % len(secretWord)
    print "-------------"
    # 定义已猜测字母list，余下的未猜测字母string，猜错次数int
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    mistakesMade = 0
    while mistakesMade < 8:
        print "You have %d guesses left." % (8-mistakesMade)
        print "Available letters: %s" % availableLetters
        # 判断用户输入的字母规范正确与否
        letter = ''
        while len(letter) != 1 or (not letter.isalpha()):
            letter = raw_input("Please guess a letter: ")
        letter = letter.lower()
        if letter in lettersGuessed:
            print "Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(letter)
            availableLetters = getAvailableLetters(lettersGuessed)
            if letter in secretWord:
                print "Good guess: %s" % getGuessedWord(secretWord, lettersGuessed)
            else:
                print "Oops! That letter is not in my word: %s" % getGuessedWord(secretWord, lettersGuessed)
                mistakesMade += 1
        print "-------------"
        # 判断最终猜测结果正确与否
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
            break
        elif mistakesMade == 8:
            print "Sorry, you ran out of guesses. The word was %s." % secretWord


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords() # 载入单词表
secretWord = chooseWord(wordlist).lower() # 随机选词
hangman(secretWord) # 开始游戏
