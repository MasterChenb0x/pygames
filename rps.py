#!/usr/local/bin/python3

#Import the Universe
import random

#Reusable code (functions)
def selectionConvert(selection):
	'''
	Convert selection to an integer for Maths.
	'''
	if selection == "r":
		return 0
	elif selection == "p":
		return 1
	elif selection == "s":
		return 2

def compare(playerHand, computerHand):
	'''
	Function to calculate the winner
	'''
	result = playerHand - computerHand
	if result % 3 == 0:
		return "TIE!"
	elif result % 3 == 1:
		return "WIN!"
	elif result % 3 == 2:
		return "LOSE!" 

def main():
	#Set defaults
	play = "y"

	while play == "y":
		userSelect = input("Make your selection: (r)ock, (p)aper, or (s)cissors: ")
		userSelect = userSelect.lower()
		print(userSelect)
		userSelect = selectionConvert(userSelect)
		print(userSelect)
		compSelect = random.randint(0,2)
		print(compSelect)
		outcome = compare(userSelect, compSelect)
		print(outcome)
		play = input("Would you like to play again? (y/N): ")

main()
