#!/usr/bin/python

import sys
import random
import string

# Asks player if they would like to begin a new game
def newGame():
	while True:
		try:
			response = str(raw_input("Would you like to begin a new game of Hangman (Y or N)? ")).upper().strip()
			if response[0] == 'Y':
				return True
			if response[0] == 'N':
				return False
		except:
			pass

		print "I'm sorry, I didn't get that. "

# Extracts random word from chosen file
def extractWord():
	while True:
		try:
			file = raw_input("\nPlease enter the path or filename of your chosen wordbank: ")
			with open(file, 'r') as f:
				word = random.choice(f.read().split())
				return word
		except:
			pass

		print "Invalid path/filename. Please try again."

# Sets number of guesses for the game
def getNumGuesses():
	while True:
		try:
			numGuesses = int(raw_input("\nHow many guesses would you like to have? "))
			if numGuesses in range(1, 11):
				return numGuesses
		except:
			pass

		print "Invalid number of guesses. Please type a number from 1-10."

# Collects and validates letter guess
def getGuess():
	while True:
		try:
			guess = raw_input('\nPlease guess a letter: ').lower()
			if guess.isalpha() and len(guess) == 1:
				return guess
		except:
			pass
		print "Invalid character. Please type one letter."

# Ouputs chosen word as blanks and fills in letters as player
# guesses correctly
def getBlanks(gameWord, guesses):
    count = 0
    blanks = ['_ '] * len(gameWord)

    for i, j in enumerate(gameWord):
        if j in guesses:
            count += 1
            blanks.insert(count-1, j)
            blanks.pop(count)
            if count == len(gameWord):
                return ''.join(str(e) for e in blanks)
        else:
            count += 1
            blanks.insert(count-1,'_')
            blanks.pop(count)
            if count == len(gameWord):
                return ''.join(str(e) for e in blanks)

def hangman():
	# Initialize number of games played and won
	gamesWon = 0
	gamesPlayed = 0

	while newGame():
		gamesPlayed += 1

		# Set mystery word and initialize letters guessed
		gameWord = extractWord()
		guesses = ""

		# Initialize number of guesses for current game
		numGuesses = getNumGuesses()
		if numGuesses in range(1, 4):
			print "\nOh my, you must have a death wish."

		print "\nHere is your mystery word. Good luck!\n" + getBlanks(gameWord, guesses)

		# Collect and validate guesses; lose a guess with each wrong answer
		while numGuesses > 0:
			guess = getGuess()

			if guess in guesses:
				print "\nYou've already guessed that letter. Please try another one.\n"
			elif guess in gameWord:
				guesses += guess
				print "\nGood guess!\n"
			else:
				guesses += guess
				print "\nSorry, that letter is not in this word.\n"
				numGuesses -= 1
			
			print getBlanks(gameWord, guesses)

			# If player wins
			if getBlanks(gameWord, guesses) == gameWord:
				print "\nYOU WIN! Great job!"
				gamesWon += 1
				break
			print "Guesses left: " + str(numGuesses)
			print "Letters guessed: " + ''.join(sorted(guesses))

		# If player loses	
		if numGuesses == 0:
			print '\nSorry, the word was "' + gameWord + '". Game over. :('

		print "Games won this session: " + str(gamesWon) + " out of " + str(gamesPlayed) + "\n"

	print "Oh well, maybe next time. Goodbye!"

hangman()
