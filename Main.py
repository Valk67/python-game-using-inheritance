#!/usr/bin/env python3
#Main.py

import Player
import Element

'''
Main funtion the begining of the program.  The user choses 2 players if not vaild choices it loops
and asks for 2 more.  Once two players are both valid it calles vsMessage that displays the message
of who is playing and then passes the players to function round which then has the two players play
5 rounds after this the program terminates.
'''
def main():
	print ('Welcome to Rock, Paper, Scissors, Lizard, Spock!\n')
	choose_players()
	input1 = int(input())
	input2 = int(input())
	while (input1 < 1 or input1 > 6) or (input2 < 1 or input2 > 6):
		print('Select player 1: Select player 2: Invalid choice(s). Please start over.\n')
		input1 = int(input())
		input2 = int(input()) 
	vsMessage(input1, input2)		

#vsmessage takes in 2 player types and prints the vs message and then calls function round
def vsMessage(input1, input2):
	p1 = playertype(input1)
	p2 = playertype(input2) 
	print ('Select player 1: Select player 2: '+ str(p1.name())+ ' vs. ' + str(p2.name()) +'. Go!\n')
	round (p1, p2) 

'''
Round is the main function that controls the game after the user determines two player types
Since each game is 5 rounds the while will run for 5 iterations.  Additionally a decent amount 
of code was written in this function to keep track of the last moves of each players.  This 
could of been used for mybot but chose a different strategy so its only relevent to player 
lastplaybot
'''
def round(play1, play2):
	lastmov1 = None 
	lastmov2 = None  
	p1score = 0
	p2score = 0	
	roundcounter = 1
	while roundcounter < 6:
		print ('Round '+ str(roundcounter) +': ')
		p1move = play1.play()
		p2move = play2.play() 
		if str(play1.name()) == 'LastPlayBot' or str(play2.name()) == 'LastPlayBot': 
			if str(play1.name()) == 'LastPlayBot' and roundcounter > 1:
				p1move = lastmov2
			elif str(play2.name()) == 'LastPlayBot' and roundcounter > 1:
				p2move = lastmov1
		#prints the players move choices to output
		print('Player 1 chose',p1move.name())
		print('Player 2 chose',p2move.name())
		
		#var is equal to the number that returns from compare which is defined
		#in each elements unique compareto function
		var = p1move.compareTo(p2move)
		if var == 1:
			print('Player 1 won the round.\n')
			p1score += 1
		elif var == -1:
			print('Player 2 won the round.\n')
			p2score += 1
		else:
			print('Round was a tie.\n')	
		#lastmov1 and lastmov2 saves the last move. used by lastplaybot
		roundcounter += 1
		lastmov1 = p1move
		lastmov2 = p2move
	#final score message that prints score and determines who wins
	print('Final score is ' + str(p1score) + ' to ' + str(p2score) + '.')
	if p1score > p2score:
		print('Player 1 wins.')
	elif p1score < p2score:
		print('Player 2 wins.')
	else:
		print('Game was a draw.')

#Move_choice returns a inheirted class from class element. These inheirted classes
#are the moves players use against each other
def move_choice(c_num):
	if c_num == 1:
		rock = Element.Rock('Rock') 	
		return rock
	elif c_num == 2:
		paper = Element.Paper('Paper')
		return paper
	elif c_num == 3:
		scissors = Element.Scissors('Scissors')
		return scissors
	elif c_num == 4:
		lizard = Element.Lizard('Lizard')
		return lizard
	elif c_num == 5:
		spock = Element.Spock('Spock')
		return spock

#returns the player class type to round function and then runs certian moves 
#based on the type of player they are.
def playertype (number):
	if number == 1:
		return Player.Human('Human')
	elif number == 2:
		return Player.StupidBot('StupidBot')
	elif number == 3:
		return Player.RandomBot('RandomBot')
	elif number == 4:
		return Player.IterativeBot('IterativeBot')
	elif number == 5:
		return Player.LastPlayBot('LastPlayBot')
	elif number == 6:
		return Player.MyBot('MyBot') 

#opening message that prompts the user to select 2 players
def choose_players():
	print ('Please choose two players: ')
	print ('1 : Human\n2 : StupidBot\n3 : RandomBot') 
	print ('4 : IterativeBot\n5 : LastPlayBot\n6 : MyBot')

#runs main function
if __name__ == "__main__":
	main() 
