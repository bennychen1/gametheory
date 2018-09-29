import unittest
from creategame import StrategicGame, Player
from asimplegame import BertrandGame

'''class TestGameStart(unittest.TestCase):
	def test_init(self):
		sg = StrategicGame(["A", "B"], ["X", "Y"], {"X": 2, "Y": 10})
		self.assertEqual(sg.players, ["A", "B"])'''

class TestSimple(unittest.TestCase):
	def createGame(self):
		players = ["player1", "player2"]
		strategies = []
		strategies.append([i for i in range(11)])
		strategies.append([i for i in range(11)])
		game = BertrandGame(players, strategies, 1, 100)
		return game 

	def test_marketShareProfit(self):
		game = self.createGame()
		marketShares = game.marketShare(10, 9)
		self.assertEquals(marketShares, [0, game.marketSize])
		self.assertEquals(game.profit(10, 9, marketShares[0], marketShares[1]), [0, 800])



		


if __name__ == '__main__':
	unittest.main()