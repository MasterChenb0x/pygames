#!/usr/local/bin/python3

import random
import sys

flip = []

count = int(input("How many coin flips?: "))

for c in range(0, count):
	flip.append(random.randint(0,1))
print(flip[:])

for i in range(0,len(flip)):
	if flip[i] == 0:
		print("Heads")
	elif flip[i] == 1:
		print("Tails")

