import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class createGame(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		layout= QHBoxLayout()

		gameTypeSelect = QComboBox()
		gameTypeSelect.addItem('Regular')
		gameTypeSelect.addItem('Dyanmic')

		self.gameType = gameTypeSelect.currentText()

		layout.addWidget(gameTypeSelect)
		self.setLayout(layout)
		self.setGeometry(300, 300, 300, 300)
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = createGame()
	sys.exit(app.exec_())

