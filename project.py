# 1) Randomly pick a word from a word bank
# 2) Hide the letters in a list
# 3) User Input
# 4) Reveal the letters
# 5) Win Condition
import sys
import string
import random

#Here is an extra comment
character_list = string.ascii_lowercase
word_list = ['this will be your real list']
word = (random.choice(word_list))
hidden = list(word)
new_string = ""
turns = 6
word_pizza = list(word)
letters_the_user_has_guessed = []







while turns > 0: 
    #This code hides the word and only shows the guessed letters
    user_output = []
    for letter in word:
        if letter in letters_the_user_has_guessed:
            user_output.append(letter)
        else:
            user_output.append('*')
    print user_output
    #This code asks for user input
    print "You have %d guess." %turns
    user_letter = raw_input("Guess a letter>")
    
    #This code looks to see if the letter is in the word
    if user_letter in ["quit", 'exit']:
        print "Bye"
        sys.exit(0)
    if user_letter not in word:
        print "Wrong! -1 turn"
        turns -=1
    letters_the_user_has_guessed.append(user_letter)
    if turns == 0:
        print "You Loose!"
        sys.exit(0)

                
    







