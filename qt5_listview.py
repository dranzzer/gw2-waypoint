import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class AppDemo():
	def __init__(self):
		super().__init__()
		mainLayout = QVBoxLayout()
		companies = ("a","b","c")
		model = QStandardItemModel(len(companies),1)
		model.setHorizontalHeaderLabels(['Company'])

		for row,company in enumerate(companies):
			item = QStandardItem(company)
			model.setItem(row,0,item)


		self.setLayout(mainLayout)


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())