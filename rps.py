#!/usr/local/bin/python3

import random

def selectionConvert(selection):
	if selection == "r":
		return 0
	elif selection == "p":
		return 1
	elif selection == "s":
		return 2

def compare(playerHand, computerHand):
	result = playerHand - computerHand
	if result % 3 == 0:
		return "TIE!"
	elif result % 3 == 1:
		return "WIN!"
	elif result % 3 == 2:
		return "LOSE!" 

userSelect = input("Make your selection: (r)ock, (p)aper, or (s)cissors: ")
userSelect = userSelect.lower()
print(userSelect)
userSelect = selectionConvert(userSelect)
print(userSelect)
compSelect = random.randint(0,2)
print(compSelect)
outcome = compare(userSelect, compSelect)
print(outcome)

