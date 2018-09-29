class Player:
	'''
		name: string such as "player 1"
		strategies: a list such as ["Left", "Right", ...]
	'''

	def __init__(self, name, strategies):
		self.name = name 
		self.strategies = strategies

	def __repr__(self):
		return self.name




class StrategicGame:
	'''
		User inputs players, strategies available to players
		payoffs: user specify rules of game (need some way to turn rules into code)
			maybe user specifies combinations (if short) or type of game
		utilityFunctions: specify utility functions
		gameType: mixed/pure, dynamic, Bertrand, hotelling, dollar
		be able to compute pure strategy NE
		be able to print out a matrix
		turn into some GUI
		need some way for a 3 player game
	'''

	def __init__(self, players, strategies, rules, utilityFunctions, gameType):
		'''
			players: list of strings players ["A", "B"]
			strategies: list of list of strings for strategies (dictionary or list)
			rules: list of rules of game specifying what payoffs
			utilityFunctions: list U(m) = 2x - U(s)
			gameType: mixed/pure, dynamic, Bertrand, hotelling
		'''
		self.players = players
		self.strategies = strategies
		self.payoffs = payoffs
		self.rules = rules 
		self.utilityFunctions = utilityFunctions
		self.gameType = gameType

	def drawMatrix(self):
		assert()
		w = self.strategies[1].length # Player 2's strategies
		h = self.strategies[0].length
		matrix = [[0 for x in range(w)] for y in range(h)] 
		return matrix

	def drawTree(self):
		return None 

	def findNE(self):
		return None

	def iteratedDeletion(self):
		return None

	def findUtilities(self, player1Util, player2Util):
		return None

	def findMixedEquilibrium(self, strategies, utilityFunctions):


