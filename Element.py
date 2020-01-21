#Ele.py

#class element is the parent class to all the elements rock, paper, etc
#compareTo is redifined by each inheirted class and the function name is 
#used in Main.py and not modified.
class Element:
	def __init__(self, element):
		self._name = element
	def name(self):
		return self._name
	def compareTo(self, inst_of_element):
		raise NotImplementedError("Note yet implemented")

'''
All the element inheirted classes below are pretty much the same 
except for the way they define compareTo.  Each element child 
class has a different set of rules when compared to another element
child's name funcion.
'''
class Rock(Element):
	def __init__(self, rock):
		super().__init__(rock)
	def compareTo(self, inst_of_element):
		if inst_of_element.name() == 'Paper':
			print ('Paper covers Rock')
			return -1
		elif inst_of_element.name() == 'Rock':
			print ('Rock equals Rock')
			return 0
		elif inst_of_element.name() == 'Scissors':
			print ('Rock crushes Scissors')
			return 1
		elif inst_of_element.name() == 'Spock':
			print ('Spock vaporizes Rock')
			return -1
		elif inst_of_element.name() == 'Lizard':
			print ('Rock crushes Lizard')
			return 1

class Paper(Element):
	def __init__(self, paper): 
		super().__init__(paper)
	def compareTo(self, insta_of_element):
		if insta_of_element.name() == 'Rock': 
			print ('Paper covers Rock')
			return 1
		elif insta_of_element.name() == 'Paper':
			print ('Paper equals Paper')
			return 0        
		elif insta_of_element.name() == 'Scissors':
			print ('Scissors cuts Paper')
			return -1
		elif insta_of_element.name() == 'Spock':
			print ('Paper disproves Spock')
			return 1
		elif insta_of_element.name() == 'Lizard':
			print ('Lizard eats Paper')
			return -1

class Scissors(Element):
	def __init__(self, scissors):
		super().__init__(scissors)
	def compareTo(self, insta_of_element):
		if insta_of_element.name() == 'Rock':
			print ('Rock crushes Scissors')
			return -1
		elif insta_of_element.name() == 'Paper':
			print ('Scissors cuts Paper')
			return 1
		elif insta_of_element.name() == 'Scissors':
			print ('Scissors equals Scissors')
			return 0
		elif insta_of_element.name() == 'Spock':
			print ('Spock smashes Scissors')
			return -1
		elif insta_of_element.name() == 'Lizard':
			print ('Scissors decapitate Lizard')
			return 1

class Spock(Element):
	def __init__(self, spock):
		super().__init__(spock)
	def compareTo(self, insta_of_element):
		if insta_of_element.name() == 'Rock':
			print ('Spock vaporizes Rock')
			return 1
		elif insta_of_element.name() == 'Paper':
			print ('Paper disproves Spock')
			return -1
		elif insta_of_element.name() == 'Scissors':
			print ('Spock smashes Scissors')
			return 1
		elif insta_of_element.name() == 'Lizard':
			print ('Lizard poisons Spock')
			return -1
		elif insta_of_element.name() == 'Spock':
			print ('Spock equals Spock')
			return 0

class Lizard(Element):
	def __init__(self, lizard):
		super().__init__(lizard)
	def compareTo(self, insta_of_element):
		if insta_of_element.name() == 'Rock':
			print ('Rock crushes Lizard')
			return -1
		elif insta_of_element.name() == 'Paper':
			print ('Lizard eats Paper')
			return 1
		elif insta_of_element.name() == 'Scissors':
			print ('Scissors decapitate Lizard')
			return -1
		elif insta_of_element.name() == 'Spock':
			print ('Lizard poisons Spock')
			return 1
		elif insta_of_element.name() == 'Lizard':
			print ('Lizard equals Lizard')
			return 0





