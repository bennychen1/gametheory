import unittest
from creategame import StrategicGame

class TestGameStart(unittest.TestCase):
	def test_init(self):
		sg = StrategicGame(["A", "B"], ["X", "Y"], {"X": 2, "Y": 10})
		self.assertEqual(sg.players, ["A", "B"])

if __name__ == '__main__':
	unittest.main()