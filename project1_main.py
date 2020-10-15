import sys
import cv2 as cv
from mainWindow import Ui_mainWindow
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_mainWindow()
		self.ui.setupUi(self)
		self.ui.BTN_CORNER.clicked.connect(self.corner_clicked)

	def corner_clicked(self):
		# set window name
		QtWidgets.QMainWindow.setWindowTitle(self, "1.1 Find Corners")
		criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
		for i in range(1, 16):
			# load image name
			filename = ("Q1_Image/{}.bmp".format(i))
			# read the file
			img = cv.imread(filename)
			# convert image into black and white
			gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
			# find corners of the chess board and draw points on image
			ret, corners = cv.findChessboardCorners(gray, (8, 11), None)
			if ret == True:
				corners2 = cv.cornerSubPix(gray, corners, (8, 11), (-1, -1), criteria)
				cv.drawChessboardCorners(img, (8, 11), corners2, ret)
			# window of images
			windowName = ("Display Window {}".format(i))
			cv.namedWindow(windowName, 0);
			cv.resizeWindow(windowName, 500, 500);
			cv.imshow(windowName, img)
		# set window name
		QtWidgets.QMainWindow.setWindowTitle(self, "Main Window")

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
