# program name: dice.py
# author: johnny
# date: 10/8/16

import random

random.seed()

def main():
	diceTable = {}
	while True:
		cmd = input('action: ')
		if cmd == 'q':
			break
		elif cmd.startswith('roll'):
			roll(cmd, diceTable)
		elif cmd.startswith('set'):
			action = setAction(cmd, diceTable)
			print('set {} to {}.'.format(action, diceTable[action]))

def setAction(cmdString, table):
	if cmdString == 'set':
		action = input('What action do you want to set? ')
		dice = input("What's the dice you want to roll for this action? ")
	else:
		actionList = cmdString.split(' ')
		action = actionList[1]
		dice = actionList[2]
	table[action] = dice
	return action

def calcRoll(multiplier, size, modifier):
	total = 0
	for i in range(multiplier):
		total += random.randint(1, size)
	total += modifier
	return total

def roll(cmdString, table):
	factors = [0]*3
	if cmdString == 'roll':
		dice = input("What's your roll (1d20+0)? ")
	else:
		dice = cmdString.split(' ')[1]
	if dice in table.keys():
		dice = table[dice]
	args = dice.replace('d', '+').split('+')
	args = [int(x) for x in args]
	for i in range(len(args)):
		factors[i] = args[i]
	multiplier = factors[0]
	size = factors[1]
	modifier = factors[2]
	total = calcRoll(multiplier, size, modifier)
	print('Rolling {}:{}'.format(dice, total))

if __name__ == '__main__':
	print('Basic usage:')
	print("To roll a dice: 'roll x' where x is something like 1d20+5. the + modifier is optional")
	print("To set an action: 'set x y' where x is an unspaced string.")
	print("y is the same dice format as is required to roll.")
	print("To call this, type 'roll <action>'")
	print("For example, 'set axe 1d20+5' will set your axe action to 1d20+5.")
	print("If you want to call your axe action, just type: 'roll axe'")
	main()