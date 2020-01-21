
import Main
import random

#below is the parent class Player to all the sub classes of player below
#only function modified by the subclasses is the function play() which 
#depends on the inheirtied class.
class Player:
	def __init__(self, player):
		self._name = player
	def name(self):
		return self._name
	def play():
		raise NotImplementedError("Not yet Implemented")

#only plays rock each round 
class StupidBot(Player):
	def __init__(self, stupid):
		super().__init__(stupid)
	def play(self):
		move = Main.move_choice(1)
		return move

#Random bot just selects at random an int btw 1 and 5 and plays that
class RandomBot(Player):
	def __init__(self, random):
		super().__init__(random)
	def play(self):
		randnum = random.randint(1, 5)
		move = Main.move_choice(randnum)
		return move

#iterativebot just adds 1 to counter after each move to rotate through all the moves
class IterativeBot(Player):
	def __init__(self, iterative):
		super().__init__(iterative)
	counter = 1
	def play(self):
		move = Main.move_choice(self.counter)
		self.counter += 1
		return move
'''
chose to just keep track of the other players previous moves within the function 
round in main.py.  Seems like a more efficent way then to modify the constrcutor
and keep passing new numbers.  So lastplaybot's play() is actually only ever called 
once in this program.
'''
class LastPlayBot(Player):
	def __init__(self, last):
		super().__init__(last)
	def play(self):
		move = Main.move_choice(1)
		return move

class Human(Player):
	def __init__(self, human):
		super().__init__(human)
	def play(self):
		print ('(1) : Rock\n(2) : Paper\n(3) : Scissors\n(4) : Lizard\n(5) : Spock')
		choice = int(input('Enter your move: '))
		while choice < 1 or choice > 5:
			print ('Invalid move.  Please try again')
			print ('(1) : Rock\n(2) : Paper\n(3) : Scissors\n(4) : Lizard\n(5) : Spock')
			choice = int(input('Enter your move: '))
		move = Main.move_choice(choice)
		return move

'''
My goal was to win the most rounds out of say 100 rounds against any combination of 
20 player slections.
MyBot was configured basded on probablity and my person perference.
When examining all players. Since one player the bot can possiblily play
only plays rock statistically speaking if I never play scissors or snake
the probably of wining will go up.  Since lastplay will play my moves it
would reason that I should also avoid playing my last move and a move that will lose 
to iteration so the order of cycling through the 4 other moves is also important. 
Iterator plays rock, paper, etc. So the order the bot should play should try and beat 
that each round as well.  
So to beat Stupid last and iterator my order should be 
paper, paper, spock, rock, paper
         W L T
supid:   4 1 0
iterator:4 0 1  
lastplay:2 2 1
since human and random are not predictable I wont account for them since I would rather
account for moves I know will happen against certian opponents. 
'''
class MyBot(Player):
	def __init__(self, bot):
		super().__init__(bot)
	count = 0
	moveNum = 2 #to start with paper
	def play(self): #2 2 5 1 2 
		if self.count == 2:
			self.moveNum = 5
		elif self.count == 3:
			self.moveNum = 1
		elif self.count == 4:
			self.moveNum = 2	
		move = Main.move_choice(self.moveNum)
		self.count += 1
		return move







