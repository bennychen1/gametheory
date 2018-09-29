import unittest
from creategame import StrategicGame, Player
from asimplegame import BertrandGame

'''class TestGameStart(unittest.TestCase):
	def test_init(self):
		sg = StrategicGame(["A", "B"], ["X", "Y"], {"X": 2, "Y": 10})
		self.assertEqual(sg.players, ["A", "B"])'''

class TestSimple(unittest.TestCase):
	def createGame(self, p1, p2):
		players = ["player1", "player2"]
		strategies = []
		strategies.append([i for i in range(p1)])
		strategies.append([i for i in range(p2)])
		game = BertrandGame(players, strategies, 1, 100)
		return game 

	def test_marketShareProfit(self):
		game = self.createGame(10, 9)
		marketShares = game.marketShare(10, 9)
		self.assertEquals(marketShares, [0, game.marketSize])
		self.assertEquals(game.profit(10, 9, marketShares[0], marketShares[1]), [0, 800])

	def test_BertrandGame(self):
		game = self.createGame(2, 2)
		matrixResult = {0: {0:[-50, -50], 1:[-100, 0], 2:[-100, 0]},
						1: {0: [0, -100], 1: [0, 0], 2: [0, 0]},
						2: {0: [0, 0], 1: [0, 0], 2: [50, 50]}}
		self.assertEquals(matrixResult, game.createMatrix())

if __name__ == '__main__':
	unittest.main()