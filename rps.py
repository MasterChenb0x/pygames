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
def nameConvert(num):
	'''
	Converts integers back to names after Maths.
	'''
	hands = ["Rock", "Paper", "Scissors"]
	return hands[num]

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
	print("Let's play Rock, Paper Scissors!")
	print("		Rock smashes Scissors")
	print("		Scissors cuts Paper.")
	print("		Paper covers Rock.")
	while play == "y":
		userSelect = input("Make your selection: (r)ock, (p)aper, or (s)cissors: ")
		userSelect = userSelect.lower()
		userSelect = selectionConvert(userSelect)
		compSelect = random.randint(0,2)
		outcome = compare(userSelect, compSelect)
		userSelect = nameConvert(userSelect)
		compSelect = nameConvert(compSelect)
		print("You selected " + userSelect)
		print("The computer selected " + compSelect)
		print(outcome)
		play = input("Would you like to play again? (y/N): ")

if __name__ == "__main__":
	main()
