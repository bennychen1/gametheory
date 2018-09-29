from creategame import StrategicGame, Player

class BertrandGame:
	def __init__(self, players, strategies, costs, marketSize):
		self.players = [Player(players[i], strategies[i]) for i in range(len(players))]
		self.costs = costs
		self.marketSize = marketSize

	def marketShare(self, p1, p2):
		if p1 < p2:
			return [self.marketSize, 0]
		elif p1 > p2:
			return [0, self.marketSize]
		else:
			half = makretSize / 2
			return [half, half]

	def profit(self, p1, p2, q1, q2):
		return [q1 * (p1 - self.costs), q2 * (p2 - self.costs)]


